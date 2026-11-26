

### 4.3 Instalación de los servicios

<!-- NUEVO: criterio de evaluación b) -->

#### 4.3.1 Servidor FTP de IIS (Windows Server)

1. Instalar el rol desde *Administrador del servidor → Agregar roles y características → Servidor web (IIS) → Servidor FTP*. Desde PowerShell (como administrador):
    ```powershell
    Install-WindowsFeature Web-Server, Web-Ftp-Server, Web-Mgmt-Console
    ```
1. Crear el sitio en el Administrador de IIS (`inetmgr`): *Sitios → Agregar sitio FTP...* y definir el nombre, la ruta física (`C:\inetpub\ftproot`), el enlace (IP y puerto 21), el certificado SSL, la autenticación y la autorización.
1. Abrir el puerto de control y el rango pasivo en el Firewall de Windows:
    ```powershell
    New-NetFirewallRule -DisplayName "FTP control 21" -Direction Inbound -Protocol TCP -LocalPort 21 -Action Allow
    New-NetFirewallRule -DisplayName "FTP pasivo 50000-50100" -Direction Inbound -Protocol TCP -LocalPort 50000-50100 -Action Allow
    ```
1. Fijar el rango de puertos pasivos y la IP externa en *Compatibilidad con firewall FTP* (a nivel de servidor y de sitio) y reiniciar el servicio:
    ```powershell
    Restart-Service ftpsvc
    ```

#### 4.3.2 vsftpd (Linux, Debian/Ubuntu)

```bash
sudo apt update
sudo apt install vsftpd
sudo systemctl enable --now vsftpd
sudo systemctl status vsftpd
sudo ufw allow 21/tcp
sudo ufw allow 50000:50100/tcp
```

Después de cada cambio en `/etc/vsftpd.conf` hay que reiniciar el servicio con `sudo systemctl restart vsftpd`. Una configuración mínima de partida:

```ini
# Acceso
listen=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022

# Enjaulado
chroot_local_user=YES

# Modo pasivo
pasv_enable=YES
pasv_min_port=50000
pasv_max_port=50100
# pasv_address=<IP pública>   (necesaria en AWS)

# Registro
xferlog_enable=YES
vsftpd_log_file=/var/log/vsftpd.log
```

Para activar **FTPS explícito** hay que generar un certificado y añadir estas directivas:

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/vsftpd.key -out /etc/ssl/certs/vsftpd.pem
```

```ini
ssl_enable=YES
rsa_cert_file=/etc/ssl/certs/vsftpd.pem
rsa_private_key_file=/etc/ssl/private/vsftpd.key
force_local_logins_ssl=YES
force_local_data_ssl=YES
ssl_tlsv1_2=YES
ssl_tlsv1=NO
ssl_sslv2=NO
ssl_sslv3=NO
```

!!! tip "Error típico con FileZilla"
    Si FileZilla muestra `522 SSL connection failed; session reuse required`, añade `require_ssl_reuse=NO` y reinicia vsftpd.

#### 4.3.3 OpenSSH Server

**En Windows (10/11 y Server 2019 o superior):**

```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
Get-NetFirewallRule -Name *ssh*
```

La instalación crea automáticamente la regla de firewall `OpenSSH-Server-In-TCP` para el puerto 22. Se comprueba con la última orden.

**En Linux (Debian/Ubuntu):**

```bash
sudo apt install openssh-server
sudo systemctl enable --now ssh
sudo ufw allow 22/tcp
```

!!! note "Nombre del servicio"
    En Debian y Ubuntu el servicio se llama `ssh`. En Red Hat y derivadas se llama `sshd`.

En ambos casos, SFTP funciona sin instalar nada más, porque va incluido como subsistema (`Subsystem sftp ...` en `sshd_config`).

### 4.4 Uso práctico de los clientes

<!-- NUEVO: criterios de evaluación f) y g) -->

#### 4.4.1 Cliente `ftp` de consola

```text
C:\> ftp 203.0.113.10
Conectado a 203.0.113.10.
220 Microsoft FTP Service
Usuario: usuari_ventas
331 Password required
Contraseña:
230 User logged in.
ftp> binary
ftp> ls
ftp> cd documentos
ftp> get manual.pdf
ftp> put informe.docx
ftp> bye
```

| Comando | Función |
|---|---|
| `open servidor` | Abre la conexión con un servidor |
| `ls` / `dir` | Lista el directorio remoto |
| `cd` / `lcd` | Cambia de directorio en el servidor / en el equipo local |
| `pwd` | Muestra el directorio remoto actual |
| `get` / `mget` | Descarga un fichero / varios ficheros |
| `put` / `mput` | Sube un fichero / varios ficheros |
| `delete`, `mkdir`, `rmdir` | Gestionan ficheros y carpetas remotas |
| `binary` / `ascii` | Cambia el modo de transferencia |
| `passive` | Activa o desactiva el modo pasivo (cliente `ftp` de Linux) |
| `prompt` | Evita que `mget`/`mput` pregunten por cada fichero |
| `debug` | Muestra los comandos reales que se envían al servidor |
| `quote <comando>` | Envía un comando FTP "en crudo" (por ejemplo, `quote SYST`) |
| `bye` / `quit` | Cierra la sesión |

!!! warning "Limitaciones del `ftp.exe` de Windows"
    El cliente `ftp` incluido en Windows **no soporta FTPS ni SFTP**, y **no soporta modo pasivo**. Para probar FTPS o el modo pasivo hay que usar FileZilla, `curl` o `lftp`.

#### 4.4.2 SFTP, SCP y SSH

```bash
sftp usuario@203.0.113.10             # sesión interactiva
sftp -P 2222 usuario@203.0.113.10     # puerto distinto del 22 (P mayúscula)
sftp -i ~/.ssh/id_ed25519 usuario@203.0.113.10   # con clave privada
```

Dentro de la sesión `sftp`: `ls`, `lls` (listado local), `cd`, `lcd`, `pwd`, `lpwd`, `get fichero`, `get -r carpeta`, `put fichero`, `mkdir`, `rm`, `chmod`, `bye`.

```bash
scp informe.pdf usuario@203.0.113.10:/home/usuario/       # subir
scp usuario@203.0.113.10:/var/log/auth.log .              # descargar
scp -r carpeta/ usuario@203.0.113.10:/srv/datos/          # carpeta completa
```

**Generar y copiar un par de claves:**

```bash
ssh-keygen -t ed25519 -C "alumno@aula"      # crea ~/.ssh/id_ed25519 y .pub
ssh-copy-id usuario@203.0.113.10             # instala la clave pública (Linux/macOS)
```

En un **servidor Windows** no existe `ssh-copy-id`. La clave pública se copia a mano en `C:\Users\<usuario>\.ssh\authorized_keys` o, si el usuario es administrador, en `C:\ProgramData\ssh\administrators_authorized_keys`, y hay que ajustar los permisos de este último:

```powershell
icacls.exe "$env:ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"
```

#### 4.4.3 `curl` y `lftp`

```bash
# Descarga por FTP
curl -u usuari_ventas ftp://203.0.113.10/manual.pdf -O

