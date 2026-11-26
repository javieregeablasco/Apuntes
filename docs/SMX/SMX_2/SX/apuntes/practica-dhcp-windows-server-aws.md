

## 7 - [Windows Server] Transferencia de ficheros con FileZilla y diagnóstico de modo pasivo (RA3-CEe)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

Una vez instalado y configurado el servidor FTP en **Windows Server (`Servidor_FTPSSH`)**, vamos a verificar inmediatamente desde nuestro equipo del aula que el canal de control (`21` TCP) y el canal de datos en **modo pasivo** (`50000-50100` TCP) funcionan correctamente antes de avanzar a configuraciones más complejas.

---

### 7.1 Conexión y transferencia hacia Windows Server con FileZilla

> ⚠️ **¿Retomas la práctica en un día diferente o tras reiniciar Windows Server?**
>
> Si la instancia `Servidor_FTPSSH` se ha detenido y reiniciado hoy, **su IP pública habrá cambiado**:
> * **En FileZilla:** Introduce en el campo **Servidor** la **nueva IP pública de Windows** (consúltala en la consola de AWS EC2).
> * **Problema típico si no actualizas IIS:** FileZilla conectará con éxito al puerto 21 (`230 User logged in`), pero al enviar la orden `PASV` el servidor responderá con la IP vieja. FileZilla se quedará esperando y fallará con `Error: Conexión superó el tiempo de espera` y `No se pudo recibir la lista de directorios`.
> * 👉 **Solución:** Actualiza la IP pública en IIS siguiendo el [Apartado 6.5: Soporte de Firewall de FTP](#actualizar-ip-windows) (o ejecuta el comando rápido de PowerShell indicado allí).
>

1. Abrir **FileZilla Client** en vuestro ordenador del aula.
2. En la barra superior de **Conexión rápida** introducir:
   * **Servidor:** `<IP_PUBLICA_WINDOWS>` (en nuestro ejemplo, `52.90.151.179`)
   * **Nombre de usuario:** `alumne_redes`
   * **Contraseña:** `Smx2026..@`
   * **Puerto:** `21` (si se deja en blanco, FileZilla utiliza por defecto el puerto `21`)
3. Pulsar en el botón **Conexión rápida**.
4. Al tratarse inicialmente de una conexión FTP estándar sin cifrar (antes de configurar FTPS en la Tarea 9), FileZilla mostrará la ventana emergente **Conexión FTP insegura** (**Este servidor no es compatible con FTP sobre TLS**). Pulsar en **Aceptar**:

![Conexión rápida en FileZilla y aviso de conexión FTP sin cifrar](./07_Transferencia_Ficheros_FTP_SSH/imagenes/32_filezilla_aviso_ftp_inseguro.png)
*Figura 32: Introducción de credenciales en la barra de Conexión rápida de FileZilla y confirmación del diálogo de conexión FTP en el puerto 21.*

5. Comprobar que en el log de conexión superior aparece el listado correcto del directorio (`Directorio "/" listado correctamente`) gracias al modo pasivo configurado.
6. Crear en vuestro PC un archivo llamado `Prova_ftp.txt` (o `prueba_win.txt`) y subirlo arrastrándolo al panel derecho (Sitio remoto `/`). Comprobar en la pestaña inferior **Transferencias satisfactorias (1)** que el fichero se ha transferido sin errores:

![Transferencia de archivo completada con éxito hacia Windows Server en FileZilla](./07_Transferencia_Ficheros_FTP_SSH/imagenes/33_filezilla_transferencia_ftp_ok.png)
*Figura 33: Directorio raíz listado en modo pasivo y archivo Prova_ftp.txt transferido con éxito al servidor Windows Server.*

> 📷 **Evidencia 8 (insertar en tu documento Word) — Realizar captura de pantalla** de FileZilla mostrando la conexión exitosa en modo pasivo y el archivo subido al servidor Windows Server.

---

### 7.2 Diagnóstico de avería: Bloqueo del modo pasivo por cortafuegos o IP externa

* **Escenario de la incidencia:** Un usuario introduce su usuario y contraseña en FileZilla correctamente (`230 User logged in`), pero justo después la conexión se queda congelada mostrando `Comando: MLSD` o `LIST` y tras 20 segundos devuelve `Error: Conexión superó el tiempo de espera. No se pudo recuperar el listado del directorio`.
* **Causa técnica:** El canal de control (puerto `21`) está abierto, pero el canal de datos pasivo (`50000-50100`) está bloqueado por el Firewall de Windows Defender (`wf.msc`), por el Security Group de AWS, o bien se olvidó introducir la IPv4 pública de AWS en **FTP Firewall Support** de IIS.
* **Comprobación práctica:**
  1. Verificar en el log superior de FileZilla que el servidor responde al comando `PASV` con la IP pública correcta y un puerto del rango `50000-50100`.
  2. Verificar en Windows Server que la regla `FTP Pasivo Datos (50000-50100)` está activa en `wf.msc`.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 7**
>
> En el **Apartado 7** de tu documento Word, incluye:
>
> * **Evidencia 8:** Captura de FileZilla mostrando la conexión exitosa en modo pasivo hacia Windows Server y el archivo `Prova_ftp.txt` transferido en la pestaña de **Transferencias satisfactorias**.
>

---

## 8 - [Windows Server] Aislamiento de usuarios (User Isolation), carpeta pública y permisos NTFS (RA3-CEd)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

En un entorno empresarial real, cada departamento o usuario debe disponer de un espacio privado exclusivo para almacenar sus ficheros confidenciales, sin que otros usuarios puedan acceder ni manipularlos. Además, suele habilitarse una carpeta pública compartida (para catálogos, formularios o drivers) accesible por cualquier usuario de forma anónima, pero con permisos estrictos de solo lectura.

---

### 8.1 Creación de usuarios departamentales y estructura LocalUser en Windows Server

> 💡 **¿Retomas este apartado en una sesión posterior?**
>
> * **Comprobación de IP:** Conéctate con FileZilla utilizando la IP pública actual de Windows Server. Asegúrate de que la IP en IIS esté actualizada ([Apartado 6.5](#actualizar-ip-windows)).
> * **Requisitos previos:** Verifica que tienes la estructura de carpetas `C:\inetpub\ftproot\LocalUser` creada y el usuario `usuari_ventas` dado de alta en Windows Server con los permisos NTFS correspondientes.
>

1. Abrir **Computer Management** (`compmgmt.msc`).
2. Desplegar **Local Users and Groups** -> carpeta **Users**.
3. Crear dos usuarios locales nuevos (**New User...**):
   * **User 1:** `usuari_ventas` (Password: `Smx2026..@`).
   * **User 2:** `usuari_compras` (Password: `Smx2026..@`).
   * Para ambos usuarios: desmarcar **User must change password at next logon**, y marcar **User cannot change password** y **Password never expires**.
4. Abrir **File Explorer** en `C:\inetpub\ftproot` y crear la siguiente estructura exacta de carpetas y archivos de prueba dentro de `LocalUser` (en IIS, cuando se activa el aislamiento por nombre de usuario, los usuarios locales entran en `LocalUser\<usuario>` y el usuario `anonymous` entra automáticamente en `LocalUser\Public`):
   ```text
   C:\inetpub\ftproot\
   └── LocalUser\
       ├── alumne_redes\
       ├── usuari_ventas\
       │   └── informe_ventas_privado.txt
       ├── usuari_compras\
       │   └── presupuesto_compras_privado.txt
       └── Public\
           └── catalogo_empresa_2026.pdf
   ```
5. Conceder permisos NTFS de modificación (**Modify**) a `usuari_ventas` sobre su carpeta `C:\inetpub\ftproot\LocalUser\usuari_ventas` y a `usuari_compras` sobre `C:\inetpub\ftproot\LocalUser\usuari_compras` (pestaña **Security** -> **Edit...** -> **Add...**), manteniendo la carpeta `LocalUser\Public` únicamente con permisos de lectura para `IUSR` / `Users`:

![Estructura de carpetas dentro de C:\inetpub\ftproot\LocalUser](./07_Transferencia_Ficheros_FTP_SSH/imagenes/33b_ftproot_localuser_carpetas.png)
*Figura 33b: Estructura física de carpetas en C:\inetpub\ftproot\LocalUser para usuarios locales aislados y carpeta Public para acceso anónimo.*

> 📷 **Evidencia 9 (insertar en tu documento Word) — Realizar captura de pantalla** de File Explorer en Windows Server mostrando la estructura de carpetas dentro de `C:\inetpub\ftproot\LocalUser`.

---

### 8.2 Configuración del Aislamiento de Usuarios en IIS (FTP User Isolation)

1. Abrir **Internet Information Services (IIS) Manager** (`inetmgr`).
2. Desplegar el servidor -> carpeta **Sites** -> hacer clic sobre el sitio **`FTP-AULA`**.
3. En el panel central, hacer doble clic sobre el icono **FTP User Isolation**.
4. Dentro de **Isolate users. Restrict users to the following directory:**, seleccionar la opción: **User name directory (disable global virtual directories)**.
5. En el panel lateral derecho (**Actions**), hacer clic en **Apply**:

![Configuración de FTP User Isolation en IIS Manager](./07_Transferencia_Ficheros_FTP_SSH/imagenes/33c_iis_ftp_user_isolation.png)
*Figura 33c: Activación de la directiva User name directory (disable global virtual directories) en FTP User Isolation.*

---

### 8.3 Configuración de Acceso Anónimo (Solo Lectura) y Reglas de Autorización

1. En IIS, seleccionar el sitio **`FTP-AULA`** -> hacer doble clic en el icono **FTP Authentication**:
   * Seleccionar **Anonymous Authentication** y en el panel derecho (**Actions**) pulsar en **Enable** para que su estado pase a **Enabled** (junto con **Basic Authentication** en **Enabled**).
2. Volver al sitio **`FTP-AULA`** -> hacer doble clic en el icono **FTP Authorization Rules**:
   * Pulsar en **Add Allow Rule...** en el panel derecho:
     - **Regla 1 (Usuarios departamentales con Lectura y Escritura):** Seleccionar **Specified users**, escribir `alumne_redes, usuari_ventas, usuari_compras` y marcar los permisos **Read** y **Write** -> pulsar **OK**.
     - **Regla 2 (Usuarios anónimos con Solo Lectura):** Pulsar de nuevo en **Add Allow Rule...**, seleccionar **All anonymous users** y en **Permissions** marcar únicamente **Read** (manteniendo **Write** desmarcado) -> pulsar **OK**:

![Reglas de autorización para usuarios anónimos (Read) y usuarios locales (Read, Write)](./07_Transferencia_Ficheros_FTP_SSH/imagenes/33d_iis_ftp_authorization_rules.png)
*Figura 33d: Reglas de autorización en FTP Authorization Rules concediendo solo lectura a Anonymous Users y lectura/escritura a los usuarios locales.*

---

### 8.4 Verificación del aislamiento y permisos desde FileZilla

1. Abrir **FileZilla Client** en vuestro PC del aula.
2. **Prueba de usuario aislado (`usuari_ventas`):**
   * En la barra de **Conexión rápida**, introducir Servidor `<IP_PUBLICA_WINDOWS>`, Nombre de usuario `usuari_ventas`, Contraseña `Smx2026..@` y Puerto `21` -> pulsar **Conexión rápida**.
   * Comprobar que accede directamente a su raíz privada (`/`) donde ve exclusivamente su archivo `informe_ventas_privado.txt`, sin posibilidad de subir de nivel ni ver la carpeta de `usuari_compras`:

![Conexión aislada de usuari_ventas en FileZilla mostrando su directorio privado](./07_Transferencia_Ficheros_FTP_SSH/imagenes/33e_filezilla_usuari_ventas_aislado.png)
*Figura 33e: Usuario usuari_ventas enjaulado en su directorio privado viendo únicamente informe_ventas_privado.txt.*

3. **Prueba de usuario anónimo (`anonymous` - Solo Lectura):**
   * En la barra de **Conexión rápida**, introducir Servidor `<IP_PUBLICA_WINDOWS>`, Nombre de usuario `anonymous` (o dejar usuario y contraseña en blanco) y Puerto `21` -> pulsar **Conexión rápida**.
   * Comprobar que accede directamente a la carpeta pública (`LocalUser\Public`) y ve el archivo `catalogo_empresa_2026.pdf` (pudiendo descargarlo sin problema).
   * Intentar **borrar `catalogo_empresa_2026.pdf`** (o subir un archivo desde el panel izquierdo hacia el servidor).
   * Comprobar que el servidor FTP deniega la escritura o el borrado devolviendo el código de error **`Respuesta: 550 Access is denied`**:

![Conexión anónima en FileZilla mostrando el archivo público y el error 550 Access is denied al intentar borrarlo](./07_Transferencia_Ficheros_FTP_SSH/imagenes/33f_filezilla_anonymous_550_denied.png)
*Figura 33f: Acceso anónimo de solo lectura a la carpeta Public con denegación de borrado/escritura (550 Access is denied).*

> 📷 **Evidencia 10 (insertar en tu documento Word) — Realizar captura de pantalla** de FileZilla mostrando la vista privada de `usuari_ventas` y otra captura mostrando el error `550 Access is denied` al intentar subir o borrar un fichero como usuario `anonymous`.

---

### 8.5 Diagnóstico de avería: Error 550 en usuarios locales por discrepancia de permisos NTFS

* **Escenario de la incidencia:** El usuario `usuari_ventas` se conecta por FTP correctamente, pero al intentar subir un fichero o crear una carpeta en su propio directorio recibe `Respuesta: 550 Access is denied`.
* **Causa técnica:** Aunque en IIS Manager las **FTP Authorization Rules** permitan escribir (`Read, Write`), los permisos de seguridad del sistema de ficheros de Windows (**NTFS**) de la carpeta física `C:\inetpub\ftproot\LocalUser\usuari_ventas` no conceden permiso de modificación (`Modify`) al usuario local.
* **Resolución:** Hacer clic derecho sobre la carpeta del usuario -> **Properties** -> pestaña **Security** -> **Edit...** -> **Add...** -> añadir al usuario y marcar **Modify** y **Write**.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 8**
>
> En el **Apartado 8** de tu documento Word, incluye las **Evidencias 9 y 10**:
>
> * **Evidencia 9:** Estructura de carpetas dentro de `C:\inetpub\ftproot\LocalUser` en el Explorador de archivos de Windows Server.
> * **Evidencia 10:** Capturas en FileZilla mostrando la vista privada aislada de `usuari_ventas` (`informe_ventas_privado.txt`) y el error `550 Access is denied` al intentar borrar o subir archivos como usuario `anonymous`.
>

---

## 9 - [Windows Server] Seguridad y cifrado con FTPS (FTP sobre TLS/SSL) (RA3-CEf)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

El protocolo FTP tradicional transmite contraseñas y datos en texto claro sin cifrar. En esta tarea aseguraremos nuestro servidor **Windows Server (`Servidor_FTPSSH`)** mediante **FTPS (FTP sobre SSL/TLS)**, creando un certificado digital autofirmado en IIS e implementando cifrado obligatorio.

---

### 9.1 Creación de un Certificado Digital Autofirmado en Windows Server

> 💡 **¿Retomas este apartado en una sesión posterior?**
>
> * **Comprobación de IP:** Utiliza la IP pública actual de Windows en FileZilla y confirma que el modo pasivo de IIS tiene la IP al día ([Apartado 6.5](#actualizar-ip-windows)).
> * **Aviso de certificado al cambiar de IP:** Al cambiar la IP pública de la máquina, FileZilla detectará la conexión como un nuevo destino y volverá a mostrar la ventana de validación del certificado autofirmado `Certificado-FTPs-Aula`. Simplemente marca **Confiar siempre en este certificado** y pulsa **Aceptar**.
>

1. Abrir **Internet Information Services (IIS) Manager** (`inetmgr`).
2. En el panel izquierdo (**Connections**), hacer clic sobre el **nombre del servidor** (nodo raíz).
3. En el panel central, dentro del bloque **IIS**, hacer doble clic en el icono **Server Certificates**:

![Acceso a Server Certificates desde el nodo raíz de IIS Manager](./07_Transferencia_Ficheros_FTP_SSH/imagenes/36_iis_icono_server_certificates.png)
*Figura 36: Selección del nodo raíz del servidor y acceso a Server Certificates en IIS Manager.*

4. En el panel lateral derecho (**Actions**), hacer clic en el enlace **Create Self-Signed Certificate...**:

![Opción Create Self-Signed Certificate en la columna Actions](./07_Transferencia_Ficheros_FTP_SSH/imagenes/37_iis_create_self_signed_link.png)
*Figura 37: Acceso al asistente de creación de certificado autofirmado.*

5. En la ventana **Specify Friendly Name**:
   * **Specify a friendly name for the certificate:** `Certificado-FTPs-Aula`
   * **Select a certificate store for the new certificate:** Mantener seleccionado `Personal`.
   * Pulsar en **OK**.

![Asignación del nombre Certificado-FTPs-Aula y almacén Personal](./07_Transferencia_Ficheros_FTP_SSH/imagenes/38_iis_friendly_name_certificado.png)
*Figura 38: Configuración del nombre descriptivo Certificado-FTPs-Aula en el almacén Personal.*

6. Comprobar que el certificado `Certificado-FTPs-Aula` aparece listado en el panel central de **Server Certificates** con su fecha de caducidad (**Expiration Date**) y su huella (**Certificate Hash**):

![Certificado autofirmado Certificado-FTPs-Aula creado y listado en IIS](./07_Transferencia_Ficheros_FTP_SSH/imagenes/39_iis_certificado_creado.png)
*Figura 39: Certificado digital Certificado-FTPs-Aula generado en el servidor.*

> 📷 **Evidencia 11 (insertar en tu documento Word) — Realizar captura de pantalla** del panel Server Certificates mostrando el nuevo certificado creado con su fecha de caducidad y emisor.

---

### 9.2 Configuración del cifrado SSL en el sitio FTP (FTP SSL Settings)

1. En el panel izquierdo de IIS, desplegar **Sites** y hacer clic sobre el sitio FTP **`FTP-AULA`**.
2. En el panel central, hacer doble clic en el icono **FTP SSL Settings**:

![Acceso a FTP SSL Settings dentro del sitio FTP-AULA](./07_Transferencia_Ficheros_FTP_SSH/imagenes/40_iis_icono_ftp_ssl_settings.png)
*Figura 40: Selección del sitio FTP-AULA y apertura de FTP SSL Settings.*

3. Configurar el cifrado del sitio:
   * En el desplegable **SSL Certificate**, seleccionar `Certificado-FTPs-Aula`.
   * En la directiva **SSL Policy**, marcar **Require SSL connections**.
   * En el panel lateral derecho (**Actions**), hacer clic en **Apply**.

![Selección del certificado Certificado-FTPs-Aula y política Require SSL connections](./07_Transferencia_Ficheros_FTP_SSH/imagenes/41_iis_ftp_ssl_require.png)
*Figura 41: Asignación del certificado Certificado-FTPs-Aula y activación de Require SSL connections en FTP SSL Settings.*

4. Reiniciar el sitio FTP pulsando en **Restart** dentro de la sección **Manage FTP Site** de la columna derecha de IIS (o reiniciando **Microsoft FTP Service** desde `services.msc`).

---

### 9.3 Conexión segura con FileZilla y validación de certificado TLS

1. Abrir **FileZilla Client** en vuestro PC del aula.
2. Conectar hacia el servidor en el puerto **`21`** (podéis hacerlo directamente desde la barra de **Conexión rápida** introduciendo Servidor `<IP_PUBLICA_WINDOWS>`, Usuario `alumne_redes`, Contraseña `Smx2026..@` y Puerto `21`, ya que FileZilla negocia automáticamente **FTP explícito sobre TLS** si el servidor lo soporta, o bien guardando el perfil en **Archivo** -> **Gestor de sitios...** con cifrado **Requiere FTP explícito sobre TLS**).
3. Pulsar en **Conexión rápida** (o **Conectar**).
4. Al establecer la negociación segura en el puerto `21`, aparecerá la ventana emergente **Certificado desconocido**:
   * Revisar la información del bloque **Certificado**: huella digital (**SHA-256**) y período de validez, así como los **Detalles de la sesión** (`Protocolo: TLS1.2`, `Cifrado: AES-256-GCM`).
   * Marcar la casilla **Confiar siempre en este certificado en futuras sesiones**.
   * Pulsar en **Aceptar**:

![Validación del certificado TLS 1.2 y huella SHA-256 en FileZilla](./07_Transferencia_Ficheros_FTP_SSH/imagenes/42_filezilla_certificado_tls_ftps.png)
*Figura 42: Verificación del certificado digital autofirmado (SHA-256) y sesión cifrada TLS 1.2 (AES-256-GCM) en el puerto 21.*

5. Comprobar en el panel de log de FileZilla que se negocia el cifrado del canal de datos (`Respuesta: 200 PBSZ command successful` y `Comando: PROT P` -> `200 PROT command successful`) y se lista el directorio raíz (`Directorio "/" listado correctamente`).
6. En la barra de estado inferior derecha de FileZilla, comprobar que aparece el **icono del candado cerrado** indicando que tanto el canal de control como el canal de datos viajan cifrados mediante TLS 1.2:

![FileZilla conectado por FTPS mostrando los comandos PBSZ/PROT P y el candado de cifrado](./07_Transferencia_Ficheros_FTP_SSH/imagenes/43_filezilla_ftps_conectado_candado.png)
*Figura 43: Conexión FTPS establecida en el puerto 21 con cifrado del canal de datos (PROT P) y candado de seguridad activo.*

> 📷 **Evidencia 12 (insertar en tu documento Word) — Realizar captura de pantalla** de la ventana del certificado en FileZilla mostrando la huella digital SHA-256 y de FileZilla conectado con el candado de conexión segura activo.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 9**
>
> En el **Apartado 9** de tu documento Word, incluye las **Evidencias 11 y 12**:
>
> * **Evidencia 11:** Panel **Server Certificates** de IIS mostrando el certificado `Certificado-FTPs-Aula` creado.
> * **Evidencia 12:** Ventana de validación del certificado TLS (huella SHA-256) en FileZilla y sesión FTPS conectada mostrando los comandos `PBSZ 0` / `PROT P` y el candado de seguridad activo.
>

---

## 10 - [Windows Server] Administración remota y bastionado de SSH con PuTTY y PuTTYgen (RA3-CEf)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

El acceso por contraseña convencional está expuesto a ataques de fuerza bruta. En esta tarea aprovecharemos el servicio **OpenSSH Server** que dejamos activo en **Windows Server (`Servidor_FTPSSH`)** en el apartado 6.3.1 para conectar remotamente por el puerto `22` con **PuTTY**, generar un par de claves asimétricas con **PuTTYgen** y bastionar el servidor deshabilitando el acceso por contraseña.

---

### 10.1 Conexión SSH básica hacia Windows Server con PuTTY

> ⚠️ **¿Retomas la práctica en un día diferente para configurar SSH?**
>
> * **Problema si usas la IP vieja:** Si introduces en PuTTY la IP del día anterior, la conexión se quedará congelada y devolverá `Network error: Connection timed out`.
> * **Solución:** Consulta la **nueva IP pública** de `Servidor_FTPSSH` en la consola de AWS EC2 ([Apartado 6.0](#60-lanzamiento-de-la-instancia-ec2-de-windows-server-2022-en-aws)) e indícala en el campo **Host Name** de PuTTY con el puerto `22`.
> * **Alerta de clave host en PuTTY:** Al cambiar la IP, PuTTY mostrará el aviso `The server's host key is not cached in the registry`. Es un comportamiento completamente normal; haz clic en **Accept** para continuar.
>

1. Abrir **PuTTY** en vuestro PC del aula.
2. En el campo **Host Name (or IP address)** introducir la **IP pública de Windows Server** (`<IP_PUBLICA_WINDOWS>`), **Port** `22` y **Connection type** `SSH`.
3. Pulsar en **Open**, aceptar la advertencia inicial de clave host del servidor (**PuTTY Security Alert** pulsando `Accept`) e iniciar sesión indicando el usuario `alumne_redes` y su contraseña (`Smx2026..@`).
4. Al entrar, ejecutar `whoami` y `hostname` para verificar que estáis conectados a la consola de comandos remota de Windows Server.

No obstante, el método profesional y seguro recomendado para entornos de producción es **sustituir las contraseñas por autenticación asimétrica de clave pública** y bastionar el servicio, tal y como configuramos a continuación.

---

### 10.2 Generación del par de claves con PuTTYgen

1. En vuestro ordenador del aula, abrir **PuTTYgen** (**PuTTY Key Generator**).
2. En la parte inferior (**Parameters**), mantener seleccionado el tipo de clave **RSA** (`2048` bits) o **EdDSA (Ed25519)**.
3. Pulsar en el botón **Generate** y mover continuamente el cursor del ratón sobre el área vacía para generar entropía criptográfica aleatoria:

![Parámetros de clave y botón Generate en PuTTYgen](./07_Transferencia_Ficheros_FTP_SSH/imagenes/45b_puttygen_interfaz_inicial.png)
*Figura 45b: Selección del tipo de clave RSA (2048 bits) y ubicación del botón Generate en PuTTYgen.*

4. En el campo **Key comment**, escribir: `alumne_redes@ies-mre`.
5. Pulsar en **Save private key** (confirmar guardar sin contraseña de paso para este laboratorio) y guardarla como `clave_privada_smx.ppk` en vuestra carpeta de trabajo.
6. En el cuadro superior que indica **Public key for pasting into OpenSSH authorized_keys file**, seleccionar y **copiar todo el texto completo de la clave pública** (`ssh-rsa AAAA...`):

![Generación del par de claves SSH en PuTTYgen](./07_Transferencia_Ficheros_FTP_SSH/imagenes/46_puttygen_clave_generada.png)
*Figura 46: Clave pública RSA generada en PuTTYgen con comentario identificativo alumne_redes@ies-mre y guardado de clave privada (.ppk).*

> 📷 **Evidencia 13 (insertar en tu documento Word) — Realizar captura de pantalla** de la ventana de PuTTYgen mostrando la clave generada y el comentario `alumne_redes@ies-mre`.

---

### 10.3 Instalación de la clave pública en Windows Server y ajuste de sshd_config

1. En el Escritorio Remoto (RDP) de **Windows Server**:
   * Abrir el **Bloc de notas (Notepad)** como Administrador.
   * Abrir el fichero `C:\ProgramData\ssh\sshd_config` (seleccionando **All Files `(**.**)`** en el diálogo de apertura).
   * Bajar hasta las dos últimas líneas del archivo (`Match Group administrators` y `AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys`) y comprobar que están comentadas con una almohadilla `#` delante para que Windows utilice siempre la carpeta `.ssh` estándar de cada usuario:
     ```ini
     #Match Group administrators
     #       AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
     ```
2. Crear la carpeta `C:\Users\alumne_redes\.ssh` (si no existe) y dentro de ella crear/abrir con **Notepad** el archivo **`authorized_keys`** (sin extensión `.txt`), pegando en una sola línea la clave pública copiada desde PuTTYgen:

![Clave pública copiada en authorized_keys mediante Notepad](./07_Transferencia_Ficheros_FTP_SSH/imagenes/46b_windows_authorized_keys_notepad.png)
*Figura 46b: Clave pública RSA pegada en una sola línea dentro del archivo authorized_keys de alumne_redes.*

3. Reiniciar el servicio **OpenSSH SSH Server** desde la consola gráfica `services.msc`:

![Reinicio del servicio OpenSSH SSH Server en services.msc](./07_Transferencia_Ficheros_FTP_SSH/imagenes/46c_services_reiniciar_openssh.png)
*Figura 46c: Reinicio del servicio OpenSSH SSH Server en Windows Server tras actualizar las claves autorizadas.*

---

### 10.4 Conexión automática mediante clave privada en PuTTY

1. Abrir **PuTTY** en vuestro PC del aula.
2. En el menú izquierdo, ir a **Connection** -> **Data** y en **Auto-login username** escribir `alumne_redes`:

![Configuración de Auto-login username en PuTTY](./07_Transferencia_Ficheros_FTP_SSH/imagenes/46d_putty_autologin.png)
*Figura 46d: Configuración del inicio de sesión desatendido para alumne_redes en Connection -> Data.*

3. En el árbol izquierdo, desplegar **Connection** -> **SSH** -> **Auth** -> **Credentials**:
   * En el campo **Private key file for authentication**, hacer clic en **Browse...** y seleccionar vuestro archivo `clave_privada_smx.ppk`:

![Carga de la clave privada .ppk en PuTTY Credentials](./07_Transferencia_Ficheros_FTP_SSH/imagenes/46e_putty_credentials.png)
*Figura 46e: Asociación del archivo de clave privada clave_privada_smx.ppk en Connection -> SSH -> Auth -> Credentials.*

4. Volver arriba a **Session**:
   * **Host Name:** IP pública de Windows Server (`<IP_PUBLICA_WINDOWS>`). **Port:** `22`.
   * En **Saved Sessions**, escribir `Windows-Clave-SSH` y hacer clic en **Save**:

![Guardado del perfil de sesión en PuTTY](./07_Transferencia_Ficheros_FTP_SSH/imagenes/46f_putty_guardar_sesion.png)
*Figura 46f: Perfil de sesión Windows-Clave-SSH guardado en PuTTY con IP pública, puerto 22 y clave asimétrica vinculada.*

5. Pulsar en **Open** y comprobar que la consola accede directamente a Windows Server **sin solicitar contraseña**:

![Acceso directo a la consola de Windows Server mediante clave privada](./07_Transferencia_Ficheros_FTP_SSH/imagenes/47a_putty_login_exitoso.png)
*Figura 47a: Sesión SSH abierta en el puerto 22 conectando de forma directa y autenticada con la clave privada de alumne_redes.*

---

### 10.5 Bastionado del servidor SSH en Windows Server (Deshabilitar contraseña)

1. En **Windows Server**, volver a abrir `C:\ProgramData\ssh\sshd_config` con **Notepad (como Administrador)**.
2. Añadir o asegurar al final del archivo la directiva de seguridad que prohíbe el acceso mediante contraseña convencional:
   ```ini
   PasswordAuthentication no
   ```

![Directiva PasswordAuthentication no añadida en sshd_config](./07_Transferencia_Ficheros_FTP_SSH/imagenes/47b_sshd_config_passwordauth_no.png)
*Figura 47b: Bastionado de OpenSSH mediante la directiva PasswordAuthentication no en sshd_config.*

3. Guardar los cambios (`Ctrl + S`) y reiniciar el servicio **OpenSSH SSH Server** en `services.msc`.
4. Abrir una nueva ventana limpia de **PuTTY** poniendo solo la IP de Windows Server (sin cargar la clave `.ppk`) e intentar entrar como `alumne_redes`: comprobar que el servidor rechaza inmediatamente el acceso mostrando el error de seguridad:
   ```text
   No supported authentication methods available (server sent: publickey,keyboard-interactive)
   ```

![Bloqueo de acceso por contraseña en PuTTY tras el bastionado](./07_Transferencia_Ficheros_FTP_SSH/imagenes/47c_putty_bloqueo_bastionado.png)
*Figura 47c: Rebuig d'accés en PuTTY (No supported authentication methods available) demostrant que el servidor només accepta claus públiques criptogràfiques.*

> 📷 **Evidencia 14 (insertar en tu documento Word) — Realizar captura de pantalla** de la sesión de PuTTY entrando automáticamente sin contraseña mediante clave privada (`Figura 47a`) y otra captura del bloqueo por bastionado (`Figura 47c`) al intentar acceder sin clave.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 10**
>
> En el **Apartado 10** de tu documento Word, incluye las **Evidencias 13 y 14**:
>
> * **Evidencia 13:** Generación del par de claves asimétricas en PuTTYgen con el comentario `alumne_redes@ies-mre`.
> * **Evidencia 14:** Sesión de PuTTY entrando automáticamente sin contraseña mediante clave pública y captura del rechazo (`No supported authentication methods available`) al intentar acceder sin clave privada.
>

---

## 11 - [Windows Server] Transferencia segura con SFTP/SCP y auditoría de Logs y Wireshark (RA3-CEe,f,g)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

Para completar todo el bloque práctico sobre **Windows Server (`Servidor_FTPSSH`)**, realizaremos transferencias seguras por el puerto `22` mediante **SFTP** y **SCP**, y auditaremos tanto los registros de actividad W3C de IIS como los paquetes de red capturados con **Wireshark**.

---

<a id="filtro-wireshark"></a>
### 11.1 Transferencia gráfica por SFTP hacia Windows Server en FileZilla (Puerto 22)

> ⚠️ **Comprobaciones de red si realizas este apartado en un día posterior**
>
> Si la instancia de Windows Server se ha reiniciado:
> * **FileZilla SFTP (11.1):** Actualiza el campo **Servidor** con la nueva IP pública de Windows Server.
> * **PowerShell SCP (11.2):** En el comando `scp`, sustituye `<IP_PUBLICA_WINDOWS>` por la IP pública actual ([Consultar IP en AWS](#60-lanzamiento-de-la-instancia-ec2-de-windows-server-2022-en-aws)).
> * **Filtro de Wireshark (11.4):** Si utilizas el filtro opcional por IP `(ftp || tls || ssh) && ip.addr == <IP_PUBLICA_WINDOWS>`, **debes poner la IP pública actual**. Si dejas la IP de una sesión anterior, Wireshark filtrará todo el tráfico y la captura aparecerá vacía.
>

1. Abrir **FileZilla Client**.
2. Dado que en el apartado anterior hemos bastionado el servidor SSH deshabilitando la autenticación por contraseña (`PasswordAuthentication no`), para conectar por SFTP debemos utilizar la clave privada generada con PuTTYgen (`clave_privada_smx.ppk`):
   * Ir al menú **Archivo** -> **Gestor de sitios...** (o pulsar `Ctrl + S`).
   * Crear un **Nuevo sitio** (por ejemplo, `Windows-SFTP`).
   * En **Protocolo**, seleccionar **SFTP - SSH File Transfer Protocol**.
   * En **Servidor**, escribir la IP pública de Windows Server (`54.198.204.170`) y en **Puerto** `22`.
   * En **Modo de acceso**, seleccionar **Archivo de claves** (**Key file**).
   * En **Usuario**, indicar `alumne_redes`.
   * En **Archivo de claves**, pulsar **Examinar...** y seleccionar vuestro archivo `clave_privada_smx.ppk`.

![Configuración del sitio SFTP con clave privada en el Gestor de sitios de FileZilla](./07_Transferencia_Ficheros_FTP_SSH/imagenes/34b_filezilla_sftp_gestor_sitios_clave.png)
*Figura 34b: Parámetros del sitio SFTP en FileZilla: protocolo SFTP (puerto 22), IP pública del servidor y autenticación mediante clave privada (.ppk).*

3. Pulsar en **Conectar**. Al ser la primera vez, aceptar la clave del servidor (**Hostkey is trusted**).
4. Comprobar que en el log superior se autentica con la clave y lista el directorio remoto `C:/Users/alumne_redes`.
5. Arrastrar un archivo local de prueba (por ejemplo, `Llista Regals.xlsx` o cualquier documento de texto) hacia la carpeta remota para realizar la subida cifrada.
6. Verificar que la transferencia se completa con éxito y que en la esquina inferior derecha aparece el **candado dorado cerrado**:

![FileZilla conectado mediante SFTP en el puerto 22 mostrando transferencia completada y el candado de cifrado](./07_Transferencia_Ficheros_FTP_SSH/imagenes/35_filezilla_sftp_conectado.png)
*Figura 35: Conexión SFTP activa en el puerto 22 hacia Windows Server con subida completada con éxito y candado de seguridad activo.*

> 📷 **Evidencia 15 (insertar en tu documento Word) — Realizar captura de pantalla** de FileZilla conectado por el protocolo SFTP al puerto 22 de Windows Server mostrando la transferencia completada y el icono del candado inferior.

---

### 11.2 Transferencia por línea de comandos mediante SCP hacia Windows Server

1. En vuestro ordenador del aula, abrir una ventana de **Windows PowerShell**.
2. Dado que el servidor tiene deshabilitada la contraseña tras el bastionado, `scp` utilizará automáticamente el par de claves asimétricas alojado en vuestro perfil (`~/.ssh/id_rsa` o indicando `-i .\clave_privada_smx.pem`).
3. Crear un archivo local de prueba y enviarlo hacia Windows Server mediante `scp`:
   ```powershell
   Set-Content -Path .\backup_aula.txt -Value "Copia de seguridad realizada mediante SCP - 2SMX"
   scp .\backup_aula.txt alumne_redes@<IP_PUBLICA_WINDOWS>:C:/Users/alumne_redes/
   ```
4. Comprobar en la consola la barra de progreso al `100%` y descargar el archivo de vuelta con un nuevo nombre (`fichero_recuperado.txt`) para verificar su integridad:
   ```powershell
   scp alumne_redes@<IP_PUBLICA_WINDOWS>:C:/Users/alumne_redes/backup_aula.txt .\fichero_recuperado.txt
   Get-Content .\fichero_recuperado.txt
   ```

![Transferencia de subida y descarga mediante SCP en Windows PowerShell](./07_Transferencia_Ficheros_FTP_SSH/imagenes/48_powershell_scp_transferencia.png)
*Figura 48: Subida y descarga segura de archivos hacia Windows Server por línea de comandos mediante SCP sobre el puerto 22 autenticando por clave.*

> 📷 **Evidencia 16 (insertar en tu documento Word) — Realizar captura de pantalla** de PowerShell ejecutando los comandos `scp` de subida y descarga mostrando la transferencia completada al `100%`.

---

### 11.3 Auditoría de registros de actividad en Windows Server (Logs W3C de IIS)

1. En Windows Server, abrir **File Explorer** y navegar a la ruta donde IIS almacena los registros de FTP:
   ```text
   C:\inetpub\logs\LogFiles\FTPSVC1\
   ```
2. Abrir el fichero de log más reciente (`u_exAAMMDD.log`, por ejemplo `u_ex261006.log`) con **Notepad**:

![Auditoría del fichero de registro u_ex261006.log de IIS FTP en Notepad](./07_Transferencia_Ficheros_FTP_SSH/imagenes/44_notepad_log_iis_ftp.png)
*Figura 44: Inspección en Notepad del fichero de registro W3C (u_ex261006.log) mostrando la autenticación (230), apertura de puertos pasivos (50000-50003), subida de archivo (STOR Prova_ftp.txt -> 226) y negociación FTPS (AUTH TLS -> 234 y PROT P -> 200).*

3. Identificar en el log los códigos de estado de vuestras operaciones:
   * `234`: Negociación de cifrado `AUTH TLS` aceptada.
   * `230`: Inicio de sesión correcto (`PASS ***`).
   * `227`: Entrada en Modo Pasivo (`PASV`).
   * `226`: Transferencia de archivo completada (`STOR Prova_ftp.txt`).
   * `550`: Permiso denegado (cuando el usuario `anonymous` intentó borrar el catálogo).

> 📷 **Evidencia 17 (insertar en tu documento Word) — Realizar captura de pantalla** del fichero de log de IIS en Notepad destacando una línea con un comando de subida exitoso (`STOR` con código `226`) y la negociación FTPS (`AUTH TLS` con código `234`).

---

### 11.4 Auditoría de tráfico con Wireshark: FTP en texto claro vs. FTPS y SFTP cifrados

Para comprobar empíricamente por qué nunca debe utilizarse FTP sin cifrar en redes públicas o corporativas, realizaremos una captura de paquetes con **Wireshark** desde el ordenador del aula mientras nos comunicamos con nuestro servidor Windows Server.

#### 11.4.1 Instalación y preparación previa de Wireshark
1. Si no disponéis de Wireshark en vuestro equipo del aula, descargar el instalador oficial de Windows (64-bit) desde [wireshark.org](https://www.wireshark.org/download.html).
2. Durante el asistente de instalación, es imprescindible mantener marcada la casilla de **Npcap** (controlador de captura de paquetes en modo promiscuo de Windows) con las opciones predeterminadas.

#### 11.4.2 Selección de la interfaz e inicio de la captura
1. Abrir **Wireshark**.
2. En la pantalla inicial de bienvenida (**Welcome to Wireshark**), identificar la tarjeta de red activa del equipo (la que muestra una línea con picos de actividad o tráfico):
   * En los ordenadores de sobremesa del aula suele ser **Ethernet**.
   * Si estáis trabajando con un ordenador portátil, seleccionar **Wi-Fi**.
3. Hacer doble clic sobre la interfaz activa o seleccionarla y pulsar el botón azul con forma de **aleta de tiburón** (esquina superior izquierda) para comenzar a capturar tráfico en tiempo real.
4. En la barra superior de filtro de visualización (**Apply a display filter ...**), escribir el siguiente filtro y pulsar `Enter` (la barra se pondrá en color verde claro si la sintaxis es correcta):
   ```text
   ftp || tls || ssh
   ```
   *(Opcional: Si queréis aislar exclusivamente el tráfico con vuestro servidor Windows en AWS, podéis usar: `(ftp || tls || ssh) && ip.addr == <IP_PUBLICA_WINDOWS>`)*.

![Inicio de captura y aplicación del filtro de visualización en Wireshark](./07_Transferencia_Ficheros_FTP_SSH/imagenes/44c_wireshark_filtro_interfaz.png)
*Figura 44c: Selección de la interfaz activa de red (Ethernet/Wi-Fi), inicio de captura con la aleta de tiburón y aplicación del filtro ftp || tls || ssh en Wireshark.*

#### 11.4.3 Procedimiento de generación de tráfico de prueba
Con la captura de Wireshark corriendo en segundo plano:
1. **Generar tráfico FTP plano (en texto claro):**
   * En FileZilla, conectar por FTP ordinario sin cifrado (`ftp://<IP_PUBLICA_WINDOWS>`, puerto `21`) con el usuario `alumne_redes` y su contraseña `Smx2026..@`.
2. **Generar tráfico FTPS (cifrado con TLS):**
   * Conectar con FileZilla requiriendo TLS explícito (**Requiere FTP explícito sobre TLS**).
3. **Generar tráfico SFTP (cifrado con SSH):**
   * Conectar con FileZilla por el puerto `22` (SFTP) o ejecutar un comando `scp` en PowerShell.
4. Volver a Wireshark y pulsar el botón **rojo cuadrado** (**Stop capturing packets**) en la barra de herramientas para detener la captura.

#### 11.4.4 Inspección y análisis comparativo de paquetes (Auditoría de seguridad)
Al examinar la lista de tramas filtradas comprobaremos la diferencia fundamental entre protocolos:

1. **FTP plano (Vulnerabilidad crítica):**
   * En las tramas de color rosa asociadas al protocolo FTP, buscar la petición de autenticación:
     * `Request: USER alumne_redes`
     * `Request: PASS Smx2026..@`
   * Al hacer clic sobre el paquete `PASS`, en el panel inferior de inspección de datos se comprueba que **la contraseña viaja en texto completamente plano y legible**, lo que permitiría a cualquier atacante en la red interceptarla (*sniffing* o ataque Man-In-The-Middle).
2. **FTPS sobre TLS (Cifrado de canal):**
   * Se aprecia la negociación inicial en el puerto 21 (`AUTH TLS -> 234 AUTH command ok`).
   * A partir de ese instante, todos los comandos y datos viajan cifrados bajo el protocolo **`TLSv1.2`** clasificados como **`Application Data`**.
3. **SFTP sobre SSH (Blindaje total):**
   * En el puerto `22`, toda la sesión queda encapsulada bajo **`SSHv2`** mostrando únicamente paquetes de tipo **`Encrypted packet`**. Ni las credenciales ni los nombres de los archivos transferidos son accesibles.

![Comparativa de paquetes en Wireshark entre FTP en texto claro y FTPS/SFTP cifrados](./07_Transferencia_Ficheros_FTP_SSH/imagenes/44b_wireshark_ftp_texto_claro_vs_cifrado.png)
*Figura 44b: Auditoría en Wireshark contrastando la exposición de credenciales en FTP plano (Request: PASS Smx2026..@) frente al tráfico cifrado en FTPS (TLSv1.2 Application Data) y SFTP (SSHv2 Encrypted packet).*

> 📷 **Evidencia 18 (insertar en tu documento Word) — Realizar captura de pantalla** de Wireshark mostrando los paquetes capturados donde se contrasten los paquetes en texto claro de FTP frente a los paquetes cifrados `TLSv1.2 Application Data` (FTPS) y `SSHv2 Encrypted packet` (SFTP).

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 11 (Fin del Bloque Windows Server)**
>
> En el **Apartado 11** de tu documento Word, incluye las **Evidencias 15 a 18**:
>
> * **Evidencia 15:** FileZilla conectado por SFTP (puerto `22`) a Windows Server con el candado activo.
> * **Evidencia 16:** Consola de PowerShell ejecutando la subida y descarga con `scp` al `100%`.
> * **Evidencia 17:** Fichero de log de IIS (`u_exAAMMDD.log`) en Notepad destacando las líneas `STOR` (`226`) y `AUTH TLS` (`234`).
> * **Evidencia 18:** Captura de paquetes en Wireshark comparando FTP plano frente a `TLSv1.2 Application Data` (FTPS) y `SSHv2 Encrypted packet` (SFTP).
>

---

## 12 - [Ubuntu Server] Instalación de vsftpd, modo pasivo, jaula chroot y pruebas en FileZilla (RA3-CEb,c,d,e)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

Una vez completadas y verificadas todas las prácticas sobre Windows Server, pasamos al segundo bloque del laboratorio desplegando el servicio de transferencia de ficheros en **Linux (`Ubuntu Server 24.04 LTS`)** mediante el demonio **`vsftpd`**. *(Mientras trabajes exclusivamente en esta tarea y en la Tarea 13, puedes mantener detenida la máquina de Windows Server para ahorrar saldo en AWS Academy).*

---

### 12.0 Lanzamiento de la instancia EC2 de Ubuntu Server 24.04 LTS en AWS

1. En la consola de **AWS EC2** -> **Instances** -> pulsar en **Launch instances** (**Lanzar instancias**) y desplegar la segunda máquina virtual del laboratorio con las siguientes especificaciones:

| Parámetro de configuración | Valor requerido |
|---|---|
| **Name (Nombre)** | `Ubuntu_FTPSSH` |
| **Application and OS Images (AMI)** | `Ubuntu Server 24.04 LTS (HVM), SSD Volume Type` (64 bits x86) |
| **Instance type (Tipo de instancia)** | `t3.micro` (Recomendado — 2 vCPU, 1 GiB RAM, **Apto para la capa gratuita**) o `t2.micro` |
| **Key pair (login)** | `vockey` (o par de claves del laboratorio) |
| **Network settings (Security group)** | Seleccionar **Select existing security group** y elegir **`grup-servidors-ftp-ssh`** (creado en el apartado 6.1) |
| **Configure storage** | `8 GiB` o `10 GiB` gp3 (SSD) |

> 💡 **En Ubuntu Server sí utilizamos la capa gratuita (t2.micro / t3.micro)**
>
> A diferencia de Windows Server, la máquina `Ubuntu_FTPSSH` funciona exclusivamente en modo terminal consola (CLI sin entorno de escritorio) y el demonio `vsftpd` es extremadamente ligero (consume menos de 150 MiB de RAM). Por tanto, aquí sí seleccionaremos el tipo **`t2.micro`** (o `t3.micro`), que cuenta con la etiqueta verde **Apto para la capa gratuita** (*Free tier eligible*), optimizando al máximo los créditos del laboratorio.
>

2. Esperar a que la instancia pase a estado `Running` y anotar su **Dirección IPv4 pública**:

![Instancia Ubuntu_FTPSSH en estado Running con IP pública asignada en AWS EC2](./07_Transferencia_Ficheros_FTP_SSH/imagenes/49_aws_ec2_ubuntu_instancia_running.png)
*Figura 49: Instancia Ubuntu_FTPSSH en estado En ejecución (Running) en el panel de instancias de AWS EC2 con su dirección IPv4 pública asignada.*

> 📷 **Evidencia 19 (insertar en tu documento Word) — Realizar captura de pantalla** del panel de instancias de AWS EC2 mostrando la instancia `Ubuntu_FTPSSH` en ejecución (`Running`) con el grupo de seguridad `grup-servidors-ftp-ssh` asignado.

---

### 12.1 Verificación de puertos en el Security Group de Ubuntu

1. En la consola de AWS -> **EC2** -> comprobar que el Security Group (`grup-servidors-ftp-ssh`) asociado a la instancia `Ubuntu_FTPSSH` tiene abiertos los puertos:
   * Puerto `22` TCP (SSH).
   * Puerto `21` TCP (FTP Control).
   * Rango de puertos `40000-40100` TCP (FTP Pasivo en Linux).

---

### 12.2 Instalación del servicio vsftpd

1. Conectarse a la instancia `Ubuntu_FTPSSH` por SSH utilizando AWS EC2 Instance Connect (o mediante cliente SSH / PuTTY con la clave del laboratorio):

![Conexión a la terminal de Ubuntu_FTPSSH mediante EC2 Instance Connect en el navegador](./07_Transferencia_Ficheros_FTP_SSH/imagenes/49b_ec2_instance_connect_ubuntu_terminal.png)
*Figura 49b: Sesión interactiva en la terminal de Ubuntu Server abierta directamente en el navegador con EC2 Instance Connect, mostrando el prompt `ubuntu@ip-...` y la barra inferior con la instancia e IP pública asignada.*

2. Actualizar el índice de repositorios e instalar el paquete `vsftpd`:
   ```bash
   sudo apt update && sudo apt install -y vsftpd
   ```

---

<a id="actualizar-ip-ubuntu"></a>
### 12.3 Configuración de modo pasivo, NAT y jaula chroot en /etc/vsftpd.conf

1. Abrir el fichero de configuración principal del servicio:
   ```bash
   sudo nano /etc/vsftpd.conf
   ```
2. Modificar las siguientes directivas para garantizar el funcionamiento en IPv4, habilitar la escritura, el enjaulado (`chroot`) y el rango pasivo en AWS:

   * **Al principio del fichero:** Comprobar que el servicio escucha en modo IPv4 independiente y comentar la directiva de IPv6:
     ```ini
     listen=YES
     #listen_ipv6=YES
     ```
     *(Importante: En Ubuntu 24.04, si `listen_ipv6=YES` está activo, entrará en conflicto con `pasv_address` y provocará desconexiones `ECONNABORTED` al intentar transferir archivos).*

   * **Al final del fichero:** Añadir el bloque de enjaulado, modo pasivo para AWS y compatibilidad de llamadas al sistema (`seccomp_sandbox`):
     ```ini
     # Acceso de usuarios locales con permisos de escritura
     anonymous_enable=NO
     local_enable=YES
     write_enable=YES
     local_umask=022

     # Enjaulado (chroot jail) de usuarios en su directorio /home/<usuario>
     chroot_local_user=YES
     allow_writeable_chroot=YES

     # Configuración de modo pasivo para AWS Cloud
     pasv_enable=YES
     pasv_min_port=40000
     pasv_max_port=40100
     pasv_address=<TU_IP_PUBLICA_UBUNTU>
     seccomp_sandbox=NO
     ```

![Configuración del modo pasivo y chroot en vsftpd.conf](./07_Transferencia_Ficheros_FTP_SSH/imagenes/50_ubuntu_vsftpd_conf.png)
*Figura 50: Configuración del fichero /etc/vsftpd.conf en nano mostrando las directivas de enjaulado chroot_local_user, modo pasivo pasv_enable, rango de puertos 40000-40100 y la dirección IP pública en pasv_address.*

> 📷 **Evidencia 20 (insertar en tu documento Word) — Realizar captura de pantalla** del fichero `/etc/vsftpd.conf` editado donde se aprecien las directivas `chroot_local_user=YES`, `pasv_enable=YES`, `pasv_address` y el rango `40000-40100`.

---

### 12.4 Creación de usuarios locales y activación del servicio

1. Crear los usuarios `alumne_redes` y `usuari_ventas` en Ubuntu Server:
   ```bash
   sudo adduser alumne_redes
   # Asignar la contraseña: Smx2026..@
   sudo adduser usuari_ventas
   # Asignar la contraseña: Smx2026..@
   ```
2. Reiniciar el servicio `vsftpd` y verificar que se encuentra activo (`active (running)`):
   ```bash
   sudo systemctl restart vsftpd
   sudo systemctl status vsftpd
   ```

![Verificación del estado activo del servicio vsftpd en Ubuntu Server](./07_Transferencia_Ficheros_FTP_SSH/imagenes/51_ubuntu_vsftpd_status.png)
*Figura 51: Terminal de Ubuntu Server mostrando la ejecución de systemctl status vsftpd con el estado active (running) y el proceso principal vsftpd en ejecución.*

> 📷 **Evidencia 21 (insertar en tu documento Word) — Realizar captura de pantalla** de la terminal de Ubuntu mostrando el estado `active (running)` del servicio `vsftpd`.

---

### 12.5 Prueba de transferencia y verificación de enjaulado (chroot) desde FileZilla

> ⚠️ **¿Retomas la conexión a Ubuntu en un día diferente o tras reiniciar?**
>
> Si la máquina virtual `Ubuntu_FTPSSH` se ha detenido y vuelto a iniciar:
> * **En FileZilla:** Introduce en el campo **Servidor** la **nueva IP pública de Ubuntu** (visible en la consola de AWS EC2).
> * **Problema crítico en `vsftpd` si no actualizas la IP:** Si el fichero `/etc/vsftpd.conf` conserva la IP de un día anterior en la directiva `pasv_address`, FileZilla conectará al puerto 21 pero se congelará indefinidamente en `150 Here comes the directory listing...` y fallará por *timeout*.
> * 👉 **Solución:** Abre la terminal de Ubuntu y actualiza la directiva con:
>   ```bash
>   sudo nano /etc/vsftpd.conf
>   # Modifica la línea: pasv_address=<NUEVA_IP_PUBLICA_UBUNTU>
>   sudo systemctl restart vsftpd
>   ```
>   Consulta los detalles completos en el [Apartado 12.3: Configuración de modo pasivo en vsftpd](#actualizar-ip-ubuntu).
>

1. Abrir **FileZilla Client** en vuestro PC del aula y conectar hacia **Ubuntu Server**:
   * **Servidor:** `<IP_PUBLICA_UBUNTU>`
   * **Nombre de usuario:** `alumne_redes` (y posteriormente probar con `usuari_ventas`)
   * **Contraseña:** `Smx2026..@`
   * **Puerto:** `21`
2. Subir un archivo llamado `prueba_ubuntu.txt` y comprobar que la transferencia en modo pasivo (`40000-40100`) se completa con éxito.
3. Verificar que gracias a la directiva `chroot_local_user=YES`, el usuario aparece enjaulado en `/` (que corresponde físicamente a su directorio personal `/home/alumne_redes`), impidiendo que pueda subir de nivel hacia `/home` o `/etc`.

![Transferencia de archivos y enjaulado chroot en Ubuntu Server desde FileZilla](./07_Transferencia_Ficheros_FTP_SSH/imagenes/52_filezilla_ubuntu_chroot_transfer.png)
*Figura 52: Cliente FileZilla conectado a Ubuntu Server mostrando el inicio de sesión exitoso, la transferencia completada de prueba_ubuntu.txt y el enjaulado chroot del usuario en su directorio raíz /.*

> 📷 **Evidencia 22 (insertar en tu documento Word) — Realizar captura de pantalla** de FileZilla conectado a Ubuntu Server mostrando la subida de `prueba_ubuntu.txt` y el enjaulado del usuario en su directorio raíz `/`.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 12**
>
> En el **Apartado 12** de tu documento Word, incluye las **Evidencias 19 a 22**:
>
> * **Evidencia 19:** Instancia `Ubuntu_FTPSSH` en ejecución (`Running`) en AWS EC2.
> * **Evidencia 20:** Fichero `/etc/vsftpd.conf` con las directivas `chroot_local_user=YES`, `pasv_enable=YES`, `pasv_address` y puertos `40000-40100`.
> * **Evidencia 21:** Salida de `sudo systemctl status vsftpd` mostrando `active (running)`.
> * **Evidencia 22:** FileZilla conectado a Ubuntu Server mostrando la subida de `prueba_ubuntu.txt` y el enjaulado del usuario en `/`.
>

---

## 13 - [Ubuntu Server] Seguridad FTPS con OpenSSL, claves SSH y auditoría de logs en Linux (RA3-CEf,g)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

En esta tarea aseguraremos nuestro servidor **Ubuntu Server (`Ubuntu_FTPSSH`)** implementando cifrado **FTPS con OpenSSL**, configurando el acceso **SSH por clave pública** y auditando los registros del sistema en `/var/log/`.

---

### 13.1 Configuración de FTPS (TLS/SSL) en Ubuntu Server con OpenSSL y vsftpd

> 💡 **¿Retomas este apartado en una sesión posterior?**
>
> * **Comprobación de IP:** Conéctate por SSH y FileZilla FTPS usando la nueva IP pública de Ubuntu Server.
> * **Verificación de vsftpd:** Asegúrate de que `pasv_address` en `/etc/vsftpd.conf` coincide con la IP pública actual de Ubuntu ([Apartado 12.3](#actualizar-ip-ubuntu)) y que el servicio está activo con `sudo systemctl status vsftpd`.
>

1. En la consola SSH de **`Ubuntu_FTPSSH`**, generar un certificado digital autofirmado X.509 RSA de `2048 bits` válido por 365 días en `/etc/ssl/private/vsftpd.pem`:
   ```bash
   sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout /etc/ssl/private/vsftpd.pem \
     -out /etc/ssl/private/vsftpd.pem
   ```
2. Cumplimentar los datos identificativos del certificado cuando los solicite OpenSSL:
   * **Country Name (2 letter code):** `ES`
   * **State or Province Name:** `Valencia`
   * **Locality Name:** `Catadau`
   * **Organization Name:** `IES Mestre Ramon Esteve`
   * **Organizational Unit Name:** `2SMX - Serveis en Xarxa`
   * **Common Name (FQDN):** `ftp.iesmre.local`
3. Restringir los permisos del archivo `.pem`:
   ```bash
   sudo chmod 600 /etc/ssl/private/vsftpd.pem
   ```
4. Editar `/etc/vsftpd.conf` (`sudo nano /etc/vsftpd.conf`) y añadir al final el bloque de cifrado SSL/TLS obligatorio:
   ```ini
   # Cifrado explicito FTPS (TLS/SSL) en vsftpd
   ssl_enable=YES
   allow_anon_ssl=NO
   force_local_data_ssl=YES
   force_local_logins_ssl=YES
   ssl_tlsv1=YES
   ssl_sslv2=NO
   ssl_sslv3=NO
   require_ssl_reuse=NO
   ssl_ciphers=HIGH
   rsa_cert_file=/etc/ssl/private/vsftpd.pem
   rsa_private_key_file=/etc/ssl/private/vsftpd.pem
   ```

![Ventana del certificado desconocido en FileZilla con los datos de IES Mestre Ramon Esteve](./07_Transferencia_Ficheros_FTP_SSH/imagenes/53_ubuntu_openssl_filezilla_ftps_cert.png)
*Figura 53: Ventana emergente de certificado X.509 en FileZilla al conectar por FTPS a Ubuntu Server, validando el cifrado TLS 1.3 con AES-256-GCM y los datos del IES Mestre Ramon Esteve (Catadau).*

> 📷 **Evidencia 23 (insertar en tu documento Word) — Realizar captura de pantalla** de la ventana de verificación del certificado X.509 en FileZilla mostrando los datos de la entidad (`IES Mestre Ramon Esteve`, `Catadau`, `ftp.iesmre.local`) y la sesión TLS 1.3 con Ubuntu Server.

---

### 13.2 Instalación de la clave pública SSH y bastionado en Ubuntu Server

1. En la sesión SSH de **Ubuntu Server** (conectado como `alumne_redes`), crear el directorio `.ssh` e instalar la misma clave pública que generamos en PuTTYgen en la Tarea 10:
   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   nano ~/.ssh/authorized_keys
   # Pegar la clave pública ssh-rsa ... en una sola línea, guardar (Ctrl+O) y salir (Ctrl+X)
   chmod 600 ~/.ssh/authorized_keys
   ```
2. Probar desde **PuTTY** en vuestro PC que podéis entrar a `Ubuntu_FTPSSH` con el usuario `alumne_redes` y el fichero `clave_privada_smx.ppk` sin que pida contraseña.
3. Bastionar el servidor SSH de Ubuntu editando `/etc/ssh/sshd_config`:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```
   Asegurar las directivas `PubkeyAuthentication yes` y `PasswordAuthentication no`, y reiniciar el servicio (`sudo systemctl restart ssh`).

---

### 13.3 Auditoría de registros en Ubuntu Server (vsftpd.log y auth.log)

1. En la consola SSH de Ubuntu Server, consultar las últimas transferencias registradas por `vsftpd` (descomentando `xferlog_enable=YES` en `/etc/vsftpd.conf` si no estuviera activo):
   ```bash
   sudo tail -n 25 /var/log/vsftpd.log
   ```
2. Consultar el registro de autenticaciones y accesos SSH del sistema:
   ```bash
   sudo cat /var/log/auth.log | grep -E "sshd.*(Accepted|Failed)" | tail -n 20
   ```
3. Identificar en la salida la dirección IP pública del cliente y el método de autenticación empleado (`publickey` o `password`).

![Auditoría de registros en Ubuntu Server en vsftpd.log y auth.log](./07_Transferencia_Ficheros_FTP_SSH/imagenes/54_ubuntu_auditoria_logs_vsftpd_auth.png)
*Figura 54: Auditoría de seguridad en Ubuntu Server mostrando el registro de subida exitosa en /var/log/vsftpd.log (OK UPLOAD de prueba_ubuntu.txt) y el registro de comandos privilegiados y accesos en /var/log/auth.log.*

> 📷 **Evidencia 24 (insertar en tu documento Word) — Realizar captura de pantalla** de la terminal de Ubuntu mostrando las últimas líneas del registro `/var/log/vsftpd.log` y de `/var/log/auth.log`.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 13 (Fin del Bloque Ubuntu Server)**
>
> En el **Apartado 13** de tu documento Word, incluye las **Evidencias 23 y 24**:
>
> * **Evidencia 23:** Generación del certificado X.509 con `openssl` en Ubuntu Server y validación del certificado en FileZilla al conectar por FTPS.
> * **Evidencia 24:** Terminal de Ubuntu mostrando las últimas líneas de auditoría en `/var/log/vsftpd.log` y `/var/log/auth.log`.
>

---

<a id="apartado-14"></a>
## 14 - [Inter-Servidores] Pruebas cruzadas bidireccionales en AWS Cloud (RA3-CEe,f)

> ⚠️ **¡ATENCIÓN CRÍTICA: Ambas máquinas pueden tener IPs nuevas si retomas hoy la práctica!**
>
> En este apartado de pruebas cruzadas es donde más errores ocurren si se realiza en un día diferente, ya que **tanto Windows Server como Ubuntu Server habrán cambiado de dirección IP pública**:
>
> **Lista de comprobaciones obligatorias antes de empezar:**
> 1. **Abre la consola de AWS EC2** y comprueba que ambas instancias (`Servidor_FTPSSH` y `Ubuntu_FTPSSH`) están en estado `Running`. Anota la **Dirección IPv4 pública actual** de cada una.
> 2. **En Windows Server:**
>    * Verifica que la directiva **FTP Firewall Support** de IIS tiene la IP actual de Windows ([Apartado 6.5](#actualizar-ip-windows)) y reinicia el servicio (`Restart-Service ftpsvc`).
>    * Comprueba que OpenSSH tiene temporalmente habilitada la autenticación por contraseña (`PasswordAuthentication yes`) como se indica en el paso previo del [Apartado 14.1](#141-conexion-ftp-y-ssh-desde-ubuntu-server-hacia-windows-server).
> 3. **En Ubuntu Server:**
>    * Verifica que `/etc/vsftpd.conf` tiene en `pasv_address` la IP pública actual de Ubuntu ([Apartado 12.3](#actualizar-ip-ubuntu)).
>    * Recuerda haber ejecutado el desbloqueo de contraseñas de SSH (`PasswordAuthentication yes`) indicado en el [Apartado 14.2](#142-conexion-ftp-y-ssh-desde-windows-server-hacia-ubuntu-server).
> 4. **Sustitución en los comandos:**
>    * En **14.1** (desde Ubuntu hacia Windows): Sustituye `<IP_PUBLICA_WINDOWS>` por la IP pública actual de Windows Server.
>    * En **14.2** (desde Windows hacia Ubuntu): Sustituye `<IP_PUBLICA_UBUNTU>` por la IP pública actual de Ubuntu Server.
>

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

En esta tarea comprobaremos la interoperabilidad bidireccional conectando los dos servidores entre sí a través de la nube de Amazon Web Services.

---

### 14.1 Conexión FTP y SSH desde Ubuntu Server hacia Windows Server

> ⚠️ **Comprobaciones previas en Windows Server antes de realizar las pruebas cruzadas**
>
> Para que las conexiones entrantes desde Linux hacia Windows Server funcionen correctamente, verifica en Windows Server los siguientes puntos técnicos:
>
> 1. **Autenticación por contraseña en OpenSSH:** En el Apartado 10 habíamos bastionado el servidor OpenSSH desactivando las contraseñas (`PasswordAuthentication no`). Para que podamos iniciar sesión desde Ubuntu mediante contraseña con `ssh alumne_redes@<IP_WINDOWS>`, abre PowerShell en Windows Server como Administrador y permite temporalmente las contraseñas:
>    ```powershell
>    (Get-Content C:\ProgramData\ssh\sshd_config) -replace 'PasswordAuthentication no', 'PasswordAuthentication yes' | Set-Content C:\ProgramData\ssh\sshd_config
>    Restart-Service sshd
>    ```
> 2. **Certificado FTPS activo en IIS:** En **IIS Manager** -> **Sitio FTP** (o `FTP-AULA`) -> **FTP SSL Settings**, comprueba que está seleccionado `Certificado-FTPs-Aula` con la directiva **Allow SSL connections** (o *Require*) y pulsa **Apply**. Si no estuviera seleccionado, el servidor devolverá el error `534 Local policy on server does not allow TLS secure connections`.
> 3. **IP pública en FTP Firewall Support:** Si has reiniciado la máquina y la IP pública de Windows ha cambiado, actualiza la dirección en **FTP Firewall Support** y reinicia el servicio (`Restart-Service ftpsvc`).
>

1. Desde la sesión SSH de **Ubuntu Server**, transferir un fichero al servidor Windows Server mediante `curl`:
   ```bash
   echo "Hola desde Linux hacia Windows Server en AWS" > saludo_linux.txt
   curl --ssl-reqd -k -T saludo_linux.txt -u alumne_redes:Smx2026..@ ftp://<IP_PUBLICA_WINDOWS>/
   ```
   *(Nota: incluimos `--ssl-reqd -k` dado que el servidor Windows exige cifrado explícito FTPS con certificado autofirmado).*
2. Desde la misma consola de Ubuntu Server, iniciar una sesión remota SSH hacia el servidor Windows y comprobar que el archivo se ha recibido en el directorio FTP del usuario:
   ```bash
   ssh alumne_redes@<IP_PUBLICA_WINDOWS>
   ```
   *Una vez dentro del prompt remoto de Windows Server (`alumne_redes@EC2AMAZ-...>`), listar el directorio raíz FTP del usuario:*
   ```cmd
   dir C:\inetpub\ftproot\LocalUser\alumne_redes
   exit
   ```
   *(Nota de verificación: Al ejecutar `dir` dentro de la sesión SSH, ya estáis gestionando e inspeccionando el sistema de archivos de Windows Server directamente desde la terminal remota. Opcionalmente, si tenéis el escritorio remoto (RDP) de Windows abierto, también podéis abrir el Explorador de archivos en `C:\inetpub\ftproot\LocalUser\alumne_redes` para verlo en la interfaz gráfica).*

![Transferencia FTPS con curl y conexión SSH desde Ubuntu hacia Windows Server](./07_Transferencia_Ficheros_FTP_SSH/imagenes/55_ubuntu_curl_ftps_ssh_windows.png)
*Figura 55: Transferencia cruzada desde Ubuntu Server hacia Windows Server mediante curl bajo FTPS explícito (saludo_linux.txt transferido al 100%) y apertura de sesión SSH interactiva en Windows Server verificando la recepción del archivo con dir.*

> 📷 **Evidencia 25 (insertar en tu documento Word) — Realizar captura de pantalla** de la consola de Ubuntu mostrando la subida del fichero por FTP/FTPS con `curl` y la apertura de sesión SSH en Windows validando la presencia del fichero con `dir`.

---

### 14.2 Conexión FTP y SSH desde Windows Server hacia Ubuntu Server

> ⚠️ **Desbloqueo obligatorio de autenticación por contraseña en Ubuntu Server (AWS EC2)**
>
> En las imágenes oficiales de Ubuntu en AWS EC2 (como Ubuntu 24.04 LTS), el aprovisionamiento en la nube (`cloud-init`) desactiva por defecto el inicio de sesión mediante contraseña mediante una plantilla prioritaria en `/etc/ssh/sshd_config.d/60-cloudimg-settings.conf` con el parámetro `PasswordAuthentication no`.
>
> Por este motivo, cuando intentéis conectaros desde Windows Server mediante `scp` o `ssh` con el usuario local `alumne_redes`, el cliente de Windows recibirá inmediatamente el error:
> ```text
> alumne_redes@<IP_UBUNTU>: Permission denied (publickey).
> C:\Windows\System32\OpenSSH\scp.exe: Connection closed
> ```
>
> **Solución obligatoria en Ubuntu Server (ejecutar en su terminal):**
> Para permitir que los usuarios locales se autentiquen con su contraseña (`Smx2026..@`), sobrescribid la directiva y reiniciad el demonio SSH:
> ```bash
> echo "PasswordAuthentication yes" | sudo tee /etc/ssh/sshd_config.d/60-cloudimg-settings.conf
> sudo systemctl restart ssh
> ```
> *(Comprobad que no muestra ningún error. A partir de este momento, el servidor Ubuntu aceptará contraseñas).*
>

**Procedimiento paso a paso desde Windows Server:**

1. Dentro de vuestro escritorio remoto (RDP) de **Windows Server**, abrid una ventana de **PowerShell** como Administrador.
2. Cread un archivo de texto de prueba para enviar al servidor Linux:
   ```powershell
   "Hola desde Windows Server hacia Linux" | Out-File -FilePath test_windows.txt -Encoding utf8
   ```
3. Transferid el archivo hacia la carpeta personal del usuario `alumne_redes` en Ubuntu Server mediante **SCP** (Secure Copy Protocol):
   ```powershell
   scp test_windows.txt alumne_redes@<IP_PUBLICA_UBUNTU>:~/
   ```
   *(La primera vez que os conectéis os preguntará si deseáis confiar en la huella ED25519 del host: escribid `yes` y pulsad Enter. A continuación, introducid la contraseña `Smx2026..@`).*
4. Abrid una sesión remota interactiva **SSH** desde Windows Server hacia Ubuntu Server para verificar que el archivo ha llegado y comprobar su contenido:
   ```powershell
   ssh alumne_redes@<IP_PUBLICA_UBUNTU>
   ```
   *Una vez dentro del prompt de Ubuntu (`alumne_redes@ip-...:~$`), listad el archivo y mostradlo en pantalla:*
   ```bash
   ls -la test_windows.txt
   cat test_windows.txt
   exit
   ```
   *(Alternativa opcional con `curl` por FTPS desde PowerShell: `curl.exe --ssl-reqd -k -T test_windows.txt -u alumne_redes:Smx2026..@ ftp://<IP_PUBLICA_UBUNTU>/`).*

![Conexión SCP y SSH interactiva desde Windows Server hacia Ubuntu Server](./07_Transferencia_Ficheros_FTP_SSH/imagenes/56_windows_scp_ssh_ubuntu.png)
*Figura 56: Consola de PowerShell en Windows Server mostrando la transferencia del archivo test_windows.txt mediante scp hacia Ubuntu Server y la sesión remota SSH posterior verificando el archivo con ls -la y cat.*

> 📷 **Evidencia 26 (insertar en tu documento Word) — Realizar captura de pantalla** de la consola de PowerShell en Windows Server mostrando el envío del archivo con `scp` hacia Ubuntu Server y la apertura de sesión interactiva `ssh` validando la presencia y contenido de `test_windows.txt`.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 14**
>
> En el **Apartado 14** de tu documento Word, incluye las **Evidencias 25 y 26**:
>
> * **Evidencia 25:** Consola de Ubuntu Server subiendo `saludo_linux.txt` por FTPS con `curl` y abriendo sesión SSH hacia Windows Server verificando el archivo con `dir`.
> * **Evidencia 26:** Consola de PowerShell en Windows Server transfiriendo `test_windows.txt` con `scp` y abriendo sesión interactiva `ssh` en Ubuntu Server comprobando el archivo con `ls -la`.
>

---

## 15 - Control de costes, parada de la infraestructura en AWS y entrega final (RA3-CEh)

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

Una vez completadas con éxito todas las pruebas técnicas en **Windows Server**, **Ubuntu Server** y las **pruebas cruzadas de interoperabilidad** entre ambos sistemas operativos, el paso imprescindible en cualquier despliegue profesional en la nube es aplicar las políticas de **control de costes y parada controlada de los recursos** para no consumir créditos innecesarios.

---

### 15.1 Cierre de sesiones y parada controlada de las instancias en AWS

> ⚠️ **¡Obligatorio al finalizar cada sesión de trabajo y al terminar la práctica!**
>
> Los laboratorios de AWS Academy disponen de un crédito limitado (\$50). Dejar las instancias encendidas consume saldo continuamente y puede provocar que os quedéis sin horas de laboratorio antes de que termine el curso.
>

1. **Desconexión de las sesiones activas:** Cerrar las ventanas de Escritorio Remoto (RDP), FileZilla, Wireshark y las sesiones de PuTTY o PowerShell abiertas en vuestro ordenador físico.
2. **Detener las instancias en AWS (`Stop instance`):**
   * Abrid la consola de AWS -> **EC2** -> **Instances** (**Instancias**).
   * Seleccionad las casillas de vuestras dos máquinas: **`Servidor_FTPSSH`** y **`Ubuntu_FTPSSH`**.
   * Haced clic en el desplegable superior **Instance state** -> **Stop instance** (**Detener la instancia**).
   * Esperad unos segundos y pulsad el botón de refrescar (⟳) hasta que en la columna **Instance state** aparezca claramente **`Stopped`** (**Detenido**) en ambas máquinas.

![Panel de instancias de AWS EC2 con ambas máquinas detenidas](./07_Transferencia_Ficheros_FTP_SSH/imagenes/57_aws_ec2_instances_stopped.png)
*Figura 57: Consola de AWS EC2 mostrando las dos instancias del laboratorio (Servidor_FTPSSH y Ubuntu_FTPSSH) en estado Stopped (Detenido) para garantizar el control de costes.*

> 📷 **Evidencia 27 (insertar en tu documento Word) — Realizar captura de pantalla** del panel de instancias de EC2 mostrando ambas máquinas (`Servidor_FTPSSH` y `Ubuntu_FTPSSH`) seleccionadas y en estado `Stopped` (**Detenido**).

3. **Cerrar el laboratorio:** Volved a la pestaña de **AWS Academy** (Vocareum) y pulsad en el botón rojo superior **`End Lab`**.

https://sri.codeandcoke.com/doku.php?id=sri:t3

https://acastan.gitbook.io/servicios/ficheros

https://despliegue.codeandcoke.com/apuntes:servicios_transferencia

https://marcosruiz.github.io/posts/servicio-vsfptd/

https://docs.google.com/presentation/d/16LLGSFIHKK79dWvvZw0lVgjssmxKZAD3wJG7qlZxbcw/edit?slide=id.g1142a802_1_0#slide=id.g1142a802_1_0
