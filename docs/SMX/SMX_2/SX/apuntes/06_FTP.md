---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Servicios en red
module number: 0227
lesson: UD. 6.0 - Servicio de transferencia de archivos
author: Javier Egea Blasco  
layout: default  
year: 26-27  
keywords: SMX, SMR, SX, SR
schedule: 233h - 7h/w
---

![Descripción de la imagen](./img_6/img_6_1.png){ .img2 .marginbottom40}

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:**|
||
| **RA3. Gestiona servicios de transferencia de ficheros describiendo sus características e instalando los servidores y clientes correspondientes.**|

|**Criterios de evaluación de la unidad didáctica:**|
||
|**a) Se ha establecido la utilidad y modo de operación del servicio de transferencia de ficheros.**|
|**b)** Se ha instalado un servicio de transferencia de ficheros. |
|**c)** Se han creado usuarios y grupos para acceso remoto al servidor.|
|**d)** Se ha configurado el acceso anónimo.|
|**e)** Se han establecido límites en los distintos modos de acceso.|
|**f)** Se ha comprobado el acceso al servidor, tanto en modo activo como en modo pasivo.|
|**g)** Se han realizado pruebas con clientes en línea de comandos y en modo gráfico.|

!!! warning "Nota:"
    Los criterios de evaluación en negrita será evaluados durante la FCT.

## 1 - Presentación y evolución de los servicios de transferencia de ficheros

- La transferencia de archivos a través de redes informáticas constituye uno de los **servicios cliente-servidor** más antiguos y esenciales de la arquitectura TCP/IP.
- Antes del desarrollo de la World Wide Web (www) y del protocolo HTTP(S), la necesidad primordial de los centros de cálculo universitarios y militares era compartir programas ejecutables, conjuntos de datos masivos y documentos entre ordenadores distantes y con **sistemas operativos heterogéneos**.

### 1.1 Evolución histórica: Del RFC 114 al RFC 959

- El protocolo **FTP (File Transfer Protocol)** nació formalmente el 16 de abril de 1971 con la publicación del **RFC 114** por Abhay Bhushan en el MIT, operando sobre las primeras redes de conmutación de paquetes de ARPANET y la pila NCP (*Network Control Program*).
- Con la transición definitiva a la arquitectura de Internet basada en TCP/IP en 1980, el protocolo se rediseñó en el **RFC 765** y finalmente se consolidó en octubre de 1985 con la publicación del **RFC 959**, que continúa siendo el estándar fundacional vigente hoy en día.
- A lo largo de las décadas, FTP ha evolucionado mediante diversas ampliaciones (*RFC extensions*), destacando:
   1. **RFC 2228 (FTP Security Extensions):** Introduce mecanismos de autenticación y cifrado mediante comandos como `AUTH TLS`.
   1. **RFC 2428 (FTP Extensions for IPv6 and NATs):** Define los comandos `EPRT` (*Extended Port*) y `EPSV` (*Extended Passive*) para dar soporte al direccionamiento IPv6 y facilitar la interoperabilidad con pasarelas NAT complejas.
   1. **RFC 3659 (Extensions to FTP):** Añade comandos modernos como `MLST` y `MLSD` para obtener listados de ficheros con metadatos estandarizados e información horaria en UTC.

### 1.2 FTP y modelo TCP/IP

![img](./img_6/img-6-3.png){.sietecinco .margintop10 marginbottom20 .marco}

- FTP se sitúa en la **Capa de Aplicación** (capa 4 de TCP/IP).
- Para el transporte de la información, se apoya de forma estricta en el protocolo **TCP (Transmission Control Protocol)** en la capa de transporte.
- La elección de TCP (frente a protocolos no orientados a conexión como UDP) es indispensable por tres factores determinantes:  
    1. **Fiabilidad absoluta:** Cada paquete de datos debe ser confirmado mediante ACKs para asegurar que ni un solo byte del fichero transferido se pierda o llegue corrupto.
    1. **Entrega secuencial y ordenada:** Garantiza que los segmentos fragmentados en la red se reensamblen en el destino en el orden exacto.
    1. **Control de flujo y congestión:** Regula la velocidad de transmisión adaptándose a la capacidad del receptor y a las condiciones de congestión de los enlaces de red.

### 1.3 Modelo cliente-servidor y arquitectura de servicios

![img](./img_6/img-6-5.jpeg){.sietecinco .margintop10 marginbottom20 .marco}

- FTP sigue el paradigma **cliente-servidor**:  
  - El **servidor FTP** es un proceso que permanece a la escucha de peticiones en el puerto TCP 21, esperando que los clientes se conecten y soliciten transferencias de ficheros o listados de directorios.
  - El **cliente FTP** es un programa que se ejecuta en la máquina del usuario final, capaz de establecer la conexión con el servidor, enviar órdenes y recibir datos.

### 1.3 Casos de uso corporativos en la administración de sistemas

A pesar del auge de protocolos web (HTTP/HTTPS) y APIs REST, los servicios de transferencia de ficheros basados en FTP, FTPS y SFTP siguen siendo pilares en las infraestructuras de IT:

1. **Despliegue y mantenimiento de portales web:** Carga de contenidos HTML, scripts PHP, hojas de estilo CSS y elementos multimedia en servidores web de alojamiento (*hosting* compartido o dedicado).
1. **Gestión de dispositivos de red y telecomunicaciones:** Actualización masiva de firmwares e imágenes de sistemas operativos (Cisco IOS, JunOS), y volcado de configuraciones en *switches*, *routers* y cortafuegos.
1. **Copias de seguridad remotas (*backups*):** Automatización nocturna del envío de volcados de bases de datos (SQL) y ficheros de archivo comprimidos hacia servidores de almacenamiento remoto (*off-site*).
1. **Intercambio B2B (*Business-to-Business*):** Intercambio automático de albaranes, facturas electrónicas (EDI) y ficheros de transacciones bancarias entre sistemas centrales de diferentes organizaciones.

## 2 - Protocolo FTP (RFC 959)

### 2.1 Canal de control y Canal de datos

La gran particularidad de FTP frente a casi todos los demás protocolos de red (HTTP, SSH o SMTP) radica en que **no utiliza una única conexión para todo**, sino que desacopla la comunicación en **dos conexiones TCP independientes con ciclos de vida y propósitos completamente distintos**:

![img](./img_6/img-6-2.jpeg){.cien}

!!! info "Canal de control (Puerto 21 TCP por defecto)"
    - Es la conexión principal (*out-of-band signaling*). Se establece al inicio de la sesión entre el cliente y el puerto de escucha 21 TCP del servidor.
    - Permanece **abierta de forma continua** durante toda la sesión del usuario.
    - Por este canal circulan exclusivamente órdenes cortas en texto ASCII (como `USER`, `PASS`, `LIST`, `RETR`, `QUIT`) emitidas por el cliente y las correspondientes respuestas numéricas de estado de 3 dígitos generadas por el servidor.
    - Por este canal **nunca viaja el contenido de los archivos** ni los listados de directorios.

!!! info "Canal de datos (Puertos variables TCP / Puerto 20 en modo activo)"
    - Es una conexión efímera que se abre **bajo demanda** únicamente cuando el cliente solicita una acción que implica intercambio de información volumétrica: transferir un fichero (subida con `STOR` o descarga con `RETR`) o solicitar el listado de archivos de una carpeta (`LIST` o `NLST`).
     - Una vez finalizada la transmisión del archivo o entregado el listado, el canal de datos **se cierra inmediatamente**. Si el usuario desea descargar otro fichero a continuación, se negociará y abrirá una nueva conexión de datos independiente.

!!! question "💡 ¿Por qué FTP desacopló el control de los datos?"
    - Este diseño permite al cliente enviar órdenes de interrupción (como el comando `ABOR` para abortar una descarga) a través del canal de control mientras un archivo enorme se está descargando por el canal de datos, sin tener que esperar a que termine de llegar la totalidad del flujo de bytes.

### 2.2 Tipos de datos: ASCII vs Binario

- El RFC 959 contempla distintos modos de interpretar la información transmitida a través del canal de datos
- Su correcta elección permitirá evitar la corrupción irreversible de los ficheros transferidos, especialmente cuando se trabaja con sistemas operativos heterogéneos (Windows, Linux, macOS):

| Modo de Transferencia | Comando FTP | Comportamiento del protocolo | Tipos de ficheros compatibles | Riesgo de corrupción |
|---|:---:|---|---||
| **Modo ASCII / Texto** | `TYPE A` | - Convierte automáticamente los caracteres de salto de línea entre sistemas operativos emisores y receptores.<br>- En Windows las líneas terminan en `CR+LF` (`\r\n`, bytes `0x0D 0x0A`), mientras que en Linux/UNIX terminan únicamente en `LF` (`\n`, byte `0x0A`). | Ficheros de texto plano (`.txt`, `.html`, `.css`, `.csv`, `.php`). | **Muy alto:** Si se transfiere un ejecutable, imagen o zip en modo ASCII, el servidor alterará los bytes `0x0D` y `0x0A`, destruyendo por completo la estructura del archivo. |
| **Modo Binario / Imagen** | `TYPE I` | Transmite el archivo byte a byte de forma idéntica, sin interpretar ni modificar ningún carácter ni secuencia de escape. | Ejecutables (`.exe`), imágenes (`.png`, `.jpg`), comprimidos (`.zip`, `.tar.gz`), bases de datos, PDFs. | **Nulo:** Conserva la integridad matemática del fichero íntegra. Es el modo por defecto en clientes modernos como FileZilla. |

### 2.3 Repertorio de comandos estándar de FTP (RFC 959)

Las órdenes que viajan por el canal de control son palabras mnemotécnicas de 3 o 4 caracteres en texto plano ASCII seguidas de parámetros y delimitadas por el terminador `CRLF` (`\r\n`):

!!! tip "Autenticación e inicio de sesión:"
    - `USER <nombre>`: Envía el identificador del usuario que desea iniciar sesión.
    - `PASS <contraseña>`: Envía la contraseña de dicho usuario.
    - `QUIT`: Cierra la conexión de control y finaliza la sesión en el servidor.