# FTPS explícito (certificado autofirmado: -k lo acepta)
curl --ssl-reqd -k -u usuari_ventas ftp://203.0.113.10/manual.pdf -O

# Subida por SFTP
curl -u usuario -T informe.pdf sftp://203.0.113.10/home/usuario/

# lftp con FTPS explícito y modo pasivo desactivado (modo activo)
lftp -u usuari_ventas ftp://203.0.113.10
lftp :~> set ftp:ssl-force true
lftp :~> set ssl:verify-certificate no
lftp :~> set ftp:passive-mode off
```

#### 4.4.4 FileZilla (cliente gráfico)

1. *Archivo → Gestor de sitios → Nuevo sitio*.
1. Elegir el **Protocolo** (FTP, SFTP) y escribir el servidor, el puerto y el usuario. Para FTPS, en **Cifrado** se elige *Requerir FTP explícito sobre TLS*.
1. En **Tipo de acceso** se puede elegir *Normal*, *Anónimo* o *Pedir contraseña*. Para SFTP con clave, *Archivo de clave*.
1. En la pestaña **Configuración de transferencia** se fija el **modo de transferencia**: *Por defecto*, *Activo* o *Pasivo*, y el número máximo de conexiones simultáneas.
1. Al conectar, el **panel de mensajes** superior muestra los comandos enviados y los códigos de respuesta (`Comando:`, `Respuesta:`). Es la mejor herramienta de depuración.

#### 4.4.5 Comprobar el modo activo y el modo pasivo

Para cumplir el criterio de evaluación f), hay que **demostrar** que se ha probado cada modo y qué ocurre en cada uno.

| Prueba | Modo pasivo | Modo activo |
|---|---|---|
| **FileZilla** (*Configuración de transferencia*) | `Pasivo` | `Activo` |
| **`ftp` en Linux** | `passive` (si indica `Passive mode on`) | `passive` (si indica `Passive mode off`) |
| **`curl`** | Opción por defecto (usa `EPSV`/`PASV`) | `--ftp-port -` |
| **`lftp`** | `set ftp:passive-mode on` | `set ftp:passive-mode off` |

**Cómo saber qué modo se está usando**

- **En el panel de mensajes de FileZilla**: en pasivo aparece `Comando: PASV` y `Respuesta: 227 Entering Passive Mode (...)`. En activo aparece `Comando: PORT ...`.
- **En Wireshark**: el filtro `ftp.request.command == "PASV" || ftp.request.command == "PORT"` muestra qué orden se envió. Con `tcp.port == 20` se ven las conexiones de datos del modo activo, y con `tcp.port >= 50000 && tcp.port <= 50100` las del modo pasivo.

**Resultados esperables**

- **Pasivo sin rango abierto en el firewall:** el login funciona, pero el listado se queda colgado y termina con error `425` o con *timeout*.
- **Pasivo con IP privada en AWS:** el servidor anuncia una IP no alcanzable y se produce *timeout* (apartado 2.6).
- **Activo desde un equipo detrás de NAT:** el servidor no puede conectar con el cliente y el listado falla.
- **Activo en la misma red local sin firewall:** funciona.

#### 4.4.6 Errores típicos y cómo diagnosticarlos

| Síntoma | Causa más probable | Qué comprobar |
|---|---|---|
| `530 Login incorrect` / `530 User cannot log in` | Usuario o contraseña erróneos, anónimo deshabilitado o usuario no autorizado | Credenciales, regla de autorización del sitio, `userlist_enable` en vsftpd |
| `550 Access is denied` / `Permission denied` | Falta de permisos NTFS o de Linux sobre la carpeta | Permisos de la carpeta y regla de autorización de IIS |
| `425 Can't open data connection` | Cortafuegos o NAT bloquea el canal de datos | Rango pasivo, `pasv_address`, reglas del firewall y del Security Group |
| `421 Too many connections` o `421 Timeout` | Se alcanzó el límite de conexiones o expiró por inactividad | Apartado 5.5 (límites) |
| `500 OOPS: vsftpd: refusing to run with writable root inside chroot()` | La raíz del enjaulado tiene permisos de escritura | Apartado 5.4.1 |
| `534 Policy requires SSL` / fallo de TLS | El servidor exige FTPS y el cliente usa FTP plano | Cifrado del sitio en el cliente |
| El listado de directorios se queda colgado | Fallo en el canal de datos (modo pasivo mal configurado) | Apartado 2.6 y 4.4.5 |
| `REMOTE HOST IDENTIFICATION HAS CHANGED` | La clave del servidor SSH ha cambiado | Apartado 3.6.1 |
| `Permission denied (publickey)` | La clave pública no está bien instalada o sus permisos son incorrectos | `authorized_keys`, permisos (`chmod 600`) y `ssh -v` |
| `Connection timed out` en el puerto 22 | Puerto cerrado o servicio parado | Security Group, firewall, `Get-Service sshd` o `systemctl status ssh` |

## 5 - Gestión de usuarios, aislamiento, bastionado y auditoría

### 5.1 Tipologías de usuarios en un servidor de ficheros (Anónimos, Locales y Virtuales)

