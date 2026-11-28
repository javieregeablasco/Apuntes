#!/bin/bash

# Registrar toda la salida del script
exec > >(tee -a /var/log/user-data.log) 2>&1

set -euxo pipefail

echo "======================================"
echo " INICIANDO INSTALACION DEL SERVIDOR WEB"
echo "======================================"

# Actualizar repositorios
apt-get update

# Instalar actualizaciones
sudo apt-get upgrade -y

# Instalar Apache
DEBIAN_FRONTEND=noninteractive apt-get install -y apache2

# Instalar node 
sudo apt-get install nodejs npm -y

# Directorio para la API
mkdir /home/ubuntu/api-web
cd /home/ubuntu/api-web
npm init -y
npm install express mysql2

# -------------------------------------
# Crear archivo de configuracion inicio
# -------------------------------------
cat > /home/ubuntu/api-web/server.js << 'EOF'
const express = require('express');
const mysql = require('mysql2/promise');

const app = express();
const PORT = 3000;

// Configuracion de la conexion a MariaDB
const db = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: 'appdb',
    waitForConnections: true,
    connectionLimit: 10
});

// Endpoint para consultar un cliente por su ID
app.get('/api/clientes/:id', async (req, res) => {

    try {
        const id = Number(req.params.id);

        if (!Number.isInteger(id) || id < 1) {
            return res.status(400).json({
                error: 'Identificador no valido'
            });
        }

        const [filas] = await db.execute(
            'SELECT id, nombre, email FROM clientes WHERE id = ?',
            [id]
        );

        if (filas.length === 0) {
            return res.status(404).json({
                error: 'Cliente no encontrado'
            });
        }

        res.json(filas[0]);

    } catch (error) {
        console.error('Error consultando MariaDB:', error);

        res.status(500).json({
            error: 'Error interno del servidor'
        });
    }
});

// Iniciar API exclusivamente en localhost
app.listen(PORT, '127.0.0.1', () => {
    console.log(`API funcionando en el puerto ${PORT}`);
});
EOF
# -------------------------------------
# Crear archivo de configuracion fin
# -------------------------------------

# ----------------------------------
# Configurar las credenciales inicio
# ----------------------------------
cat > /etc/api-web.env << 'EOF'
DB_HOST=10.0.1.50
DB_USER=appuser
DB_PASSWORD=TU_CONTRASEÑA
EOF
# ----------------------------------
# Configurar las credenciales fin
# ----------------------------------

# Proteger archivo
sudo chmod 600 /etc/api-web.env

# -------------------------------------
# Crear un servicio para Node.js INICIO
# -------------------------------------
cat > /etc/systemd/system/api-web.service << 'EOF'
[Unit]
Description=API Node.js para MariaDB
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/api-web
EnvironmentFile=/etc/api-web.env
ExecStart=/usr/bin/node /home/ubuntu/api-web/server.js
Restart=always

[Install]
WantedBy=multi-user.target
EOF
# -------------------------------------
# Crear un servicio para Node.js FIN
# -------------------------------------

# Activar API
sudo systemctl daemon-reload
sudo systemctl enable --now api-web

# Configurar Apache como intermediario
sudo a2enmod proxy proxy_http

# Crear la configuracion para redirigir las peticiones API hacia Node.js
cat > /etc/apache2/conf-available/api-web.conf << 'EOF'
ProxyPreserveHost On

ProxyPass /api http://127.0.0.1:3000/api
ProxyPassReverse /api http://127.0.0.1:3000/api
EOF


# Activar Apache
sudo a2enconf api-web
sudo apache2ctl configtest
systemctl enable apache2
systemctl start apache2
sudo systemctl restart apache2

# Crear página web 
cat > /var/www/html/index.html <<'EOF'
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidor Web AWS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #9dc1e6;
            text-align: center;
            padding: 80px 20px;
        }
        .contenedor {
            background: rgb(236, 193, 193);
            max-width: 650px;
            margin: auto;
            padding: 40px;
            border-radius: 12px;
            margin-bottom: 25px;
        }
        
        .contenedor_2 {
            background: lightgray;
            max-width: 650px;
            margin: auto;
            padding: 40px;
            border-radius: 12px;
        }
        .consultarCliente {
            background: rgb(221, 235, 220);
            max-width: 500px;
            margin: auto;
            padding: 20px;
            border-radius: 6px;
        }

        .aspectoBoton {
            background: rgb(69, 173, 221);
            margin: auto;
            margin-top: 20px;
            display: block;
            border-radius: 6px;
            padding: 8px 16px;
            border: none;
            cursor: pointer;
        }

        h1 { color: #e47911; }
        h2 { color: #203acf; }
    </style>
</head>

<body>

    <div class="contenedor">
      <h1>¡Servidor web funcionando!</h1>
      <p>Instancia EC2 de AWS.</p>
      <p>Ubuntu Server + Apache2</p>
      <h2>Creado por Javier Egea Blasco</h2>
    </div>
    
    <div class="contenedor_2">
      <h1>Consulta de clientes</h1>
      <p>Esta página permite consultar los datos de un cliente mediante su ID.</p>
    
      <div class="consultarCliente">
        <label for="idCliente">ID del cliente:</label>
        <input type="number" id="idCliente" value="1" min="1">
        <button onclick="consultarCliente()" class="aspectoBoton">
            Consultar
        </button>
        <div id="resultado"></div>
      </div>
    </div>  

    <script>
        async function consultarCliente() {
            const id = document.getElementById('idCliente').value;
            const resultado = document.getElementById('resultado');

            resultado.textContent = 'Consultando...';

            try {
                const respuesta = await fetch(`/api/clientes/${id}`);
                const datos = await respuesta.json();

                if (!respuesta.ok) {
                    throw new Error(datos.error);
                }

                resultado.innerHTML = `
                    <h2>Datos del cliente</h2>
                    <p><strong>ID:</strong> ${datos.id}</p>
                    <p><strong>Nombre:</strong> ${datos.nombre}</p>
                    <p><strong>Email:</strong> ${datos.email}</p>
                `;

            } catch (error) {
                resultado.textContent = 'Error: ' + error.message;
            }
        }
    </script>

</body>
</html>
EOF

# Permisos
chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html

# Reiniciar Apache
systemctl restart apache2

# Comprobación
systemctl is-active apache2

echo "======================================"
echo " INSTALACION FINALIZADA CORRECTAMENTE"
echo "======================================"