!!! tip "Navegación e inspección del sistema de ficheros:"
    - `PWD` (*Print Working Directory*): Muestra la ruta del directorio de trabajo actual en el servidor.
    - `CWD <ruta>` (*Change Working Directory*): Cambia al directorio especificado (equivalente a `cd`).
    - `CDUP` (*Change to Parent Directory*): Sube un nivel en el árbol jerárquico de directorios (equivalente a `cd ..`).
    - `MKD <directorio>` (*Make Directory*): Crea una nueva carpeta en la ruta remota.
    - `RMD <directorio>` (*Remove Directory*): Elimina la carpeta remota indicada.

!!! tip "Operaciones de transferencia y gestión de ficheros:"
    - `LIST`: Solicita el listado detallado de ficheros y directorios (permisos, tamaño, fecha de modificación, similar a `ls -la`). Se entrega a través del canal de datos.
    - `NLST` (*Name List*): Solicita una lista simple con únicamente los nombres de los ficheros.
    - `RETR <fichero>` (*Retrieve*): Descarga el archivo solicitado desde el servidor hacia el cliente.
    - `STOR <fichero>` (*Store*): Sube y almacena un archivo desde el cliente en el servidor.
    - `DELE <fichero>` (*Delete*): Elimina el fichero especificado del servidor.

!!! tip "Negociación del canal de datos:"
    - `PORT <h1,h2,h3,h4,p1,p2>`: Indica al servidor la dirección IP y el puerto TCP en el que el cliente espera la conexión de datos (Modo Activo).
    - `PASV`: Solicita al servidor que abra un puerto pasivo y espere la conexión del cliente (Modo Pasivo).
    - `TYPE <A|I>`: Establece el tipo de representación de los datos (`A` para ASCII, `I` para binario/imagen).

### 2.4 Códigos de respuesta del servidor

- Cada vez que el cliente emite una orden por el canal de control, el servidor responde obligatoriamente con un **código numérico de tres dígitos** acompañado de un texto descriptivo legible para humanos.

- La taxonomía del primer dígito categoriza de manera unívoca la respuesta:

![img](./img_6/img-6-4.jpeg){.cien}

| Código | Significado canónico del RFC 959 | Contexto habitual en el laboratorio y producción |
|:-:|---||
| `150` | *File status okay; about to open data connection.* | Notificación previa al inicio del flujo de datos en operaciones `LIST`, `RETR` o `STOR`. |
| `200` | *Command okay.* | La orden solicitada (por ejemplo, `TYPE I` o `PORT`) se ha procesado con éxito. |
| `220` | *Service ready for new user.* | Mensaje de bienvenida (*banner*) enviado por el servidor nada más abrir el canal de control en el puerto 21. |
| `226` | *Closing data connection. Requested file action successful.* | La transferencia del archivo o el listado del directorio ha finalizado completamente sin errores. |
| `227` | *Entering Passive Mode (h1,h2,h3,h4,p1,p2).* | Respuesta a la orden `PASV`, proporcionando la IP y puerto efímero del servidor para la conexión de datos. |
| `230` | *User logged in, proceed.* | Autenticación correcta de las credenciales introducidas. El usuario entra a su directorio raíz. |
| `331` | *User name okay, need password.* | Respuesta al comando `USER`; el nombre de cuenta es reconocido y el servidor aguarda el comando `PASS`. |
| `421` | *Service not available, closing control connection.* | El servidor está saturado de conexiones o se ha superado el tiempo máximo de inactividad (*timeout*). |
| `425` | *Can't open data connection.* | Fallo de negociación de red al intentar abrir el canal de datos (típico cuando un firewall bloquea los puertos). |
| `500` | *Syntax error, command unrecognized.* | La orden enviada por el cliente no existe o contiene parámetros sintácticamente inválidos. |
| `530` | *Not logged in.* | Credenciales erróneas (usuario/contraseña incorrectos) o acceso anónimo denegado por directiva. |
| `550` | *Requested action not taken. File unavailable or access denied.* | **El código de error más frecuente:** El usuario intenta leer, escribir o borrar un fichero sobre el que no tiene permisos NTFS/Linux, o la ruta indicada no existe. |

### 2.5 Modos de transferencia: Modo Activo (PORT) vs Modo Pasivo (PASV)

- La diferencia fundamental entre ambos modos radica en **quién toma la iniciativa para abrir la conexión TCP del canal de datos**:

#### 2.5.1 Modo Activo

![img](./img_6/img-6-6.png){.cien .marco .marginbottom20}

1. El cliente abre la conexión de control desde un puerto local (1035) hacia el puerto 21 del servidor.
1. Antes de transferir, el cliente abre el puerto 1036 en escucha y se lo comunica al servidor con PORT 192,168,1,50,4,12 (puerto = 4 × 256 + 12 = 1036).
1. El servidor confirma el comando con un ACK por el canal de control (21 → 1035).
1. El servidor inicia la conexión de datos desde su puerto 20 hacia la IP del cliente y el puerto 1036, y envía los datos.
1. El cliente confirma la recepción con un ACK (1036 → 20).

!!! question ":one: ¿Qué comando FTP de envío de datos ilustra la imagen anterior?<br>:two: ¿Qué comando se usaría para enviar datos en vez de recirbirlos?"

!!! warning "Limitaciones del modo activo"

    - Los clientes domésticos y corporativos suelen estar detrás de **un router con NAT/PAT y un cortafuegos con inspección de estado**.
    - El **comando PORT** incluye la IP privada del cliente, que no es alcanzable desde Internet**.
    - **Cuando el servidor envía el SYN desde su puerto 20** hacia el puerto del cliente, **el cortafuegos lo trata como tráfico entrante no solicitado y lo descarta** (normalmente en silencio). La conexión de control no sirve de referencia, porque es otra conexión.
    - **Solo funciona si el router tiene un ALG de FTP activo que reescriba la IP y el puerto en PORT y abra el puerto dinámicamente**. Con FTPS el ALG no puede inspeccionar el tráfico, así que la conexión de datos falla igualmente.
    - Por eso en Internet se usa casi siempre **el modo pasivo**, donde es el cliente quien inicia ambas conexiones.

#### 2.5.2 Modo Pasivo

Para solventar el bloqueo originado por los cortafuegos de los clientes, se introdujo el modo pasivo:

![img](./img_6/img-6-7.png){.cien .marco .marginbottom20}

1. El cliente abre la conexión de control desde un puerto local (1035) hacia el puerto 21 del servidor.
1. Al necesitar datos, el cliente envía la orden PASV.
1. El servidor reserva un puerto efímero libre (ej. TCP 50020) y responde por el canal de control con 227 Entering Passive Mode (203,0,113,10,195,100). El puerto es 195 × 256 + 100 = 50020.
1. El cliente inicia la conexión de datos desde otro puerto local (1036) hacia el puerto 50020 del servidor. El servidor responde con SYN-ACK y el cliente cierra el handshake con ACK.
1. Como el cliente inicia ambas conexiones (1035 → 21 y 1036 → 50020), los cortafuegos locales y los routers NAT admiten los paquetes de respuesta en estado ESTABLISHED / RELATED.

### 2.6 Problemática del Modo Pasivo en entornos NAT y Cloud (AWS)

- El modo pasivo evita que el cliente tenga que aceptar conexiones entrantes, pero traslada el problema al servidor: si el servidor está detrás de un NAT o en la nube (por ejemplo, AWS), hay que configurarlo para que el cliente pueda alcanzar el puerto de datos.

- Caso sin configurar, donde la conexión de datos falla.
    ![img](./img_6/img-6-8.png){.cien .marco .marginbottom20 .margintop10}

- Puntos a configurar:  

    !!! tip ":one: - El servidor desconoce su IP pública."
        - En AWS EC2, la máquina virtual solo ve su IP privada (ej. 172.31.25.100).
        - La IP pública la gestiona el Internet Gateway de Amazon, que hace la traducción.
        - Sin configuración adicional, el servidor responde a PASV con su IP privada: 227 Entering Passive Mode (172,31,25,100,195,100).
        - El cliente intenta conectarse a esa IP, que no es enrutable desde Internet, y la conexión termina por timeout.

    !!! tip ":two: - Hay que indicar la IP pública en el servidor."
        - El administrador debe configurar la IP pública para que se envíe en la respuesta 227:
        - En vsftpd: parámetro pasv_address.
        - En IIS (Windows): campo Firewall External IP Address.
        - En AWS conviene usar una Elastic IP, porque la IP pública normal cambia al detener y volver a iniciar la instancia.
  
    !!! tip ":three: - Hay que limitar el rango de puertos pasivos."
        - Por defecto, el servidor puede elegir cualquier puerto efímero del sistema (unos 16.000 en Windows, más de 28.000 en Linux).
        - Abrir un rango tan grande en el cortafuegos es inviable e inseguro. Se debe fijar un rango reducido, por ejemplo del 50000 al 50100, y dimensionarlo según las transferencias simultáneas esperadas (cada transferencia usa un puerto).
  
    !!! tip ":four: - Hay que abrir los puertos en todos los cortafuegos."
        Deben permitirse las conexiones entrantes en:
         1. El Security Group de AWS (Inbound Rules): puerto 21 (control) y el rango pasivo (50000-50100).
         1. El cortafuegos del sistema operativo (Windows Firewall o iptables/ufw): los mismos puertos.
        !!! note "Los Security Groups son stateful, así que no hace falta una regla de salida para las respuestas."

- Escenario con pasv_address configurado con la IP públicac. El Internet Gateway reenvía el tráfico hacia la IP privada del servidor.
    ![img](./img_6/img-6-9.png){.cien .marco .marginbottom20 .margintop10}

## 3 - Seguridad en los protocolos de transferencia y acceso remoto

### 3.1 Vulnerabilidades del protocolo FTP tradicional

- El protocolo FTP original fue concebido a principios de los años 80 bajo un paradigma de confianza mutua dentro de redes académicas cerradas.
- Como consecuencia, **carece por completo de mecanismos criptográficos nativos**:  
    1. **Exposición total de credenciales:** Las órdenes `USER` y `PASS` viajan en texto plano por el canal de control. Cualquier analizador de protocolos conectado a la red local o en puntos intermedios de enrutamiento puede interceptar las contraseñas sin esfuerzo (*sniffing*  + `Wireshark`).
    1. **Intercepción y manipulación de datos:** Los archivos transferidos carecen de firmas de integridad o cifrado confidencial, permitiendo a un atacante en posición de intermediario (*Man-in-the-Middle*) leer el contenido o inyectar código malicioso en descargas de ejecutables.