Un aspecto clave en la administración de un servicio de transferencia de ficheros es determinar cómo se identifican los usuarios y qué alcance de permisos reciben:

1. **Acceso anónimo (`anonymous` o `ftp`):**
    - **Propósito:** Permitir que cualquier usuario de Internet descargue recursos públicos (manuales, documentación, parches, distribuciones de software) sin necesidad de contar con una cuenta previa en el sistema.
    - **Credenciales:** Se utiliza convencionalmente el identificador `anonymous` y, como contraseña, cualquier cadena de texto (tradicionalmente la dirección de correo del visitante).
    - **Regla de seguridad vital:** Los usuarios anónimos deben configurarse con **permisos estrictos de solo lectura (`Read-only`)**. Otorgar permisos de escritura o borrado a usuarios anónimos constituye una negligencia crítica, ya que permitiría a actores maliciosos utilizar el almacenamiento del servidor para alojar contenido ilegal, herramientas de ataque o malware.

2. **Usuarios locales del sistema operativo:**
    - **Propósito:** Empleados o usuarios autorizados que disponen de una cuenta de usuario creada en la base de datos de seguridad local del sistema operativo anfitrión (la base de datos SAM en Windows Server o los ficheros `/etc/passwd` y `/etc/shadow` en Linux).
    - **Riesgo:** Si un atacante compromete la contraseña de un usuario local a través de FTP sin cifrar, podría llegar a reutilizar dichas credenciales para acceder a otros servicios locales del servidor (como RDP o SSH).

3. **Usuarios virtuales:**
    - **Propósito:** Cuentas de usuario que existen únicamente en la configuración interna del servicio FTP o en una base de datos externa (MySQL, MariaDB, ficheros Berkeley DB), sin correspondencia directa con cuentas de inicio de sesión del sistema operativo.
    - **Beneficio:** Todas las cuentas virtuales se mapean a un único usuario del sistema sin privilegios de ejecución (como el usuario `nobody` o `ftp`), logrando el máximo grado de aislamiento y seguridad frente a posibles brechas de acceso.

### 5.2 Creación de usuarios y grupos

<!-- NUEVO: criterio de evaluación c) -->

Para no asignar permisos usuario por usuario, se crea un **grupo** (por ejemplo, `ftpusuarios`), se mete en él a las cuentas autorizadas y se asignan los permisos al grupo.

#### 5.2.1 En Windows Server (IIS)

```powershell
New-LocalGroup -Name "FTPUsuarios" -Description "Usuarios del servicio FTP"
$pass = Read-Host -AsSecureString "Contraseña"
New-LocalUser -Name "usuari_ventas" -Password $pass -PasswordNeverExpires
Add-LocalGroupMember -Group "FTPUsuarios" -Member "usuari_ventas"
```

En IIS, un usuario necesita **dos permisos** para poder operar. El acceso efectivo es **la intersección** de ambos, es decir, el más restrictivo:

| Capa | Dónde se configura | Qué controla |
|---|---|---|
| **Reglas de autorización FTP** | Sitio FTP → *Reglas de autorización FTP* | Quién puede entrar al sitio (usuarios, grupos o todos) y con qué permiso: *Lectura* y/o *Escritura* |
| **Permisos NTFS** | Propiedades de la carpeta → *Seguridad* | Qué puede hacer la cuenta en el sistema de ficheros: lectura, modificación, etc. |

!!! example "Ejemplo"
    Se crea la regla *Permitir → grupo FTPUsuarios → Lectura y Escritura*, pero la carpeta solo concede a ese grupo permiso NTFS de *Lectura*. El usuario podrá descargar, pero al subir recibirá `550 Access is denied`.

También se puede restringir el acceso por origen con *Restricciones de direcciones IP y dominios de FTP* (permitir o denegar IP o rangos).

#### 5.2.2 En Linux (vsftpd)

```bash
sudo groupadd ftpusuarios
sudo useradd -m -s /usr/sbin/nologin -G ftpusuarios usuari_ventas
sudo passwd usuari_ventas
echo "/usr/sbin/nologin" | sudo tee -a /etc/shells
```

!!! note "¿Por qué `/etc/shells`?"
    Para que el usuario pueda entrar **solo por FTP** y no por consola, se le asigna un shell sin acceso (`nologin`). Pero el módulo PAM de vsftpd rechaza las cuentas con shells que no estén en `/etc/shells`, por lo que hay que añadirlo.

vsftpd ofrece dos listas de control complementarias:

| Directiva | Fichero | Función |
|---|---|---|
| `userlist_enable=YES` + `userlist_file=/etc/vsftpd.userlist` + `userlist_deny=NO` | Lista de usuarios | **Lista blanca:** solo pueden entrar los usuarios escritos en el fichero (uno por línea). Con `userlist_deny=YES` es una lista negra |
| `chroot_local_user=NO` + `chroot_list_enable=YES` + `chroot_list_file=/etc/vsftpd.chroot_list` | Lista de excepciones del enjaulado | Enjaula **solo** a los usuarios de la lista (o a todos menos a ellos, según `chroot_local_user`) |
| `/etc/ftpusers` | Lista del sistema | Usuarios que **nunca** pueden entrar por FTP (por defecto `root` y otras cuentas de sistema) |

#### 5.2.3 En OpenSSH

El acceso se limita con directivas de `sshd_config`:

```text
AllowGroups sftpusers      # solo los miembros de este grupo pueden entrar por SSH
DenyUsers  invitado        # lista negra de usuarios
```

### 5.3 Configuración del acceso anónimo

<!-- NUEVO: criterio de evaluación d) -->

El acceso anónimo está **desactivado por defecto** en la mayoría de servidores. Si se activa, debe ser de **solo lectura** (apartado 5.1).

#### 5.3.1 En IIS

1. En el sitio FTP, abrir *Autenticación de FTP* y **habilitar** *Autenticación anónima*.
1. En *Reglas de autorización FTP*, añadir una regla: *Permitir acceso → Usuarios anónimos → **solo Lectura***.
1. En la carpeta física, la identidad anónima (por defecto `IUSR`) necesita **solo permiso NTFS de lectura**.
1. Si el sitio usa aislamiento de usuarios por directorio (apartado 5.4.2), los anónimos aterrizan en `LocalUser\Public`.