### 3.2 FTPS: FTP sobre TLS

- FTPS añade cifrado TLS al protocolo FTP sin cambiar su modelo de comandos.
- La RFC 4217 define su funcionamiento, basado en la extensión de seguridad de la RFC 2228.
- El servidor se identifica con un certificado digital X.509.

#### 3.2.1 FTPS explícito (FTPES)

1. El cliente se conecta al puerto 21 TCP en texto claro y recibe el banner de bienvenida.
1. El cliente envía AUTH TLS para pedir que se cifre la conexión. Si el servidor acepta, responde 234.
1. Ambos realizan el handshake TLS. El servidor presenta su certificado y el cliente lo valida. Desde ese momento, el canal de control va cifrado con el algoritmo negociado.
1. El cliente envía USER y PASS ya por el canal cifrado.
1. Para cifrar también los datos, el cliente envía PBSZ 0 y PROT P (nivel Private). Sin PROT P, los datos viajan en claro.
1. Si el servidor no admite TLS (por ejemplo, responde 534), es el cliente quien decide si continúa sin cifrar o aborta.

#### 3.2.2 FTPS implícito (en desuso)

1. El cliente se conecta a un puerto dedicado: 990 TCP para control (y 989 TCP como puerto de origen de datos en modo activo).
1. El handshake TLS se realiza nada más abrir la conexión, antes de cualquier comando FTP. No existe AUTH TLS.
1. Estado actual: no está estandarizado y se considera obsoleto. Requiere puertos adicionales y no permite negociar capacidades como el explícito. Aun así, sigue presente en sistemas heredados.

!!! warning "Una consecuencia práctica que enlaza con el modo activo y pasivo:"
    - Como el canal de control va cifrado, los ALG de los routers no pueden leer PORT ni 227.
    - Por eso en FTPS conviene usar **el modo pasivo con un rango de puertos fijo y la IP externa configurada**.

### 3.3 SFTP: SSH File Transfer Protocol (El estándar seguro monocanal)

Existe una confusión conceptual muy extendida: **SFTP NO es FTP con cifrado**.

- **SFTP (SSH File Transfer Protocol)** es un protocolo totalmente independiente diseñado desde cero por el grupo de trabajo de la IETF como un **subsistema de extensión de SSH-2 (Secure Shell)**.
- **Arquitectura de conexión única (Monocanal):** A diferencia de la doble conexión de FTP, SFTP canaliza absolutamente todo (autenticación, navegación, listados, transferencias y control de flujo) a través de **un único puerto TCP: el puerto 22**.
- **Beneficios operativos determinantes:**
    1. **Cero problemas con NAT y cortafuegos:** Basta con permitir el puerto 22 TCP en los grupos de seguridad y reglas de red. No requiere rangos de puertos efímeros ni configuraciones de IP pública pasiva.
    1. **Cifrado extremo a extremo nativo:** Todo el canal viaja protegido por los algoritmos de intercambio de claves Diffie-Hellman y cifrados simétricos de alta seguridad (ChaCha20, AES-GCM).
    1. **Autenticación avanzada:** Se integra de forma nativa con los mecanismos de autenticación de SSH, permitiendo el acceso tanto por contraseñas como mediante **parejas de claves asimétricas pública/privada** sin intervención de contraseñas.

### 3.4 SCP: Secure Copy Protocol

- Es una utilidad de transferencia punto a punto no interactiva basada en el protocolo `rcp` (*Remote Copy*) de los sistemas BSD, operando igualmente sobre el túnel seguro de **SSH (puerto 22 TCP)**.
- **Diferencia con SFTP:** SCP está orientado a la copia directa de archivos mediante una orden puntual de línea de comandos (ej. `scp archivo.txt usuario@servidor:/ruta/`), optimizando la velocidad de transferencia al no mantener una sesión interactiva de gestión del sistema de ficheros. SFTP, por contra, es un protocolo de sistema de archivos distribuido completo que permite reanudar descargas, pausar transferencias, consultar cuotas, listar directorios y modificar atributos de ficheros.

### 3.5 Taba resumen de protocolos

| Criterio técnico | FTP clásico (RFC 959) | FTPS Explícito (FTPES) | FTPS Implícito (Legacy) | SFTP (SSH File Transfer) | SCP (Secure Copy) |
|---|:---:|:---:|:---:|:---:||
| **Protocolo base** | FTP | FTP + TLS/SSL | FTP + TLS/SSL | SSH-2 (Subsistema) | SSH-2 (Túnel RPC) |
| **Cifrado de datos y credenciales** | ❌ No (Texto claro) | ✔️ Sí (TLS 1.2 / 1.3) | ✔️ Sí (TLS 1.2 / 1.3) | ✔️ Sí (Cifrado SSH) | ✔️ Sí (Cifrado SSH) |
| **Puertos de red utilizados** | TCP 21 (control) + TCP 20/dinámicos (datos) | TCP 21 (control) + Puertos pasivos (datos) | TCP 990 (control) + TCP 989/dinámicos | **Únicamente TCP 22** | **Únicamente TCP 22** |
| **Número de conexiones TCP** | 2 independientes | 2 independientes | 2 independientes | **1 única multiplexada** | **1 única conexión** |
| **Complejidad en NAT / Firewalls** | Muy alta (bloqueo en modo activo) | Alta (requiere abrir rango pasivo e IP pública) | Alta (requiere abrir puertos específicos) | **Mínima (solo requiere abrir el puerto 22)** | **Mínima (solo requiere abrir el puerto 22)** |
| **Mecanismo de autenticación** | Usuario / Contraseña en texto plano | Usuario / Contraseña + Certificado X.509 | Usuario / Contraseña + Certificado X.509 | Contraseña o **Claves asimétricas (RSA/Ed25519)** | Contraseña o **Claves asimétricas (RSA/Ed25519)** |
| **Interoperabilidad interactiva** | Sí (cliente gráfico y consola) | Sí (cliente gráfico y consola) | Sí (compatibilidad reducida) | Sí (FileZilla, consola interactiva `sftp`) | No (comando directo de copia puntual) |
| **Estado actual (en desuso vs. uso vigente)** | 🚫 **En desuso.** No debe usarse en redes no confiables: expone credenciales y datos. Solo se tolera en redes aisladas o por compatibilidad con equipos antiguos. | ✅ **Vigente.** Es la forma estándar de FTPS (RFC 4217). Se usa cuando se necesita mantener infraestructura FTP con cifrado y certificados. | 🚫 **En desuso (legacy).** Nunca fue estandarizado oficialmente (anterior a RFC 4217). Solo se mantiene por compatibilidad; se recomienda migrar a FTPES o SFTP. | ✅ **Recomendado.** Es el estándar de facto actual para transferencias seguras de ficheros, en servidores, automatización y entornos cloud. | ⚠️ **Obsoleto / desaconsejado.** El protocolo SCP/RCP original tiene debilidades de seguridad conocidas. OpenSSH 9.0+ lo implementa internamente sobre SFTP, y el comando `scp` se mantiene solo por comodidad. Se recomienda `sftp` o `rsync` sobre SSH. |

## 4 - Ecosistema de software: Servidores y Clientes (Windows y Linux)

### 4.1 Software de Servidor

- **Internet Information Services (IIS - Rol Servidor FTP):** Servidor FTP empresarial desarrollado por Microsoft e integrado de forma nativa en las ediciones de Windows Server. Proporciona administración centralizada mediante interfaz gráfica (`inetmgr`) o PowerShell, soportando FTPS explícito, aislamiento de usuarios basado en directorios o Active Directory, y registro de logs en formato W3C.
- **vsftpd (Very Secure FTP Daemon):** Servidor FTP estándar de referencia en distribuciones Linux (Ubuntu, Debian, Red Hat). Reconocido por su seguridad extrema frente a desbordamientos de búfer, bajo consumo de recursos y alto rendimiento. Su configuración reside en el fichero de texto plano `/etc/vsftpd.conf`.
- **OpenSSH Server (`sshd`):** Servicio de administración y acceso remoto multiplataforma que proporciona simultáneamente servicios de consola remota, SFTP y SCP. Disponible de forma nativa tanto en distribuciones Linux (`/etc/ssh/sshd_config`) como característica opcional en Windows Server.

### 4.2 Software de Cliente

- **FileZilla Client:** Herramienta gráfica multiplataforma (Windows, Linux, macOS) líder en el sector. Presenta una interfaz de doble panel (árbol local a la izquierda y árbol remoto a la derecha), con soporte nativo para FTP, FTPS y SFTP, gestor de sitios protegidos y reanudación automática de transferencias interrumpidas.
- **PuTTY y PuTTYgen:** Suite de utilidades de conectividad para entornos Windows. Permite el acceso a la consola SSH remota de servidores y, mediante la herramienta **PuTTYgen**, la generación, conversión y gestión de parejas de claves criptográficas en formato propietario `.ppk` (*PuTTY Private Key*).
- **Clientes integrados de consola (CLI):** Utilidades nativas en terminales de Linux y PowerShell en Windows, como `ftp`, `sftp`, `scp`, `ssh` y `curl`.

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

### 4.2 Mecanismos de enjaulado y aislamiento de usuarios (chroot y LocalUser)

- Por defecto, si un servidor FTP autentica a un usuario local sin medidas de confinamiento, el usuario aterrizará en su carpeta personal pero tendrá la capacidad técnica de emitir órdenes `cd ..` y navegar libremente hacia directorios raíz del sistema (como `C:\Windows\System32` o `/etc`), pudiendo consultar ficheros confidenciales del sistema operativo.

- Para impedirlo, se aplica el mecanismo de **enjaulado** (*chroot jail* / *User Isolation*):

#### 4.2.1 Enjaulado en Linux con `vsftpd` (`chroot`)

1. **La directiva `chroot_local_user=YES`** instruye a `vsftpd` a realizar una llamada de sistema `chroot()`, convirtiendo el directorio asignado al usuario en su nueva raíz lógica del sistema de ficheros (`/`). Cualquier intento de subir a un nivel superior es bloqueado por el propio kernel.
1. **La directiva `allow_writeable_chroot`:** Por motivos de seguridad estricta, `vsftpd` implementa una defensa contra vulnerabilidades conocidas de elevación de privilegios: 
    - Si el directorio raíz donde queda confinado el usuario tiene permisos de escritura en Linux, el servidor aborta la conexión con el error:  
    `500 OOPS: vsftpd: refusing to run with writable root inside chroot()`  
    - Para resolverlo de forma segura en entornos docentes y productivos se habilita la directiva:
    ```ini
    allow_writeable_chroot=YES
    ```
    *(o alternativamente, se retiran los permisos de escritura del directorio raíz con `chmod a-w` y se crea una subcarpeta interna con permisos de escritura).*

#### 4.2.2 Aislamiento de usuarios en Windows Server (IIS `LocalUser`)

1. En el Administrador de IIS, la característica **Aislamiento de usuarios FTP** (*FTP User Isolation*) se configura seleccionando la opción **Directorio de nombre de usuario**.
1. El servidor exige crear una estructura de carpetas estricta bajo la raíz del sitio FTP denominada `LocalUser`:
    - `C:\inetpub\ftproot\LocalUser\<nombre_de_usuario>`: Cada usuario local autenticado es confinado automáticamente a su carpeta homónima. Desde su cliente FTP, esa carpeta aparecerá como la raíz `/`, sin permitirle ver ni acceder a las carpetas de otros compañeros ni al resto del disco duro.
    - `C:\inetpub\ftproot\LocalUser\Public`: Carpeta compartida a la que son dirigidos los usuarios anónimos o no aislados.

### 4.3 Administración remota segura con SSH y bastionado (Hardening)

- La administración de servidores en entornos modernos exige canales cifrados y robustos frente a accesos no autorizados.
- El protocolo **SSH (Secure Shell)** sobre el **puerto 22 TCP** reemplazó a protocolos vulnerables antiguos como Telnet y Rlogin.

#### 4.3.1 Autenticación por parejas de claves asimétricas

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

#### 4.3.2 Bastionado (*Hardening*) del servicio OpenSSH

Para proteger un servidor expuesto a Internet en la nube frente a intrusiones automatizadas, se aplican las siguientes directivas en su fichero de configuración (`/etc/ssh/sshd_config` o `C:\ProgramData\ssh\sshd_config`):

1. **Desactivación de autenticación por contraseña (`PasswordAuthentication no`):**  
   Fuerza que cualquier conexión deba autenticarse obligatoriamente mediante una clave asimétrica válida. Si un atacante lanza un ataque de fuerza bruta con millones de contraseñas de diccionario, el servidor rechazará la conexión instantáneamente sin procesar la petición.
2. **Desactivación del acceso directo de superusuario (`PermitRootLogin no`):**  
   Impide que se intente iniciar sesión directamente como `root` o `Administrator`. Se debe ingresar con un usuario estándar y posteriormente elevar privilegios mediante `sudo`.
3. **Limitación de intentos de conexión (`MaxAuthTries 3`):**  
   Cierra la sesión tras tres intentos erróneos, bloqueando escaneos masivos.
4. **Cierre de sesiones inactivas (`ClientAliveInterval 300`):**  
   Envía paquetes nulos para desconectar automáticamente a usuarios que olviden cerrar su terminal tras 5 minutos de inactividad.

### 4.4 Auditoría, análisis forense y monitorización de registros (Logs y Wireshark)

La observabilidad y el registro de eventos son requisitos indispensables para garantizar la trazabilidad de accesos, detectar intrusiones y cumplir con normativas de ciberseguridad como el **Esquema Nacional de Seguridad (ENS)** y el **RGPD**:

#### 4.4.1 Registros en formato W3C en Microsoft IIS