#### 5.3.2 En vsftpd

```ini
anonymous_enable=YES            # activa el acceso anónimo
anon_root=/srv/ftp              # carpeta a la que accede el anónimo
no_anon_password=YES            # no pedir contraseña (opcional)
anon_upload_enable=NO           # NO permitir subir ficheros
anon_mkdir_write_enable=NO      # NO permitir crear carpetas
anon_other_write_enable=NO      # NO permitir borrar ni renombrar
anon_max_rate=51200             # límite de 50 KB/s (ver apartado 5.5)
```

!!! warning "Permisos de la carpeta"
    La carpeta `anon_root` **no debe ser escribible** por el usuario `ftp`. Un anónimo que pueda escribir en ella podría subir contenido ilegal aunque `anon_upload_enable` esté en `NO` si otra directiva se cambia por error.

**Comprobación:** al conectar con usuario `anonymous`, el servidor debe responder `230 Login successful`, y cualquier intento de `put` debe devolver `550 Permission denied`.

### 5.4 Mecanismos de enjaulado y aislamiento de usuarios (chroot y LocalUser)

<!-- CORREGIDO: numeración (antes 4.2) y la solución recomendada para el error del chroot escribible -->

- Por defecto, si un servidor FTP autentica a un usuario local sin medidas de confinamiento, el usuario aterrizará en su carpeta personal pero tendrá la capacidad técnica de emitir órdenes `cd ..` y navegar libremente hacia directorios raíz del sistema (como `C:\Windows\System32` o `/etc`), pudiendo consultar ficheros confidenciales del sistema operativo.

- Para impedirlo, se aplica el mecanismo de **enjaulado** (*chroot jail* / *User Isolation*):

#### 5.4.1 Enjaulado en Linux con `vsftpd` (`chroot`)

1. **La directiva `chroot_local_user=YES`** instruye a `vsftpd` a realizar una llamada de sistema `chroot()`, convirtiendo el directorio asignado al usuario en su nueva raíz lógica del sistema de ficheros (`/`). Cualquier intento de subir a un nivel superior es bloqueado por el propio kernel.
1. **El error del chroot escribible:** Por seguridad, `vsftpd` se niega a enjaular a un usuario si su directorio raíz tiene permisos de escritura, para evitar una vulnerabilidad conocida de elevación de privilegios. En ese caso aborta con:  
    `500 OOPS: vsftpd: refusing to run with writable root inside chroot()`
1. **Solución recomendada:** la raíz de la jaula **no es escribible** y se crea dentro una subcarpeta donde sí puede escribir:
    ```bash
    sudo chown root:root /home/usuari_ventas
    sudo chmod a-w /home/usuari_ventas
    sudo mkdir /home/usuari_ventas/ficheros
    sudo chown usuari_ventas:usuari_ventas /home/usuari_ventas/ficheros
    ```
1. **Atajo para entornos de laboratorio:** la directiva `allow_writeable_chroot=YES` desactiva la comprobación y permite que la raíz sea escribible. Es rápida, pero **debilita la seguridad**, así que no se recomienda en producción.

#### 5.4.2 Aislamiento de usuarios en Windows Server (IIS `LocalUser`)

1. En el Administrador de IIS, la característica **Aislamiento de usuarios FTP** (*FTP User Isolation*) se configura seleccionando la opción **Directorio de nombre de usuario**.
1. El servidor exige crear una estructura de carpetas estricta bajo la raíz del sitio FTP denominada `LocalUser`:
    - `C:\inetpub\ftproot\LocalUser\<nombre_de_usuario>`: Cada usuario local autenticado es confinado automáticamente a su carpeta homónima. Desde su cliente FTP, esa carpeta aparecerá como la raíz `/`, sin permitirle ver ni acceder a las carpetas de otros compañeros ni al resto del disco duro.
    - `C:\inetpub\ftproot\LocalUser\Public`: Carpeta compartida a la que son dirigidos los usuarios anónimos o no aislados.

#### 5.4.3 Enjaulado en SFTP con OpenSSH

<!-- NUEVO -->

OpenSSH permite confinar a un grupo de usuarios para que **solo puedan usar SFTP**, sin consola y sin salir de su carpeta:

```text
# /etc/ssh/sshd_config
Subsystem sftp internal-sftp

Match Group sftpusers
    ChrootDirectory /srv/sftp/%u
    ForceCommand internal-sftp
    AllowTcpForwarding no
    X11Forwarding no
```

- `Match Group`: aplica las directivas siguientes solo a los miembros del grupo.
- `ChrootDirectory`: define la nueva raíz del usuario (`%u` se sustituye por su nombre).
- `ForceCommand internal-sftp`: obliga a usar solo SFTP e impide abrir una consola.

!!! warning "Requisito de permisos"
    El directorio indicado en `ChrootDirectory` y todos sus padres deben pertenecer a **root** y **no ser escribibles** por el grupo ni por otros. El usuario escribe en una **subcarpeta** propia, igual que en vsftpd. Si no se cumple, la conexión se cierra con el error `bad ownership or modes for chroot directory`.

OpenSSH para Windows también admite `ChrootDirectory` con `internal-sftp`.

### 5.5 Límites de conexiones, tiempos y velocidad

<!-- NUEVO: criterio de evaluación e) -->

Un servidor sin límites es vulnerable a la saturación, ya sea por un ataque o por un uso abusivo. Los límites se establecen para **cada modo de acceso**: anónimos, usuarios locales y conexiones desde una IP.