El servicio FTP de IIS almacena sus accesos en ficheros de texto estructurados conforme al estándar **W3C Extended Log Format** (ubicados por defecto en `C:\inetpub\logs\LogFiles\FTPSVC1\`):

```text
#Fields: date time c-ip cs-username s-ip s-port cs-method cs-uri-stem sc-status sc-win32-status
2026-10-21 10:15:32 198.51.100.25 usuari_ventas 172.31.25.10 21 USER usuari_ventas 331 0
2026-10-21 10:15:32 198.51.100.25 usuari_ventas 172.31.25.10 21 PASS *** 230 0
2026-10-21 10:16:05 198.51.100.25 usuari_ventas 172.31.25.10 21 RETR /manual.pdf 226 0
2026-10-21 10:17:12 198.51.100.25 anonymous 172.31.25.10 21 STOR /subir.exe 550 5
```

- `date`: Fecha en la que se registra el evento (formato `AAAA-MM-DD`, en hora UTC por defecto en el formato W3C).
- `time`: Hora exacta del evento (formato `HH:MM:SS`). Junto con `date` permite reconstruir la cronología de una intrusión o un fallo.
- `c-ip`: Dirección IP pública del cliente que realiza la conexión.
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

#### 4.4.2 Registros en servidores Linux

- `/var/log/vsftpd.log`: Registra cada conexión entrante, inicios de sesión y operaciones de subida y descarga con indicación exacta de bytes transferidos.
- `/var/log/auth.log` (o `/var/log/secure`): Registra todos los intentos de autenticación en el servidor (accesos aceptados por clave pública `Accepted publickey`, intentos fallidos por contraseña `Failed password for invalid user`, y elevaciones mediante `sudo`).

#### 4.4.3 Inspección de paquetes de red con Wireshark

Mediante el uso de analizadores de tráfico en el aula o laboratorio, es posible visualizar la diferencia palpable entre la opacidad del tráfico cifrado y la vulnerabilidad del tráfico plano:

- **En FTP estándar (Puerto 21):** Los paquetes TCP revelan claramente las cabeceras `USER` y `PASS` con las contraseñas legibles en texto ASCII, así como los datos transferidos.
- **En FTPS (TLS) y SFTP (SSH):** Todos los paquetes TCP aparecen etiquetados como *Application Data* cifrado con *payloads* aleatorios ininteligibles, protegiendo la confidencialidad de la información frente a atacantes en el mismo segmento de red.

### 4.5 Buenas prácticas y control de costes en laboratorios Cloud

Al operar infraestructuras en entornos de nube pública (**AWS Academy / AWS Learner Lab**), el rol del administrador de sistemas incluye la gestión rigurosa de los recursos:

1. **Principio de mínimo privilegio:** Desactivar el acceso directo de cuentas con privilegios de superusuario (`Administrator` o `root`) al servicio FTP.
1. **Defensa en profundidad en cortafuegos:** Limitar la apertura de puertos pasivos en los grupos de seguridad estrictamente al rango acotado necesario para las transferencias del aula.
1. **Control y optimización de costes en AWS:** Las instancias virtuales EC2 consumen saldo del laboratorio mientras permanecen en estado `Running`. Al finalizar la sesión lectiva o el trabajo en casa, es **obligatorio detener las instancias (`Stop instance`)** desde la consola web de AWS. Detener la instancia congela el consumo de cómputo preservando íntegros los datos del disco SSD (EBS).

## 6 - Tarea RA3-CEb-1 - Instalación y configuración de IIS FTP y OpenSSH

<a id="aviso-cambio-ip"></a>
> 💡 **Regla de oro de AWS Academy: ¿Trabajas en días diferentes? Gestión del cambio de IP pública**
>
> En los laboratorios de AWS Academy Learner Lab, las máquinas virtuales utilizan **direcciones IPv4 públicas dinámicas**. Esto significa que **cada vez que detengas tu instancia (`Stop instance`) al terminar la clase y la vuelvas a iniciar (`Start instance`) en un día posterior, AWS le asignará una nueva dirección IP pública**.
>
> **¿Qué debes revisar obligatoriamente si retomas la práctica en un día diferente?**
> 1. **Conexión inicial (RDP / SSH / PuTTY):** Deberás conectarte siempre a la **nueva IP pública** que muestre la consola de AWS EC2 (la IP del día anterior dejará de responder).
> 2. **Modo Pasivo en Windows Server (IIS):** El servidor IIS envía al cliente la IP externa configurada en `FTP Firewall Support`. Si la IP ha cambiado y no la actualizas en IIS, FileZilla se conectará al puerto 21 pero **fallará al listar los archivos con un error de tiempo de espera (*timeout*)**. 👉 Puedes actualizarla rápidamente siguiendo el [Apartado 6.5: Soporte de Firewall de FTP](#actualizar-ip-windows).
> 3. **Modo Pasivo en Ubuntu Server (`vsftpd`):** El demonio `vsftpd` tiene configurada la IP en el fichero `/etc/vsftpd.conf` (`pasv_address`). Si la IP ha cambiado, FileZilla se quedará congelado en `150 Here comes the directory listing...`. 👉 Puedes actualizarla siguiendo el [Apartado 12.3: Configuración de modo pasivo en vsftpd](#actualizar-ip-ubuntu).
> 4. **Pruebas inter-servidores (Apartado 14):** Los comandos `curl`, `ssh` y `scp` deberán apuntar a las nuevas IPs actuales de cada servidor. 👉 Consulta los detalles en el [Apartado 14](#apartado-14).
>

> ⚠️ **Obligatorio seguir las normas para la presentación de trabajos escritos.**
>
> Todas las evidencias deberán incluir capturas de pantalla completas donde se aprecie claramente el nombre del equipo, usuario y la fecha/hora.
>

---

### 6.0 Lanzamiento de la instancia EC2 de Windows Server 2022 en AWS

1. Iniciar el laboratorio de **AWS Academy Learner Lab** pulsando **Start Lab** y, cuando el indicador superior pase a verde, hacer clic en **AWS** para abrir la consola de administración.
2. En la consola de **EC2** -> **Instances** -> pulsar en el botón naranja **Launch instances** (**Lanzar instancias**) y configurar la máquina con los siguientes parámetros técnicos:

| Parámetro de configuración | Valor requerido |
|---|---|
| **Name (Nombre)** | `Servidor_FTPSSH` |
| **Application and OS Images (AMI)** | `Microsoft Windows Server 2022 Base` (64 bits x86) |
| **Instance type (Tipo de instancia)** | **`t3.small`** (Recomendado — 2 vCPU, 2 GiB RAM, **Apto para la capa gratuita**) o **`t3.medium`** (2 vCPU, 4 GiB RAM) |
| **Key pair (login)** | `vockey` (par de claves RSA `.pem` proporcionado por AWS Academy) |
| **Network settings** | Asignar IP pública automáticamente (**Auto-assign public IP: Enable**) |
| **Configure storage** | `30 GiB` gp3 (SSD de uso general) |

> 💡 **Elección del tipo de instancia en Windows Server: t3.small vs t3.medium y la Capa Gratuita**
>
> En el desplegable de **Instance type**, AWS muestra varias opciones de la familia moderna `t3` (con procesadores más rápidos y 2 vCPU):
>
> * **Opción recomendada con Capa Gratuita: `t3.small`**
>   * Cuenta con **2 vCPU y 2 GiB de memoria RAM**.
>   * Viene identificada explícitamente con la etiqueta **«Apto para la capa gratuita»** (*Free tier eligible*).
>   * Cumple los requisitos oficiales de Windows Server 2022 y permite a los alumnos trabajar con total tranquilidad al ver el distintivo de capa gratuita.
> * **Opción de máximo rendimiento: `t3.medium`**
>   * Cuenta con **2 vCPU y 4 GiB de memoria RAM**.
>   * Aunque no lleva la etiqueta de capa gratuita, en AWS Academy su coste es de apenas **0,06 $ / hora**, lo que se descuenta del saldo educativo promocional de 50$ (sin coste real en tarjeta). Ofrece una fluidez gráfica excelente al abrir simultáneamente Server Manager, IIS y PowerShell.
>
> > ⚠️ **¡Evitar t3.nano y t3.micro en Windows Server!**
> > Aunque `t3.micro` también figure como apta para la capa gratuita, solo dispone de **1 GiB de RAM**. Windows Server 2022 con interfaz gráfica colapsará por falta de memoria RAM: tardará una eternidad en arrancar, el Administrador del Servidor fallará y la sesión RDP se congelará.
>

![Opciones de tipo de instancia t3 en AWS EC2 mostrando t3.small y t3.micro como aptas para la capa gratuita](./07_Transferencia_Ficheros_FTP_SSH/imagenes/00c_selector_tipo_instancia_t3_capa_gratuita.png)
*Figura 0b: Desplegable de tipos de instancia en AWS EC2, mostrando t3.small (2 vCPU, 2 GiB) con la etiqueta Apto para la capa gratuita.*

3. **Descarga de la clave privada (`.pem`) desde AWS Academy Learner Lab:**
   * En la parte superior de la ventana del laboratorio de AWS Academy (la barra superior de Vocareum donde figuran los botones *Start Lab*, *End Lab* y el saldo), haz clic en el botón **AWS Details**.
   * En el panel emergente lateral derecho que se despliega (**Cloud Access**), busca la sección **SSH key:**.
   * Haz clic sobre el botón **Download PEM**.
   * Se descargará en tu equipo el archivo **`labsuser.pem`** (correspondiente al par de claves `vockey` asignado en el laboratorio).
   * 📁 **Guarda este archivo en una ubicación segura y conocida de tu ordenador** (por ejemplo, en la carpeta de la práctica o en `Descargas`). Esta clave privada RSA es **imprescindible** tanto para descifrar la contraseña del usuario `Administrator` de Windows Server como para autenticarte mediante SSH/SFTP más adelante.

![Ubicación del botón AWS Details y descarga de la clave labsuser.pem en AWS Academy](./07_Transferencia_Ficheros_FTP_SSH/imagenes/00b_aws_details_download_pem.png)
*Figura 0: Panel Cloud Access abierto tras pulsar en AWS Details en la barra superior de AWS Academy, mostrando el botón Download PEM para obtener el archivo labsuser.pem.*

```text title="Ubicación del archivo labsuser.pem en AWS Academy"
+----------------------------------------------------------------------------------------------------+
|  [Start Lab]   [End Lab]   [AWS] (círculo verde)   [AWS Details]   [$0.00 / $100.00]   [Readme]    |
+----------------------------------------------------------------------------------------------------+
                                                           |
                                      +--------------------+---------------------+
                                      | Panel AWS Details (Cloud Access):        |
                                      | AWS CLI: [Show]                          |
                                      | SSH key: [Download PEM]  <-- ¡PULSAR!    |
                                      |          [Download PPK]                  |
                                      +------------------------------------------+
```

> 📷 **Evidencia 1 (insertar en tu documento Word) — Realizar captura de pantalla** del resumen de creación de la instancia `Servidor_FTPSSH` en AWS EC2 mostrando su estado `Running`, el tipo de instancia y su dirección IPv4 pública.

---

### 6.1 Preparación de la instancia en AWS y apertura de puertos

Antes de configurar los servicios en la máquina, debemos garantizar que el **Security Group** de AWS autorice las conexiones RDP, SSH y los puertos requeridos por FTP.

1. Acceder a la consola de AWS -> **EC2** -> en el menú lateral izquierdo desplegar **Network & Security** y hacer clic en **Security Groups** (o **Grupos de seguridad**).

![Acceso a Security Groups en el menú lateral de EC2](./07_Transferencia_Ficheros_FTP_SSH/imagenes/01_menu_security_groups.png)
*Figura 1: Acceso a Security Groups en la sección Network & Security de EC2.*

2. En el panel superior, hacer clic en el botón naranja **Create security group** (**Crear grupo de seguridad**).

![Botón Crear grupo de seguridad en el panel de EC2](./07_Transferencia_Ficheros_FTP_SSH/imagenes/02_boton_crear_sg.png)
*Figura 2: Creación de un nuevo grupo de seguridad desde el panel de EC2.*

3. Indicar los detalles básicos del grupo (**Basic details**):
   * **Security group name:** `grup-servidors-ftp-ssh`
   * **Description:** `Regles per a RDP, SSH i FTP amb ports passius`
   * **VPC:** La VPC asignada por defecto en el laboratorio.

> 💡 **Regla de nomenclatura en AWS**
>
> En Amazon Web Services, el nombre de un grupo de seguridad **no puede comenzar por el prefijo `sg-`**, ya que AWS lo reserva internamente para los identificadores únicos del sistema (ej: `sg-0123456789abcdef`). Por ello nombramos el grupo como **`grup-servidors-ftp-ssh`** o **`servidores-ftp-ssh`**.
>

![Detalles básicos del Security Group](./07_Transferencia_Ficheros_FTP_SSH/imagenes/03_detalles_basicos_sg.png)
*Figura 3: Configuración del nombre, descripción y VPC del nuevo grupo de seguridad.*


4. En la sección **Inbound rules** (**Reglas de entrada**), pulsar en el botón **Add rule** (**Agregar regla**):

![Pulsar el botón Agregar regla en Reglas de entrada](./07_Transferencia_Ficheros_FTP_SSH/imagenes/04_boton_agregar_regla.png)
*Figura 4: Ubicación del botón Add rule para definir las aperturas de puertos.*

Añadir las 5 reglas requeridas:
   * **RDP:** Puerto `3389` TCP (para administrar gráficamente la máquina).
   * **SSH:** Puerto `22` TCP (para el servidor OpenSSH).
   * **FTP Control:** Puerto `21` TCP.
   * **FTP Pasivo (Windows):** Rango de puertos `50000-50100` TCP.
   * **FTP Pasivo (Ubuntu):** Rango de puertos `40000-40100` TCP.

> 📷 **Evidencia 2 (insertar en tu documento Word) — Realizar captura de pantalla** de la tabla de reglas de entrada del Security Group donde se vean los puertos 21, 22, 3389, 50000-50100 y 40000-40100.

![Tabla de reglas de entrada del Security Group completada](./07_Transferencia_Ficheros_FTP_SSH/imagenes/06_tabla_reglas_entrada.png)
*Figura 5: Definición completa de las 5 reglas de entrada (RDP, SSH, FTP 21 y rangos pasivos).*

5. Bajar hasta el final de la página y pulsar el botón naranja **Create security group**:

![Pulsar el botón Crear grupo de seguridad](./07_Transferencia_Ficheros_FTP_SSH/imagenes/07_boton_final_crear_sg.png)
6. Una vez creado, se mostrará el panel resumen del grupo de seguridad con sus 5 reglas activas:

![Panel resumen del grupo de seguridad con las 5 reglas activas](./07_Transferencia_Ficheros_FTP_SSH/imagenes/08_resumen_grupo_creado.png)
*Figura 7: Resumen del grupo de seguridad grup-servidors-ftp-ssh con sus 5 reglas de entrada operativas.*

7. **Asignación del grupo a la instancia Windows Server:**
   * En el menú lateral izquierdo, hacer clic en **Instances** (**Instancias**).
   * Marcar la casilla de `Servidor_FTPSSH`.
   * En el menú superior, pulsar en **Actions** -> **Security** -> **Change security groups**.

![Acceso a Cambiar grupos de seguridad desde el menú Acciones](./07_Transferencia_Ficheros_FTP_SSH/imagenes/09_cambiar_grupos_seguridad.png)
*Figura 8: Opción Change security groups en el menú Actions de la instancia.*

   * Seleccionar `grup-servidors-ftp-ssh`, eliminar el grupo anterior (`launch-wizard-1`) y hacer clic en el botón naranja **Save** (**Guardar**).

![Ventana Cambiar grupos de seguridad asociando el nuevo grupo](./07_Transferencia_Ficheros_FTP_SSH/imagenes/10_ventana_cambiar_grupos.png)
*Figura 9: Ventana de asociación del grupo grup-servidors-ftp-ssh y eliminación del grupo anterior.*

> 💡 **¿Por qué eliminamos launch-wizard-1? ¿Seguirá funcionando el RDP?**
>
> Al desasociar el grupo `launch-wizard-1` y dejar únicamente `grup-servidors-ftp-ssh`, garantizamos que toda la seguridad se centraliza en un único grupo ordenado y limpio. **No perderás el acceso por RDP**, ya que en el nuevo grupo hemos añadido explícitamente la regla de entrada para el puerto TCP `3389` (RDP).
>

---

### 6.2 Conexión RDP a la instancia de Windows Server

Para administrar gráficamente Windows Server 2022 nos conectaremos a través del protocolo **RDP (Remote Desktop Protocol)** utilizando el cliente nativo de Windows (*Conexión a Escritorio remoto* / `mstsc`). Como las máquinas desplegadas en AWS EC2 se crean con una contraseña aleatoria y cifrada, debemos descifrarla primero utilizando la clave privada `.pem`.

#### Paso 1: Verificación de estado y tiempo de espera de inicialización
1. En la consola de AWS -> **EC2** -> **Instances** (**Instancias**), comprueba que tu máquina `Servidor_FTPSSH` se encuentra en estado **`Running`** (**En ejecución**).
2. Observa la columna **Status check**. Para conectarte con total garantía, lo óptimo es que muestre **`2/2 checks passed`** (**2/2 comprobaciones superadas**).
3. ⏳ **Tiempo de inicialización de Windows (3 a 4 minutos):** Tras el arranque inicial de una máquina Windows Server en AWS, el servicio interno *EC2Launch* necesita entre 3 y 4 minutos para generar la contraseña local del usuario `Administrator` y cifrarla con la clave pública del laboratorio. Si pulsas en descifrar inmediatamente, la consola te mostrará una advertencia: *"Password is not available yet. Please wait at least 4 minutes after launching an instance."* Si esto ocurre, espera un par de minutos y refresca la ventana de la consola.

#### Paso 2: Descifrado de la contraseña de Administrator en AWS
1. Selecciona la instancia `Servidor_FTPSSH` marcando su casilla de verificación.
2. En la barra superior de acciones, haz clic en el botón **Connect** (**Conectar**).
3. Haz clic en la pestaña **RDP client** (**Cliente RDP** o **RDP (protocolo de escritorio remoto)**).
4. Observa los datos de conexión asignados por AWS:
   * **DNS público / IP pública:** Dirección remota a la que nos conectaremos.
   * **Nombre de usuario:** `Administrator`.
   * **Contraseña:** Enlace para obtener la clave descifrada.

![Pestaña RDP en Conectarse a la instancia mostrando DNS público, usuario Administrator y enlace para obtener contraseña](./07_Transferencia_Ficheros_FTP_SSH/imagenes/10b_ec2_rdp_client_tab.png)
*Figura 9b: Pestaña RDP (protocolo de escritorio remoto) en la consola de AWS EC2 para conectar con Windows Server.*

5. En el campo **Contraseña** (**Password**), haz clic en el enlace azul **Obtener la contraseña de Windows** (**Get password**).
6. En la pantalla emergente **Obtener la contraseña de Windows**:
   * Haz clic en el botón **Cargar archivo de clave privada** (**Upload private key file**).
   * En el explorador de archivos de tu ordenador, localiza y selecciona el archivo **`labsuser.pem`** (o `vockey.pem`) que descargaste en el apartado 6.0 desde el botón *AWS Details*.
   * Verás cómo el cuadro de texto inferior se rellena automáticamente con el texto de tu clave RSA privada (`-----BEGIN RSA PRIVATE KEY----- ...`) y se muestra la etiqueta con el nombre del archivo cargado.
   * Haz clic en el botón naranja inferior **Descifrar contraseña** (**Decrypt password**).

![Carga del archivo labsuser.pem y botón Descifrar contraseña en AWS EC2](./07_Transferencia_Ficheros_FTP_SSH/imagenes/10c_ec2_upload_pem_decrypt.png)
*Figura 9c: Carga del archivo labsuser.pem en el asistente de AWS EC2 y botón naranja Descifrar contraseña.*

7. La consola abrirá una ventana emergente mostrando los datos finales de acceso:
   * **Nombre de usuario:** `Administrator`.
   * **Contraseña:** La contraseña alfanumérica descifrada (con caracteres especiales).
8. 📋 **Copia la contraseña descifrada** pulsando en el icono del portapapeles y pulsa en el botón naranja **Aceptar**. Guárdala temporalmente en un bloc de notas o mantenla en el portapapeles.

![Ventana emergente con el usuario Administrator y la contraseña descifrada lista para copiar](./07_Transferencia_Ficheros_FTP_SSH/imagenes/10d_ec2_password_decrypted.png)
*Figura 9d: Ventana emergente en AWS con la contraseña de Administrator descifrada y lista para copiar con el icono del portapapeles.*

#### Paso 3: Conexión mediante Escritorio Remoto (RDP)
Dispones de dos métodos equivalentes para iniciar la sesión gráfica:

* **Método A (Automático mediante archivo .rdp):**
  1. En esa misma pestaña de RDP de AWS, haz clic en el botón **Descargar archivo de acceso directo a RDP** (**Download remote desktop file**).
  2. Guarda el archivo `.rdp` en tu equipo y haz doble clic sobre él.
  3. Al abrirlo, Windows mostrará una ventana de advertencia de seguridad (*Precaución: conexión remota desconocida*).
  4. Verifica que la opción **Portapapeles** está marcada (para poder pegar contraseñas y textos entre tu equipo y el servidor) y haz clic en el botón **Conectar**.

![Ventana de advertencia de seguridad de Conexión a Escritorio remoto de Windows](./07_Transferencia_Ficheros_FTP_SSH/imagenes/10e_rdp_seguridad_conectar.png)
*Figura 9e: Advertencia de conexión remota desconocida en Windows, permitiendo el uso del Portapapeles antes de pulsar Conectar.*

* **Método B (Manual mediante mstsc):**
  1. En tu ordenador del aula, pulsa el atajo de teclado `Windows + R`.
  2. Escribe `mstsc` y pulsa `Enter` para abrir la herramienta nativa *Conexión a Escritorio remoto*.
  3. En la casilla **Equipo:**, escribe o pega la **Dirección IPv4 pública** (o el DNS público) de tu instancia `Servidor_FTPSSH` (la encontrarás en el panel de EC2).
  4. Haz clic en **Conectar**.

#### Paso 4: Autenticación e inicio de sesión
1. Cuando Windows solicite las credenciales de acceso:
   * **Usuario:** `Administrator`
   * **Contraseña:** Pega la contraseña que acabas de descifrar en AWS.

> ⚠️ **Atención al inicio de sesión en ordenadores con dominio del instituto (SICE / Dominio corporativo)**
>
> Si realizas la práctica desde un equipo del aula que está integrado en un dominio corporativo o educativo, Windows asumirá por defecto que el usuario pertenece al dominio del centro (ej. `CENTRO\Administrator`). Esto provocará un fallo de credenciales erróneas.
>
> **Solución:** Pulsa en **Más opciones** (**More choices**) -> **Usar otra cuenta** (**Use a different account**) y escribe obligatoriamente:
> `.\Administrator`
>
> *(El punto y la barra `.\` fuerzan a que la autenticación se valide localmente en la máquina virtual de Windows Server en AWS, ignorando el dominio local).*
>

2. Si aparece una advertencia de seguridad indicando que no se puede comprobar la identidad del certificado SSL/TLS de la máquina remota (*"No se puede comprobar la identidad del equipo remoto..."*), marca la casilla **"No volver a preguntarme sobre conexiones a este equipo"** y pulsa en **Sí** (**Yes**).
3. Se abrirá la sesión remota en pantalla completa. Tras unos segundos preparando el entorno, se mostrará el escritorio de Windows Server 2022 y se ejecutará automáticamente el panel central **Server Manager** (**Administrador del Servidor**).

> 📷 **Evidencia 3 (insertar en tu documento Word) — Realizar captura de pantalla** del escritorio de Windows Server recién conectado mostrando el Administrador del Servidor (**Server Manager**).

---

### 6.3 Instalación del rol Servidor FTP (IIS) y Servidor OpenSSH

1. En el **Administrador del Servidor** (**Server Manager**), pulsar en el enlace central **Add roles and features** (o en el menú superior **Manage** -> **Add Roles and Features**).

![Acceso a Agregar roles y características desde Server Manager](./07_Transferencia_Ficheros_FTP_SSH/imagenes/11_server_manager_add_roles.png)
*Figura 10: Acceso al asistente para agregar roles y características desde el Administrador del Servidor (Server Manager).*

2. Avanzar por las pantallas preliminares (**Before You Begin**, **Installation Type** y **Server Selection**) manteniendo los valores por defecto pulsando **Next**.
3. En la pantalla **Server Roles**:
   * Marcar la casilla **Web Server (IIS)** (si aparece la ventana emergente solicitando características requeridas, confirmar haciendo clic en **Add Features**).
4. Avanzar por **Features** y **Web Server Role (IIS)** hasta llegar a la pantalla **Role Services**:
   * Desplegar la categoría **FTP Server** y marcar las casillas **FTP Service** y **FTP Extensibility**.
   * Verificar que en **Management Tools** queda marcada la **IIS Management Console**.

![Selección de los servicios de rol FTP Server en IIS](./07_Transferencia_Ficheros_FTP_SSH/imagenes/12_iis_ftp_role_services.png)
*Figura 11: Selección de los servicios de rol FTP Service y FTP Extensibility en el asistente de instalación.*

5. En la pantalla **Confirmation**, revisar los elementos y pulsar el botón **Install**.
6. Una vez completado el proceso, la barra de progreso mostrará el mensaje **Installation succeeded** y se activará el botón **Close**.

![Instalación completada con éxito de IIS y FTP Server](./07_Transferencia_Ficheros_FTP_SSH/imagenes/13_instalacion_completada_iis_ftp.png)
*Figura 12: Barra de instalación completada con éxito para el Servidor Web (IIS) y el Servicio FTP.*

7. Pulsar en el botón **Close** para cerrar el asistente.

---

### 6.3.1 Comprobación y activación del Servidor OpenSSH (Método Gráfico)

En las imágenes oficiales de Windows Server proporcionadas por Amazon Web Services (AWS EC2), la característica de **OpenSSH Server** ya viene preinstalada en el sistema como característica opcional (**Optional feature**), por lo que únicamente es necesario verificar su presencia e iniciar su servicio.

**Comprobación gráfica mediante Configuración:**
1. Pulsar en el botón **Inicio** de Windows -> hacer clic en el icono de **Configuración** (**Settings** - icono de rueda dentada).
2. Entrar en la sección **System** -> **Optional features** (o buscar `optional` en el buscador superior).
3. En la sección **Added features** (Características añadidas), escribir `ssh` en el filtro de búsqueda.
4. Comprobar que **OpenSSH Server** figura ya como instalado (no pulsar el botón **Remove**; pulsar en **Close** para cerrar la ventana).

![Comprobación de OpenSSH Server preinstalado en Optional features](./07_Transferencia_Ficheros_FTP_SSH/imagenes/14_openssh_server_optional_features.png)
*Figura 13: Comprobación de la característica OpenSSH Server ya preinstalada en la imagen EC2 de AWS.*

**Inicio y arranque del servicio OpenSSH (Consola gráfica de Servicios):**
1. Pulsar `Windows + R`, escribir `services.msc` y pulsar Enter (o desde **Server Manager** -> menú superior **Tools** -> **Services**).
2. Localizar en la lista el servicio **OpenSSH SSH Server**.
3. Hacer clic derecho sobre él -> **Propiedades** (**Properties**):
   * Cambiar el **Tipo de inicio** (**Startup type**) a **Automático** (**Automatic**).
   * Pulsar en el botón **Iniciar** (**Start**).
   * Pulsar **OK**.

![Servicio OpenSSH SSH Server en ejecución y en inicio automático](./07_Transferencia_Ficheros_FTP_SSH/imagenes/15_servicio_openssh_running.png)
*Figura 14: Consola gráfica de Servicios mostrando OpenSSH SSH Server en estado En ejecución (Running) y con tipo de inicio Automático.*

> 💡 **Alternativa rápida por PowerShell para administradores de sistemas**
>
> Si prefieres instalar y activar OpenSSH por línea de comandos, abre una consola de **PowerShell como Administrador** y ejecuta:
> ```powershell
> Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
> Start-Service sshd
> Set-Service -Name sshd -StartupType Automatic
> ```
>

---

### 6.4 Creación de usuarios locales para el servicio

1. Pulsar clic derecho sobre el botón Inicio de Windows -> **Computer Management** (o ejecutar `compmgmt.msc`).
2. En el panel izquierdo, desplegar **Local Users and Groups** -> carpeta **Users**.
3. Clic derecho en el panel central -> **New User...**:
   * **User name:** `alumne_redes`
   * **Full name:** `Alumne Redes`
   * **Description:** `Usuari per a proves de transferència`
   * **Password:** `Smx2026..@` (y confirmar la contraseña).
   * Desmarcar **User must change password at next logon**.
   * Marcar **User cannot change password** y **Password never expires**.
   * Pulsar en **Create** y luego en **Close**.

![Creación del usuario local alumne_redes](./07_Transferencia_Ficheros_FTP_SSH/imagenes/16_crear_usuario_alumne_redes.png)
*Figura 15: Ventana de creación del usuario local alumne_redes con las directivas de contraseña configuradas.*

4. Hacer doble clic sobre el usuario `alumne_redes` en la lista -> pestaña **Member Of**:
   * Pulsar en **Add...** -> escribir `Remote Desktop Users` -> pulsar en **Check Names** y **OK**.
   * Pulsar de nuevo en **Add...** -> escribir `Administrators` -> pulsar en **Check Names** y **OK** (imprescindible en las instancias Windows Server de AWS para que el servidor **OpenSSH** autorice el inicio de sesión por SSH y SFTP en el puerto `22`).
   * Comprobar que el usuario pertenece a los tres grupos (`Administrators`, `Remote Desktop Users` y `Users`), y pulsar en **Apply** y **OK**.

![Adición del usuario al grupo Remote Desktop Users](./07_Transferencia_Ficheros_FTP_SSH/imagenes/17_agregar_grupo_remote_desktop.png)
*Figura 16: Selección y comprobación del grupo Remote Desktop Users para el usuario alumne_redes.*

![Pertenencia de alumne_redes a los grupos Administrators, Remote Desktop Users y Users](./07_Transferencia_Ficheros_FTP_SSH/imagenes/17b_alumne_redes_member_of.png)
*Figura 16b: Pestaña Member Of mostrando al usuario alumne_redes dentro de Administrators, Remote Desktop Users y Users.*

> 📷 **Evidencia 4 (insertar en tu documento Word) — Realizar captura de pantalla** de la ventana de propiedades (**Properties** -> **Member Of**) del usuario `alumne_redes` mostrando su pertenencia a los grupos `Administrators`, `Remote Desktop Users` y `Users`.

---

<a id="actualizar-ip-windows"></a>
### 6.5 Configuración de Compatibilidad de Firewall de FTP y Modo Pasivo en IIS (FTP Firewall Support)

> 💡 **Atajo rápido con PowerShell para actualizar la IP pública en IIS (en solo 5 segundos)**
>
> Si retomas la práctica en un día posterior y tu instancia tiene una nueva IP pública, en lugar de navegar por los menús gráficos de IIS, puedes abrir **PowerShell como Administrador** en Windows Server y ejecutar estas dos líneas:
> ```powershell
> Set-ItemProperty "IIS:\Sites" -Name ftpServer.firewallSupport.externalIp4Address -Value "<NUEVA_IP_PUBLICA_WINDOWS>"
> Restart-Service ftpsvc
> ```
>

1. Abrir **Internet Information Services (IIS) Manager** (escribir `inetmgr` en Inicio o desde **Server Manager** -> **Tools** -> **Internet Information Services (IIS) Manager**).
2. En el panel izquierdo (**Connections**), hacer clic sobre el nombre del servidor (nodo raíz).
3. En el panel central, localizar la sección **FTP** y hacer doble clic sobre el icono **FTP Firewall Support**:

![Acceso a FTP Firewall Support en IIS Manager](./07_Transferencia_Ficheros_FTP_SSH/imagenes/18_iis_icono_ftp_firewall.png)
*Figura 17: Selección del nodo raíz del servidor y acceso a FTP Firewall Support en el Administrador de IIS.*

4. Para obtener la dirección IPv4 pública de la máquina virtual, volver a la pestaña del navegador con la consola de **AWS EC2** -> **Instancias** -> seleccionar `Servidor_FTPSSH` y, en la pestaña inferior **Detalles** (**Details**), copiar la **Dirección IPv4 pública** (pulsando sobre el icono de los dos cuadraditos azules situado a la izquierda de la IP):

![Copia de la Dirección IPv4 pública en la consola de AWS EC2](./07_Transferencia_Ficheros_FTP_SSH/imagenes/18b_aws_ip_publica.png)
*Figura 18: Localización y copia de la Dirección IPv4 pública de la instancia en la consola de AWS EC2.*

5. De vuelta en la ventana **FTP Firewall Support** de IIS, configurar los parámetros del canal de datos pasivo:
   * **Data Channel Port Range:** Escribir `50000-50100`.
   * **External IP Address of Firewall:** Pegar la **Dirección IPv4 pública actual** de vuestra instancia en AWS (en nuestro ejemplo, `52.90.151.179`).
   * En el panel lateral derecho (**Actions**), hacer clic en **Apply**.

![Configuración del rango pasivo y la IP pública en FTP Firewall Support](./07_Transferencia_Ficheros_FTP_SSH/imagenes/19_iis_ftp_firewall_support.png)
*Figura 19: Configuración del rango de puertos pasivos (50000-50100) y la dirección IPv4 pública externa de AWS.*

6. Al pulsar en **Apply**, aparecerá una ventana informativa recordando que es necesario abrir también dicho rango de puertos en el cortafuegos del sistema (lo cual realizaremos en el apartado 6.7). Pulsar en **OK**.

![Mensaje informativo de FTP Firewall Support](./07_Transferencia_Ficheros_FTP_SSH/imagenes/19b_aviso_ftp_firewall_support.png)
*Figura 19b: Aviso informativo recordando configurar la regla de puertos en el Firewall de Windows.*

> ⚠️ **¡No olvides poner la IPv4 Pública de AWS!**
>
> En Amazon Web Services la máquina virtual solo conoce su IP privada interna (`172.31.x.x`). Si dejas en blanco el campo **External IP Address of Firewall**, el servidor FTP responderá a los clientes externos con su IP privada y **FileZilla fallará al listar los directorios** en modo pasivo. Además, recuerda que si detienes y vuelves a iniciar la instancia en otro día de clase, deberás actualizar aquí la nueva IP pública.
>

> 📷 **Evidencia 5 (insertar en tu documento Word) — Realizar captura de pantalla** del panel FTP Firewall Support con el rango de puertos 50000-50100 y la IP pública de AWS introducidos.

---

### 6.6 Creación del sitio FTP en IIS (Add FTP Site)

1. En el panel izquierdo de IIS (**Connections**), desplegar el servidor, hacer clic derecho sobre la carpeta **Sites** y seleccionar **Add FTP Site...**:

![Acceso a Add FTP Site desde la carpeta Sites de IIS](./07_Transferencia_Ficheros_FTP_SSH/imagenes/20_iis_menu_add_ftp_site.png)
*Figura 20: Menú contextual sobre la carpeta Sites para añadir un nuevo sitio FTP.*

2. **Site Information:**
   * **FTP site name:** `FTP-AULA`
   * **Physical path:** `C:\inetpub\ftproot` -> Pulsar **Next**.

![Configuración del nombre del sitio FTP y ruta física](./07_Transferencia_Ficheros_FTP_SSH/imagenes/21_iis_ftp_site_info.png)
*Figura 21: Definición del nombre del sitio (FTP-AULA) y su directorio raíz físico (C:\inetpub\ftproot).*

3. **Binding and SSL Settings:**
   * **IP Address:** **All Unassigned** | **Port:** `21`.
   * **SSL:** Marcar **No SSL** -> Pulsar **Next**.

![Configuración de enlace IP, puerto 21 y modo sin SSL](./07_Transferencia_Ficheros_FTP_SSH/imagenes/22_iis_ftp_binding_ssl.png)
*Figura 22: Configuración del puerto de control 21 TCP y desactivación inicial de SSL.*

4. **Authentication and Authorization Information:**
   * **Authentication:** Marcar **Basic**.
   * **Authorization:** Seleccionar **Specified users** y escribir debajo `alumne_redes`.
   * **Permissions:** Marcar **Read** y **Write** -> Pulsar **Finish**.

![Configuración de autenticación básica y permisos para alumne_redes](./07_Transferencia_Ficheros_FTP_SSH/imagenes/23_iis_ftp_auth_permissions.png)
*Figura 23: Habilitación de autenticación básica y permisos de lectura y escritura para el usuario alumne_redes.*

5. Una vez finalizado el asistente, comprobar que el sitio `FTP-AULA` aparece en la lista de **Sites** en estado **Started (ftp)** escuchando por el puerto `21`:

![Sitio FTP-AULA creado e iniciado en IIS Manager](./07_Transferencia_Ficheros_FTP_SSH/imagenes/24_iis_sitio_ftp_creado.png)
*Figura 24: Sitio FTP-AULA activo y en estado iniciado (Started) en el Administrador de IIS.*

> 📷 **Evidencia 6 (insertar en tu documento Word) — Realizar captura de pantalla** de IIS Manager mostrando el sitio `FTP-AULA` creado y en estado iniciado (**Started**).

---

### 6.6.1 Asignación de permisos NTFS de escritura sobre C:\inetpub\ftproot

Por defecto, Windows Server concede únicamente permisos de **lectura** al grupo de usuarios estándar sobre el directorio físico `C:\inetpub\ftproot`. Aunque en IIS hayamos autorizado **Read** y **Write** para `alumne_redes`, cuando un usuario intenta subir un fichero, Windows comprueba **tanto los permisos FTP de IIS como los permisos NTFS del sistema de archivos** (aplicando siempre el más restrictivo). Por ello, debemos otorgar el permiso **Modify** (**Modificar**) al usuario `alumne_redes` en la carpeta:

1. Abrir el **Explorador de archivos** de Windows, navegar hasta `C:\inetpub`, hacer **clic derecho** sobre la carpeta **`ftproot`** y seleccionar **Properties** (**Propiedades**):

![Menú contextual sobre la carpeta ftproot seleccionando Properties](./07_Transferencia_Ficheros_FTP_SSH/imagenes/24b_ftproot_menu_properties.png)
*Figura 24b: Acceso a las propiedades de la carpeta física C:\inetpub\ftproot desde el Explorador de archivos.*

2. En la ventana **ftproot Properties**, abrir la pestaña superior **Security** (**Seguridad**) y pulsar en el botón **Edit...** (**Editar...**):

![Pestaña Security de ftproot Properties y botón Edit](./07_Transferencia_Ficheros_FTP_SSH/imagenes/24c_ftproot_security_edit.png)
*Figura 24c: Pestaña Security de las propiedades de ftproot y acceso a la edición de permisos NTFS.*

3. En la ventana de permisos, hacer clic en el botón **Add...**, escribir `alumne_redes`, pulsar en **Check Names** para resolver el nombre local completo y hacer clic en **OK**:

![Selección y comprobación del usuario alumne_redes en permisos NTFS](./07_Transferencia_Ficheros_FTP_SSH/imagenes/24d_ftproot_add_user.png)
*Figura 24d: Adición del usuario local alumne_redes a la lista de control de acceso (ACL) de la carpeta.*

4. Con el usuario **Alumne Redes (`alumne_redes`)** seleccionado en la lista superior, marcar la casilla **Modify** (**Modificar**) en la columna **Allow** (lo cual activará automáticamente también el permiso **Write**). Finalmente, pulsar en **Apply** y en **OK**:

![Asignación del permiso Modify para alumne_redes sobre ftproot](./07_Transferencia_Ficheros_FTP_SSH/imagenes/24e_ftproot_permissions_modify.png)
*Figura 24e: Concesión del permiso NTFS Modify (lectura, escritura y modificación) al usuario alumne_redes sobre C:\inetpub\ftproot.*

> 💡 **Permisos válidos tanto para FTP (puerto 21) como para SFTP/SSH (puerto 22)**
>
> Al asignar estos permisos NTFS directamente a la cuenta local `alumne_redes` sobre `C:\inetpub\ftproot`, el usuario no solo podrá subir y borrar archivos conectándose por **FTP tradicional o FTPS (puerto 21)**, sino que también tendrá acceso completo a dicho directorio cuando se conecte mediante **SSH o SFTP (puerto 22)**.
>

---

### 6.7 Regla en el Firewall de Windows Defender

1. En el **Administrador del Servidor** (**Server Manager**), desplegar el menú superior **Tools** y seleccionar **Windows Defender Firewall with Advanced Security** (o pulsar `Windows + R` y ejecutar `wf.msc`):

![Acceso a Windows Defender Firewall desde el menú Tools](./07_Transferencia_Ficheros_FTP_SSH/imagenes/25_server_manager_tools_firewall.png)
*Figura 25: Apertura de Windows Defender Firewall with Advanced Security desde el menú Tools de Server Manager.*

2. En el árbol izquierdo, seleccionar **Inbound Rules** (**Reglas de entrada**) y en la columna derecha (**Actions**) hacer clic en **New Rule...**:

![Selección de Inbound Rules y botón New Rule](./07_Transferencia_Ficheros_FTP_SSH/imagenes/26_firewall_inbound_new_rule.png)
*Figura 26: Selección de Inbound Rules y creación de una nueva regla de entrada.*

3. Configurar los pasos del asistente **New Inbound Rule Wizard**:
   * **Rule Type:** Marcar **Port** y pulsar **Next**.

![Selección del tipo de regla Port](./07_Transferencia_Ficheros_FTP_SSH/imagenes/27_firewall_rule_type_port.png)
*Figura 27: Selección de regla basada en puerto (Port).*

   * **Protocol and Ports:** Marcar **TCP**, seleccionar **Specific local ports** e introducir el rango `50000-50100` (o escribir directamente `22, 50000-50100` para dejar abierto a la vez el puerto `22` de **OpenSSH Server / SFTP** en el Firewall de Windows). Pulsar **Next**.

![Configuración del protocolo TCP y rango de puertos pasivos 50000-50100](./07_Transferencia_Ficheros_FTP_SSH/imagenes/28_firewall_protocol_ports.png)
*Figura 28: Apertura del rango de puertos TCP 50000-50100 para el canal de datos pasivo.*

> 💡 **Añadir el puerto 22 (SSH/SFTP) a la regla del Firewall de Windows**
>
> En las imágenes de Windows Server de AWS, aunque **OpenSSH Server** viene preinstalado, el Firewall de Windows Defender trae cerrado el puerto `22` TCP. Si ya habías creado la regla solo con `50000-50100`, puedes hacer **doble clic** sobre la regla creada (`FTP Pasivo Datos (50000-50100)`), ir a la pestaña **Protocols and Ports**, cambiar **Local port** a **`22, 50000-50100`** y pulsar **Apply** y **OK**:
>

![Inclusión del puerto 22 junto al rango pasivo 50000-50100 en las propiedades de la regla](./07_Transferencia_Ficheros_FTP_SSH/imagenes/28b_firewall_puerto_22_y_pasivo.png)
*Figura 28b: Pestaña Protocols and Ports permitiendo simultáneamente el puerto 22 (SSH/SFTP) y el rango 50000-50100 (FTP Pasivo).*

   * **Action:** Marcar **Allow the connection** y pulsar **Next**.

![Configuración de la acción Allow the connection](./07_Transferencia_Ficheros_FTP_SSH/imagenes/29_firewall_action_allow.png)
*Figura 29: Autorización de las conexiones entrantes (Allow the connection).*

   * **Profile:** Mantener marcados los tres perfiles (**Domain**, **Private** y **Public**) y pulsar **Next**.
   * **Name:** Escribir `FTP Pasivo Datos (50000-50100)` y pulsar **Finish**.

![Asignación del nombre a la regla del Firewall](./07_Transferencia_Ficheros_FTP_SSH/imagenes/30_firewall_rule_name.png)
*Figura 30: Nombre descriptivo de la regla para identificar los puertos pasivos de FTP.*

4. **Reiniciar el servicio FTP** para aplicar todos los cambios:
   * Abrir la consola gráfica de **Services** (`services.msc` o desde **Server Manager** -> **Tools** -> **Services**).
   * Localizar **Microsoft FTP Service**, hacer clic derecho sobre él y pulsar en **Restart**.

![Reinicio gráfico del servicio Microsoft FTP Service](./07_Transferencia_Ficheros_FTP_SSH/imagenes/31_reiniciar_servicio_ftp.png)
*Figura 31: Reinicio del servicio Microsoft FTP Service desde la consola gráfica de Servicios.*

> 📷 **Evidencia 7 (insertar en tu documento Word) — Realizar captura de pantalla** de la regla `FTP Pasivo Datos (50000-50100)` creada en el Firewall de Windows y del servicio `Microsoft FTP Service` en ejecución.

> ℹ️ **Qué debes añadir a tu documento Word al terminar el Apartado 6**
>
> En el **Apartado 6** de tu documento Word de la unidad, asegúrate de haber insertado y explicado brevemente las **Evidencias 1 a 7**:
>
> * **Evidencia 1:** Instancia `Servidor_FTPSSH` en estado `Running` en AWS EC2.
> * **Evidencia 2:** Tabla de reglas de entrada del Security Group `grup-servidors-ftp-ssh` (puertos `21`, `22`, `3389`, `50000-50100` y `40000-40100`).
> * **Evidencia 3:** Escritorio de Windows Server conectado por RDP mostrando **Server Manager**.
> * **Evidencia 4:** Propiedades del usuario `alumne_redes` (**Member Of**: `Administrators`, `Remote Desktop Users`, `Users`).
> * **Evidencia 5:** Configuración de `FTP Firewall Support` en IIS con el rango `50000-50100` y la IP pública de AWS.
> * **Evidencia 6:** Sitio `FTP-AULA` creado y en estado `Started` en IIS Manager.
> * **Evidencia 7:** Regla `FTP Pasivo Datos (50000-50100)` en el Firewall de Windows y servicio `Microsoft FTP Service` en ejecución.
>

---