| Qué se limita | vsftpd | IIS FTP | OpenSSH |
|---|---|---|---|
| **Conexiones simultáneas totales** | `max_clients=50` | Sitio → *Configuración avanzada* → *Conexiones* → **Máximo de conexiones** | `MaxStartups 10:30:60` (conexiones sin autenticar) |
| **Conexiones por dirección IP** | `max_per_ip=3` | No dispone. Se puede restringir por IP con *Restricciones de direcciones IP y dominios de FTP* | Cortafuegos (`ufw limit`, `fail2ban`) |
| **Tiempo de inactividad del control** | `idle_session_timeout=300` | *Tiempo de espera del canal de control* (segundos) | `ClientAliveInterval` / `ClientAliveCountMax` (ver 5.6.2) |
| **Tiempo de inactividad del canal de datos** | `data_connection_timeout=300` | *Tiempo de espera del canal de datos* | No aplica |
| **Velocidad (usuarios locales)** | `local_max_rate=1048576` (bytes/s) | No dispone de forma nativa (se puede aplicar *QoS basada en directivas* de Windows) | No dispone de forma nativa |
| **Velocidad (anónimos)** | `anon_max_rate=51200` (bytes/s) | No dispone | No aplica |
| **Número de sesiones por conexión SSH** | No aplica | No aplica | `MaxSessions 5` |
| **Rango de puertos pasivos** | `pasv_min_port` / `pasv_max_port` | *Data Channel Port Range* | No aplica |
| **Espacio en disco** | Cuotas del sistema (`quota`) | Cuotas de NTFS o de FSRM | Cuotas del sistema |

Cuando un cliente supera el máximo de conexiones, el servidor responde `421 Too many connections` y cierra la conexión de control.

Además, IIS incluye el panel **Sesiones actuales de FTP** (*FTP Current Sessions*), donde se ve quién está conectado, desde qué IP y qué está transfiriendo, y desde donde se puede **desconectar** a un usuario.

!!! info "El rango pasivo también es un límite"
    Cada transferencia simultánea en modo pasivo consume un puerto del rango. Un rango de 100 puertos limita en la práctica a unas 100 transferencias a la vez.

### 5.6 Administración remota segura con SSH y bastionado (Hardening)

<!-- CORREGIDO: numeración (antes 4.3) y varias directivas mal explicadas -->

- La administración de servidores en entornos modernos exige canales cifrados y robustos frente a accesos no autorizados.
- El protocolo **SSH (Secure Shell)** sobre el **puerto 22 TCP** reemplazó a protocolos vulnerables antiguos como Telnet y Rlogin.

#### 5.6.1 Autenticación por parejas de claves asimétricas

La autenticación tradicional por usuario y contraseña es susceptible a ataques de fuerza bruta mediante diccionarios automatizados. La mejor práctica de seguridad consiste en emplear **criptografía de clave pública**:

1. **Clave Privada (*Private Key*):**  
    - Permanece **exclusivamente en el dispositivo cliente** del administrador.
    - Debe protegerse mediante una frase de paso (*passphrase*) que la cifra en disco.
    - **Bajo ninguna circunstancia debe enviarse por la red ni entregarse a terceros**.

1. **Clave Pública (*Public Key*):**  
    - Puede distribuirse libremente sin comprometer la seguridad.
    - Se almacena en el servidor remoto en el fichero:
        - En Linux: `~/.ssh/authorized_keys` del usuario correspondiente.
        - En Windows Server: `C:\ProgramData\ssh\administrators_authorized_keys` (para miembros del grupo Administradores) o `C:\Users\<usuario>\.ssh\authorized_keys`.

1. **Algoritmos recomendados:**
    - **RSA:** Mínimo de 2048 o 4096 bits.
    - **Ed25519:** Algoritmo moderno basado en curvas elípticas (EdDSA), con claves mucho más compactas, mayor velocidad de cálculo y resistencia criptográfica superior frente a ataques.

#### 5.6.2 Bastionado (*Hardening*) del servicio OpenSSH

Para proteger un servidor expuesto a Internet en la nube frente a intrusiones automatizadas, se aplican las siguientes directivas en su fichero de configuración (`/etc/ssh/sshd_config` o `C:\ProgramData\ssh\sshd_config`):

```text
PasswordAuthentication no
PermitRootLogin no
MaxAuthTries 3
LoginGraceTime 30
ClientAliveInterval 300
ClientAliveCountMax 2
AllowGroups sftpusers sshadmins
```

1. **Desactivación de autenticación por contraseña (`PasswordAuthentication no`):**  
   Fuerza que cualquier conexión deba autenticarse obligatoriamente mediante una clave asimétrica válida. Si un atacante lanza un ataque de fuerza bruta con millones de contraseñas de diccionario, no podrá acertar ninguna, porque el servidor no acepta contraseñas.
1. **Desactivación del acceso directo de superusuario (`PermitRootLogin no`):**  
   Impide que se intente iniciar sesión directamente como `root` en Linux. Se debe ingresar con un usuario estándar y posteriormente elevar privilegios mediante `sudo`. En **Windows** esta directiva no aplica a la cuenta `Administrator`, porque OpenSSH usa las cuentas de Windows. Para bloquearla se usa `DenyUsers Administrator` o, mejor, `AllowGroups` con los grupos autorizados.
1. **Limitación de intentos de autenticación (`MaxAuthTries 3`):**  
   Cierra la **conexión** tras tres intentos erróneos. Ojo: un atacante puede volver a conectar y empezar de nuevo, por lo que esta directiva **no frena por sí sola los escaneos masivos**. Para bloquear la IP que falla repetidamente se usa una herramienta como **`fail2ban`**, que lee `/var/log/auth.log` y añade reglas al cortafuegos.
1. **Detección de clientes caídos (`ClientAliveInterval 300` y `ClientAliveCountMax 2`):**  
   El servidor envía un mensaje de comprobación cada 300 segundos y, si el cliente no responde dos veces seguidas, cierra la sesión. Sirve para **liberar sesiones de clientes que han desaparecido** (corte de red, equipo apagado). **No cierra a un usuario conectado que simplemente esté inactivo**, porque su cliente sigue respondiendo. Para cerrar sesiones inactivas en Linux se define la variable de shell `TMOUT=300` (por ejemplo, en `/etc/profile.d/timeout.sh`).
1. **Restricción de usuarios (`AllowGroups`):**  
   Solo los miembros de los grupos indicados pueden iniciar sesión. Es el mecanismo más fiable para reducir la superficie de ataque.

!!! danger "Antes de desactivar las contraseñas"
    **Comprueba que el acceso por clave funciona antes de poner `PasswordAuthentication no`**, y hazlo **abriendo una segunda sesión sin cerrar la primera**. Si activas el cambio con la clave mal instalada, te quedarás **sin acceso al servidor**, y en la nube (AWS) recuperarlo es largo y complicado. Después de editar `sshd_config`, valida la sintaxis con `sudo sshd -t` y reinicia el servicio.

### 5.7 Auditoría, análisis forense y monitorización de registros (Logs y Wireshark)

<!-- CORREGIDO: numeración (antes 4.4), descripción de c-ip y de lo que muestra Wireshark; NUEVO: registros de OpenSSH y vsftpd -->

La observabilidad y el registro de eventos son requisitos indispensables para garantizar la trazabilidad de accesos, detectar intrusiones y cumplir con normativas de ciberseguridad como el **Esquema Nacional de Seguridad (ENS)** y el **RGPD**:

#### 5.7.1 Registros en formato W3C en Microsoft IIS

El servicio FTP de IIS almacena sus accesos en ficheros de texto estructurados conforme al estándar **W3C Extended Log Format** (ubicados por defecto en `C:\inetpub\logs\LogFiles\FTPSVC1\`):

```text
#Fields: date time c-ip cs-username s-ip s-port cs-method cs-uri-stem sc-status sc-win32-status
2026-10-21 10:15:32 198.51.100.25 usuari_ventas 172.31.25.100 21 USER usuari_ventas 331 0
2026-10-21 10:15:32 198.51.100.25 usuari_ventas 172.31.25.100 21 PASS *** 230 0
2026-10-21 10:16:05 198.51.100.25 usuari_ventas 172.31.25.100 21 RETR /manual.pdf 226 0
2026-10-21 10:17:12 198.51.100.25 anonymous 172.31.25.100 21 STOR /subir.exe 550 5
```

- `date`: Fecha en la que se registra el evento (formato `AAAA-MM-DD`, en hora UTC por defecto en el formato W3C).
- `time`: Hora exacta del evento (formato `HH:MM:SS`). Junto con `date` permite reconstruir la cronología de una intrusión o un fallo.
- `c-ip`: Dirección IP del cliente que realiza la conexión (la IP origen que ve el servidor, pública o privada según la red).
- `cs-username`: Nombre del usuario que intenta la operación.
- `s-ip`: Dirección IP del servidor que atiende la conexión (útil cuando el servidor tiene varias interfaces o sitios FTP).
- `s-port`: Puerto TCP del servidor al que se conecta el cliente (`21` para el canal de control FTP/FTPES).
- `cs-method`: Comando FTP ejecutado (`USER`, `PASS`, `LIST`, `RETR`, `STOR`, `DELE`).
- `cs-uri-stem`: Ruta y nombre del fichero afectado en el servidor.
- `sc-status`: Código de estado numérico devuelto por el servidor (ej. `331` para usuario aceptado a la espera de contraseña, `230` para éxito de login, `226` para transferencia completada, `550` para acceso denegado).
- `sc-win32-status`: Código de error de Windows asociado a la operación. El valor `0` indica que no hubo error; otros valores indican la causa a nivel de sistema operativo (por ejemplo, `5` equivale a "Acceso denegado", `2` a "Archivo no encontrado").

**Prefijos de los campos:** `c-` = cliente, `s-` = servidor, `cs-` = del cliente al servidor (petición) y `sc-` = del servidor al cliente (respuesta).

**Lectura del ejemplo:**

1. Las dos primeras líneas muestran el inicio de sesión de `usuari_ventas`: el servidor acepta el usuario (`331`) y la contraseña (`230`). IIS enmascara la contraseña con `***`.
1. La tercera línea muestra una descarga correcta de `/manual.pdf` (`226`, error Win32 `0`).
1. La cuarta línea es un evento sospechoso: el usuario `anonymous` intenta subir `/subir.exe` y el servidor lo deniega (`550`, error Win32 `5` = acceso denegado). Conviene revisar la IP de origen y valorar si se deshabilita el acceso anónimo.

#### 5.7.2 Registros en servidores Linux

- `/var/log/vsftpd.log`: Registra cada conexión entrante, inicios de sesión y operaciones de subida y descarga con indicación exacta de bytes transferidos. Con `log_ftp_protocol=YES` (y `xferlog_std_format=NO`) registra además **todos los comandos FTP** del cliente y las respuestas, lo cual es muy útil para depurar.
- `/var/log/auth.log` (o `/var/log/secure`): Registra todos los intentos de autenticación en el servidor (accesos aceptados por clave pública `Accepted publickey`, intentos fallidos por contraseña `Failed password for invalid user`, y elevaciones mediante `sudo`).
- `journalctl -u ssh` (o `-u sshd` en Red Hat): Muestra los registros del servicio SSH a través de `systemd`.

#### 5.7.3 Registros de OpenSSH

<!-- NUEVO -->

- **En Windows:** *Visor de eventos → Registros de aplicaciones y servicios → OpenSSH → Operational*. Se registran los inicios de sesión correctos y fallidos del servicio `sshd`. También con PowerShell:
    ```powershell
    Get-WinEvent -LogName "OpenSSH/Operational" -MaxEvents 20
    ```
- **En Linux:** por defecto solo se registran las autenticaciones. Para ver **qué ficheros transfiere cada usuario por SFTP** hay que subir el nivel de detalle:
    ```text
    # /etc/ssh/sshd_config
    LogLevel VERBOSE
    Subsystem sftp internal-sftp -l VERBOSE
    ```

#### 5.7.4 Inspección de paquetes de red con Wireshark

Mediante el uso de analizadores de tráfico en el aula o laboratorio, es posible visualizar la diferencia palpable entre la opacidad del tráfico cifrado y la vulnerabilidad del tráfico plano:

- **En FTP estándar (Puerto 21):** Los paquetes TCP revelan claramente las cabeceras `USER` y `PASS` con las contraseñas legibles en texto ASCII, así como los datos transferidos. Con el filtro `ftp` o `ftp-data`, y la opción *Seguir flujo TCP*, se lee toda la conversación.
- **En FTPS (TLS):** El comando `AUTH TLS` y la respuesta `234` **sí se ven en claro**, porque se envían antes del *handshake*. A partir de ahí, los paquetes aparecen etiquetados como *Application Data* de TLS, con *payloads* aleatorios ininteligibles. El filtro útil es `tls`.
- **En SFTP (SSH):** tras el intercambio inicial de versiones y claves, Wireshark muestra los paquetes como *Encrypted packet*, sin posibilidad de ver ni el usuario ni los ficheros. El filtro útil es `ssh`.

### 5.8 Buenas prácticas y control de costes en laboratorios Cloud

Al operar infraestructuras en entornos de nube pública (**AWS Academy / AWS Learner Lab**), el rol del administrador de sistemas incluye la gestión rigurosa de los recursos:

1. **Principio de mínimo privilegio:** Desactivar el acceso directo de cuentas con privilegios de superusuario (`Administrator` o `root`) al servicio FTP.
1. **Defensa en profundidad en cortafuegos:** Limitar la apertura de puertos pasivos en los grupos de seguridad estrictamente al rango acotado necesario para las transferencias del aula. Abrir solo los puertos necesarios: 21 y el rango pasivo para FTP/FTPS, y 22 para SFTP/SSH.
1. **Control y optimización de costes en AWS:** Las instancias virtuales EC2 consumen saldo del laboratorio mientras permanecen en estado `Running`. Al finalizar la sesión lectiva o el trabajo en casa, es **obligatorio detener las instancias (`Stop instance`)** desde la consola web de AWS. Detener la instancia congela el consumo de cómputo preservando íntegros los datos del disco SSD (EBS).
1. **Efecto de detener la instancia sobre la IP:** Al detener y volver a iniciar una instancia, **su IP pública cambia** si no tiene una Elastic IP asociada. Hay que recordar entonces actualizar `pasv_address` o el campo *External IP Address of Firewall* de IIS, y la IP que se usa en el cliente. De lo contrario, el login funcionará pero las transferencias de datos fallarán por *timeout*.

## 6 - Tarea RA3-CEb-1 - Instalación y configuración de IIS FTP y OpenSSH

<!-- NUEVO: introducción de la tarea. El enunciado y los pasos de la práctica están pendientes de redactar. -->

En esta tarea se aborda la puesta en marcha de dos servicios de transferencia de ficheros sobre un servidor Windows, con enfoques y niveles de seguridad distintos. Por un lado, se instalará y configurará el **servicio FTP de Microsoft IIS**, que permite publicar un sitio FTP con control de usuarios, permisos de acceso, aislamiento de directorios y cifrado opcional mediante **FTPS** (TLS/SSL con certificado X.509). Por otro lado, se desplegará **OpenSSH Server**, que ofrece **SFTP** a través de un único puerto (TCP 22) y admite autenticación por contraseña o por claves asimétricas.

El objetivo es comparar en la práctica ambas alternativas, tomando como referencia lo visto en el análisis teórico de los protocolos (FTP, FTPS, SFTP y SCP): comprobar cómo se instalan y configuran, qué reglas de **firewall** requiere cada una y qué diferencias existen en cuanto a seguridad y facilidad de administración. Además, se verificará su funcionamiento con clientes como **FileZilla** o la consola `sftp`, y se revisarán los **registros de acceso** generados (como los logs W3C de IIS) para auditar conexiones correctas y accesos denegados.

Al finalizar la tarea, se habrá obtenido un entorno funcional con ambos servicios operativos y se dispondrá de criterios técnicos para decidir cuál es más adecuado según el escenario: FTPS cuando se necesita compatibilidad con infraestructura FTP existente, y SFTP como opción recomendada para entornos actuales por su simplicidad y robustez.

!!! info "Apartados de la unidad que se aplican en esta tarea"
    | Fase de la tarea | Apartado de consulta |
    |---|---|
    | Instalación de IIS FTP y OpenSSH | 4.3.1 y 4.3.3 |
    | Usuarios, grupos y permisos | 5.2.1 y 5.2.3 |
    | Acceso anónimo | 5.3.1 |
    | Aislamiento de usuarios | 5.4.2 y 5.4.3 |
    | Límites de conexión | 5.5 |
    | Modo activo y pasivo, firewall e IP externa | 2.5, 2.6 y 4.4.5 |
    | FTPS y certificado | 3.2 y 3.6.2 |
    | Claves SSH | 4.4.2 y 5.6.1 |
    | Pruebas con clientes | 4.4 |
    | Revisión de logs | 5.7 |

## 7 - Cierre de la unidad

<!-- NUEVO: resumen, glosario, cuestionario y bibliografía -->

### 7.1 Resumen de la unidad

- **FTP** (RFC 959) usa **dos conexiones TCP**: control (puerto 21) y datos (puerto 20 en activo o puerto efímero en pasivo). Todo viaja **sin cifrar**.
- En **modo activo** el servidor abre la conexión de datos hacia el cliente (suele ser bloqueada por NAT y cortafuegos). En **modo pasivo** es el cliente quien abre ambas conexiones, y es el modo habitual en Internet.
- En servidores detrás de NAT o en la nube hay que configurar **la IP pública, un rango acotado de puertos pasivos y todos los cortafuegos**.
- **FTPS** añade TLS a FTP (explícito con `AUTH TLS` por el puerto 21, implícito en desuso por el 990). **SFTP** es otro protocolo sobre **SSH** y usa solo el puerto 22. **SCP** está desaconsejado como protocolo.
- La administración de un servidor incluye **usuarios y grupos**, **acceso anónimo** (solo lectura), **enjaulado**, **límites**, **bastionado de SSH** y **auditoría de logs**.
- Los clientes deben **verificar la identidad del servidor** (huella SSH o certificado) para evitar ataques de intermediario.

### 7.2 Glosario

| Término | Definición |
|---|---|
| **ALG** (*Application Layer Gateway*) | Función de un router o cortafuegos que inspecciona un protocolo (por ejemplo, FTP) y modifica los paquetes para que funcione con NAT |
| **NAT / PAT** | Traducción de direcciones (y puertos) privadas a públicas |
| **Canal de control / de datos** | Las dos conexiones de FTP: órdenes y respuestas, frente a ficheros y listados |
| **Modo activo / pasivo** | Quién abre la conexión de datos: el servidor (activo) o el cliente (pasivo) |
| **TLS** | Protocolo de cifrado que sustituye a SSL. Es la base de HTTPS y FTPS |
| **Certificado X.509** | Documento digital que une una clave pública con una identidad y está firmado por una autoridad de certificación |
| **CA** (*Certificate Authority*) | Entidad de confianza que firma certificados |
| **Handshake** | Negociación inicial en la que cliente y servidor acuerdan algoritmos y claves |
| **chroot / enjaulado** | Mecanismo que restringe a un usuario a un directorio, que pasa a ser su raíz |
| **Clave pública / privada** | Pareja de claves asimétricas: la pública se reparte y la privada nunca sale del cliente |
| **Huella (*fingerprint*)** | Resumen corto de una clave, que sirve para comprobar que es la esperada |
| **Hardening / bastionado** | Conjunto de ajustes para reducir la superficie de ataque de un servicio |
| **Elastic IP** | Dirección IP pública fija de AWS que no cambia al reiniciar la instancia |
| **Security Group** | Cortafuegos virtual de AWS asociado a una instancia (*stateful*) |

### 7.3 Cuestionario de repaso

1. ¿Por qué FTP usa dos conexiones TCP y qué ventaja aporta separarlas?
1. Un servidor responde `227 Entering Passive Mode (203,0,113,10,195,100)`. ¿A qué IP y a qué puerto debe conectar el cliente?
1. ¿Por qué el modo activo suele fallar cuando el cliente está detrás de un NAT?
1. Un usuario consigue iniciar sesión pero el listado de directorios se queda colgado. Indica dos posibles causas.
1. ¿Qué diferencia hay entre FTPS explícito e implícito? ¿Cuál se considera obsoleto?
1. ¿Es SFTP "FTP con cifrado"? Razona la respuesta.
1. ¿Por qué se desaconseja el protocolo SCP original? ¿Qué hace OpenSSH 9.0 con el comando `scp`?
1. ¿Qué error de vsftpd aparece si la raíz del enjaulado es escribible y cuál es la solución recomendada?
1. En IIS, un usuario tiene permiso de *Escritura* en la regla de autorización pero solo *Lectura* en NTFS. ¿Qué ocurre al subir un fichero?
1. ¿Por qué hay que comprobar el acceso por clave antes de poner `PasswordAuthentication no`?
1. ¿Qué pasa con la configuración pasiva de un servidor en AWS al detener y volver a arrancar la instancia si no tiene Elastic IP?
1. ¿Qué te indica en un log de IIS la línea `STOR /subir.exe 550 5` de un usuario `anonymous`?

??? success "Respuestas (versión del profesor)"
    1. Porque el canal de control permanece abierto para órdenes mientras el de datos se abre solo para transferir. Así el cliente puede enviar órdenes como `ABOR` durante una transferencia larga.
    1. A la IP **203.0.113.10** y al puerto 195 × 256 + 100 = **50020**.
    1. Porque el servidor intenta abrir una conexión entrante hacia una IP privada (la que va en `PORT`) y el cortafuegos o NAT del cliente la descarta como tráfico no solicitado.
    1. El servidor anuncia su IP privada en la respuesta `227`; el rango de puertos pasivos no está abierto en el firewall o el Security Group; no se ha configurado la IP externa; o se está usando modo activo detrás de NAT.
    1. En el explícito se conecta al puerto 21 y se pide el cifrado con `AUTH TLS`. En el implícito se usa un puerto dedicado (990) y el TLS empieza nada más conectar. El **implícito** es el obsoleto.
    1. No. Es un protocolo distinto que funciona como subsistema de SSH, con un solo puerto (22) y autenticación de SSH. Tampoco es FTP tunelizado.
    1. Porque en el protocolo antiguo el servidor decide qué ficheros envía y el cliente no puede verificarlo del todo, así que un servidor malicioso podía sobrescribir ficheros. Desde OpenSSH 9.0 el comando `scp` usa SFTP internamente.
    1. `500 OOPS: vsftpd: refusing to run with writable root inside chroot()`. Se soluciona quitando la escritura a la raíz (`chmod a-w`) y creando una subcarpeta escribible. El atajo es `allow_writeable_chroot=YES`.
    1. El acceso es la intersección de ambos permisos: el usuario podrá leer, pero al subir recibirá `550 Access is denied`.
    1. Porque si la clave no funciona, nadie podrá entrar al servidor al estar las contraseñas desactivadas.
    1. La IP pública cambia, por lo que `pasv_address` o *External IP Address of Firewall* dejan de ser correctos. El login funciona, pero las transferencias fallan por *timeout*.
    1. Un intento de subir un ejecutable por parte de un usuario anónimo, denegado (`550`, error Win32 `5`). Es un evento sospechoso: hay que revisar la IP de origen y valorar deshabilitar el acceso anónimo.

### 7.4 Bibliografía y referencias

- **RFC 959** - File Transfer Protocol (1985).
- **RFC 2228** - FTP Security Extensions.
- **RFC 2428** - FTP Extensions for IPv6 and NATs.
- **RFC 3659** - Extensions to FTP.
- **RFC 4217** - Securing FTP with TLS.
- **RFC 1350** - The TFTP Protocol (Revision 2).
- **RFC 4251 a 4254** - Arquitectura, autenticación, transporte y conexión del protocolo SSH.
- Documentación de **vsftpd**: `man vsftpd.conf`.
- Documentación de **OpenSSH**: `man sshd_config` y [openssh.com](https://www.openssh.com).
- Microsoft Learn: documentación del **servidor FTP de IIS** y de **OpenSSH en Windows**.
- Documentación de **FileZilla**: [wiki.filezilla-project.org](https://wiki.filezilla-project.org).
