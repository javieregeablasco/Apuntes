---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Servicios en red
module number: 0227
lesson: UD. 5.0 - Servicio DNS
author: Javier Egea Blasco  
layout: default  
year: 26-27  
keywords: SMX, SMR, SX, SR
schedule: 233h - 7h/w
---

![Descripción de la imagen](./img_5/img_5_1.jpg){ .img2 .marginbottom40}

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:**|
||
| **RA. 2 Instala servicios de resolución de nombres, describiendo sus características y aplicaciones.**|

|**Criterios de evaluación de la unidad didáctica:**|
||
|**a)** Se han identificado y descrito escenarios en los que surge la necesidad de un servicio de resolución de nombres.|
|**b)** Se han clasificado los principales mecanismos de resolución de nombres.|
|**c)** Se ha descrito la estructura, nomenclatura y funcionalidad de los sistemas de nombres jerárquicos.|
|**d)** Se ha instalado un servicio jerárquico de resolución de nombres.|
|**e)** Se ha preparado el servicio para almacenar las respuestas procedentes de servidores de redes públicas y servirlas a los equipos de la red local.|
|**f)** Se han añadido registros de nombres correspondientes a una zona nueva, con opciones relativas a servidores de correo y alias.|
|**g)** Se ha trabajado en grupo para realizar transferencias de zona entre dos o más servidores.|
|**h)** Se ha comprobado el funcionamiento correcto del servidor.|

## 1 - Introducción

!!! question "¿Qué es el DNS?"
    ![Descripción de la imagen](./img_5/img_5_3.png){.cincozero}

    - El **DNS** (*Domain Name System* o **Sistema de Nombres de Dominio**) es un sistema **distribuido y jerárquico** que permite asociar    nombres de dominio legibles para las personas, como `www.aules.edu.gva.es`, con **direcciones IP**, como `195.77.20.168`, que los  dispositivos utilizan para localizar servicios y comunicarse en una red.

    - El DNS suele describirse popularmente como la **"guía telefónica de Internet"**. Al igual que la agenda de un teléfono móvil nos evita  tener que memorizar los números de teléfono de cada persona, el DNS evita que los usuarios tengan que memorizar direcciones IP para  acceder a los diferentes servicios de una red.

    - Aunque normalmente pensamos en el DNS como un sistema que traduce nombres de dominio en direcciones IP, también permite realizar otro   tipo de consultas. Por ejemplo, puede indicar qué servidores se encargan del correo electrónico de un dominio o proporcionar  direcciones IPv6.

!!! question "¿Para qué sirve?"
    ![Descripción de la imagen](./img_5/img_5_5.png){.cincozero}

    La utilidad del sistema DNS es fundamental para el funcionamiento de Internet y de **muchas redes privadas**. Entre sus principales funciones encontramos:

    - **Simplifica el acceso a los servicios de red:** permite utilizar nombres fáciles de recordar en lugar de direcciones IP.

    - **Aporta flexibilidad:** si un servicio cambia de servidor o de dirección IP, es posible modificar la información DNS manteniendo el  mismo nombre de dominio. De esta forma, los usuarios pueden continuar utilizando el mismo nombre para acceder al servicio.

    - **Permite localizar servicios de red:** los dispositivos pueden consultar el DNS para obtener información sobre la ubicación de   diferentes servicios, como servidores web o servidores de correo electrónico.

    - **Facilita la administración de redes:** en las redes locales también es posible utilizar DNS para asociar nombres a equipos y    servicios, evitando tener que recordar sus direcciones IP.

    - **Interviene en numerosos servicios de Internet**, como:  

        - **Acceder a páginas web**.
        - **Enviar y recibir correos electrónicos**.
        - **Utilizar servicios de streaming**.
        - **Jugar a videojuegos online**.
        - **Acceder a diferentes servicios y aplicaciones de Internet**.

<!-- !!! warning "Resolución de nombre inversa"

    - La resolución de nombre inversa (o *reverse DNS lookup*) es el proceso contrario a la resolución de nombres habitual: en lugar de preguntar "¿qué dirección IP corresponde a este nombre de dominio?", la consulta pregunta "¿qué nombre de dominio corresponde a esta dirección IP?".
    - Para llevarla a cabo, el DNS utiliza un dominio especial llamado **in-addr.arpa** (para IPv4) o **ip6.arpa** (para IPv6). La dirección IP se transforma e inserta dentro de este dominio en orden inverso a como se escribe normalmente.  

        !!! example "Ejemplo"
            
            - Para averiguar el nombre asociado a la IP `192.168.10.20`, el *resolver* consulta el dominio:  
            `20.10.168.192.in-addr.arpa`  
            - El registro que responde a este tipo de consulta se llama **registro PTR** (*pointer record*), y es el encargado de indicar qué nombre de dominio corresponde a esa dirección IP.  
    
    - **Usos habituales de la resolución inversa:**
        - Verificación de correo electrónico: muchos servidores de correo comprueban que la IP del remitente tenga un PTR válido antes de aceptar el mensaje, como medida contra el *spam*.
        - Diagnóstico y registro (*logging*): en herramientas como `traceroute`, `ping` o en los logs de un servidor, es más legible ver el nombre de una máquina que su dirección IP.
        - Auditoría y seguridad: permite identificar qué equipo hay detrás de una IP concreta durante el análisis de tráfico o incidentes.
    
        !!! failure "A diferencia de la resolución directa, la resolución inversa requiere que el administrador de la red configure explícitamente esta zona y sus registros PTR, ya que no se genera de forma automática a partir de los registros A o AAAA." -->

<!-- > **Importante:** el DNS no es el encargado de conectar un dispositivo a una red Wi-Fi. En una conexión Wi-Fi intervienen tecnologías y protocolos como **IEEE 802.11** y, habitualmente, **DHCP** para obtener la configuración de red. El DNS puede utilizarse posteriormente para resolver los nombres de los servicios a los que queremos acceder. -->

## 2 - Protocolo DNS

![Descripción de la imagen](./img_5/img_5_18.png){.marco .seiszero}

- **El servicio de nombres de dominio utiliza el protocolo DNS para realizar las consultas y las respuestas**.
- Se trata de un protocolo de **capa de aplicación** que puede utilizar tanto UDP como TCP en la capa de transporte.  
- Habitualmente, tanto las consultas del cliente como las respuestas del servidor caben en un datagrama (512 bytes) y se utiliza UDP (de hecho, generalmente se dice que el DNS usa UDP). 
- Si la información a transmitir es amplia (por ejemplo, una respuesta con una lista con mucha información), la comunicación pasa a TCP automáticamente.
- Otro caso en el que la comunicación es por TCP es cuando se realiza la transferencia de información de una zona entre servidores primarios y secundarios. **El servidor DNS utiliza el puerto privilegiado 53**.

!!! tip "Resumen de los que hemos visto"
    - El protocolo DNS es habitualmente UDP, pero puede ser TCP y UDP.
    - Se trata de un protocolo de capa de aplicación y utiliza el puerto 53.
    - Los datagramas DNS se componen de varios apartados, tal como se puede ver en la siguiente consulta con host:

        !!! example "Ejemplo de consulta DNS"
            ![imagen](./img_5/img_5_17.png){.sietecinco}
    
## 3 - Mecanismos de comunicación DNS

La comunicación DNS es un mecanismo de consulta/respuesta entre **el cliente y el servidor**. Los datagramas, por tanto, serán de query (consulta) o de answer (respuesta).

!!! tip "Los apartados que componen un mensaje DNS son:"

     - **HEADER**. Cabecera del mensaje que indica si se trata de una consulta o de una respuesta. Contiene el id (identificador) del   mensaje, flags y un resumen de qué secciones del mensaje llevan información y cuánta.
     - **QUESTION**. Esta sección contiene la consulta que se ha efectuado, es decir, qué dato se ha pedido al servidor. Puede ser la   resolución de un nombre de dominio a una dirección IP, pedir la lista de servidores de impresión, etc.
     - **ANSWER**. Sección que contiene la respuesta obtenida del servidor. Esta respuesta será autoritativa o no en función de si el   servidor que responde es autoritativo para esa zona: cuando la respuesta procede de un servidor caché/resolver (no autoritativo), algunas utilidades de consulta la muestran como non-authoritative answer.
     - **AUTHORITY**. Esta sección contiene las respuestas que son autoritativas para la consulta efectuada. Evidentemente, puede estar vacía.
     - **ADDITIONAL**. Contiene información adicional para completar la respuesta. En el ejemplo se observa que completa la resolución de los nombres de máquina que aparecen en la sección ANSWER, indicando su dirección IP correspondiente.

!!! example "Ejemplo de comunicación DNS"
    ![imagen](./img_5/img_5_19.png){.ochocinco}

## 4 - Servidores DNS

- Un servidor DNS es el elemento de la infraestructura de red que aloja la información de uno o más espacios de nombres de dominio y que responde a las consultas (queries) que le llegan, ya sea resolviéndolas directamente (si tiene autoridad sobre los datos) o remitiendo al cliente hacia otros servidores que sí la tienen.
- Un mismo servidor puede ser autoritativo para unas zonas y actuar solo como intermediario (resolutor) para otras, y puede alojar simultáneamente varias zonas con roles distintos.

### 4.1 Zonas DNS

- Una **zona DNS** es la porción concreta del espacio de nombres que un servidor determinado aloja y sobre la cual puede responder consultas. Por ejemplo, el servidor autoritativo que resuelve `www.edu.gva.es` contiene la zona `edu.gva.es`.
- La información de una zona (sus registros de recursos) se puede almacenar en un archivo de texto en el propio servidor o en un directorio centralizado (como AD DS en entornos Windows). En este último caso se habla de *zonas integradas*, que permiten que varios servidores compartan y escriban sobre la misma copia de datos.

### 4.2 Tipos de zona

- **Zona primaria.** Es el origen editable de la zona: todas las altas, bajas y modificaciones de registros se hacen aquí. El servidor que la aloja se llama *servidor primario* de esa zona.
- **Zona secundaria.** Es una copia de solo lectura de una zona primaria, obtenida por red desde otro servidor DNS. No se puede editar directamente ni almacenarse como zona integrada, ya que siempre depende de la fuente primaria.
- **Zona de rutas internas (*stub*).** Contiene únicamente los registros NS (y sus direcciones) necesarios para identificar qué servidores son autoritativos para una zona concreta, sin el resto de datos. Se usa para mantener actualizada la lista de servidores de una zona delegada y para mejorar la resolución evitando consultas innecesarias a los servidores raíz.
- **Zona de búsqueda inversa.** Permite la consulta contraria a la habitual: a partir de una dirección IP, obtener el nombre del equipo (en vez de nombre → IP).

<!-- Se construye bajo el dominio especial `in-addr.arpa`, donde los octetos de la dirección IPv4 se invierten para formar la jerarquía de subdominios. -->

!!! warning "Zona de búsqueda inversa"

    - Para llevar a cabo la resolución de nombre inversa, el DNS utiliza un dominio especial llamado **in-addr.arpa** (para IPv4) o **ip6.arpa** (para IPv6). 
    - La dirección IP se transforma e inserta dentro de este dominio en orden inverso a como se escribe normalmente.  

        !!! example "Ejemplo"
            
            - Para averiguar el nombre asociado a la IP `192.168.10.20`, el *resolver* consulta el dominio:  
            `20.10.168.192.in-addr.arpa`  
            - El registro que responde a este tipo de consulta se llama **registro PTR** (*pointer record*), y es el encargado de indicar qué nombre de dominio corresponde a esa dirección IP.  
    
    - **Usos habituales de la resolución inversa:**
        - Verificación de correo electrónico: muchos servidores de correo comprueban que la IP del remitente tenga un PTR válido antes de aceptar el mensaje, como medida contra el *spam*.
        - Diagnóstico y registro (*logging*): en herramientas como `traceroute`, `ping` o en los logs de un servidor, es más legible ver el nombre de una máquina que su dirección IP.
        - Auditoría y seguridad: permite identificar qué equipo hay detrás de una IP concreta durante el análisis de tráfico o incidentes.
    
        !!! failure "A diferencia de la resolución directa, la resolución inversa requiere que el administrador de la red configure explícitamente esta zona y sus registros PTR, ya que no se genera de forma automática a partir de los registros A o AAAA."

!!! warning "Un mismo servidor no puede alojar a la vez una zona primaria y una secundaria o *stub* para el mismo nombre de dominio."

### 4.3 Transferencia de zona

Se conoce como **transferencia de zona** el proceso de replicar el contenido de una zona desde el servidor que la genera (primario) hacia los servidores que tienen copia de ella (secundarios). Se puede iniciar de dos maneras:

1. Por **notificación**: el servidor primario avisa a los secundarios cuando ha habido un cambio (mecanismo definido en el RFC 1996).
1. Por **intervalo de refresco**: al arrancar el servicio o al caducar dicho intervalo (por defecto, 15 minutos, definido en el registro SOA de la zona), el servidor secundario consulta al primario para comprobar si hay cambios.

Hay dos tipos de transferencia:

- **AXFR (transferencia completa):** replica todo el archivo de zona.
- **IXFR (transferencia incremental):** replica solo los registros modificados desde la última sincronización, reduciendo el tráfico de red.

Por motivos de seguridad, es recomendable restringir qué servidores pueden solicitar una transferencia de zona (habitualmente, solo los indicados en los registros NS de la zona), ya que una transferencia abierta a cualquier host expondría toda la estructura de la red interna.

### 4.4 Delegación de zonas

El espacio de nombres se puede dividir en varias zonas para delegar su administración a otros departamentos u organizaciones (por ejemplo, delegar `filial.empresa.com` desde la zona `empresa.com`). Para cada delegación es necesario crear registros NS en la zona padre que apunten a los servidores autoritativos de la nueva subzona, de modo que otros servidores y clientes puedan encontrarlos correctamente.

### 4.5 Control de acceso

El acceso de escritura a una zona y a sus registros se puede restringir mediante listas de control de acceso (ACL), que determinan qué usuarios o grupos pueden crear o modificar registros concretos. Esto permite, por ejemplo, reservar ciertos nombres para que solo determinados usuarios los puedan registrar, protegiendo la zona de modificaciones no autorizadas sin dejar de permitir su uso general.

## 5 - Consultas al DNS

En una búsqueda de DNS habitual se producen **tres tipos de consultas**.

Al usar una combinación de estas consultas, un proceso optimizado para la resolución de DNS puede conllevar una reducción de la distancia recorrida.  
En una situación ideal, los datos de registro almacenados en la memoria caché estarán disponibles, lo cual permitirá que un servidor de nombres DNS devuelva una consulta no recursiva.

1. **Consulta recursiva:** en una consulta recursiva, un cliente DNS requiere que un servidor DNS (generalmente un resolver DNS recursivo) responda al cliente con el registro del recurso solicitado o un mensaje de error si el resolver no puede encontrar el registro.
1. **Consulta iterativa:** en esta situación, el cliente DNS permitirá que un servidor DNS devuelva la mejor respuesta posible. Si el servidor DNS consultado no cuenta con un nombre que corresponda con el de la consulta, devolverá una referencia a un servidor DNS autoritativo para un nivel inferior del espacio de nombres de dominio. El cliente DNS hará a continuación una consulta a la dirección de referencia. Este proceso continúa con servidores DNS adicionales que siguen en la cadena de consulta hasta que se produzca un error o se supere el tiempo de espera.
1. **Consulta no recursiva:** generalmente se produce cuando un cliente resolver DNS consulta a un servidor DNS por un registro al que tiene acceso porque o bien es autoritativo para el registro o el registro existe dentro de su caché. Generalmente, el servidor DNS almacenará en caché registros DNS para prevenir el consumo de ancho de banda adicional y la carga en los servidores que preceden en la cadena.

## 6 - Funcionamiento del DNS

El funcionamiento del DNS se basa en un sistema **jerárquico y distribuido** conocido como **resolución de nombres de dominio**. Su función principal es obtener información asociada a un nombre de dominio, como su dirección IP.

Cuando escribimos la dirección web `www.aules.edu.gva.es` en el navegador, el dispositivo necesita obtener la dirección IP asociada a ese nombre antes de poder establecer la comunicación con el servicio.

La resolución de un nombre puede implicar diferentes servidores DNS. De forma simplificada, el proceso es el siguiente:

---

### 6.1 Inicio de la consulta y comprobación de la caché

El dispositivo realiza una consulta a un **servidor DNS recursivo**, también denominado **DNS resolver**. Habitualmente, este servidor es proporcionado por el proveedor de acceso a Internet, aunque también puede pertenecer a una organización, una empresa o ser **configurado manualmente**.
![Descripción de la imagen](./img_5/img_5_6.png){.marco .margintop10}

Antes de realizar nuevas consultas, pueden comprobarse diferentes **cachés DNS**. Por ejemplo, pueden existir cachés en:

- El navegador.
- El sistema operativo.
- El servidor DNS recursivo.

Si alguno de estos componentes dispone de una respuesta válida almacenada en caché, no será necesario repetir todo el proceso de resolución.

La información almacenada en caché tiene un tiempo de validez denominado **TTL (*Time To Live*)**.

---

### 6.2 Consulta al servidor raíz (*Root Server*)

Si el resolver recursivo no dispone de la respuesta en su caché, comienza la búsqueda consultando la jerarquía DNS.

El primer nivel corresponde a los **servidores raíz**.
![Descripción de la imagen](./img_5/img_5_7.png){.marco .margintop10}

Existen **13 servidores raíz lógicos**, identificados mediante las letras de la **A a la M**. Cada uno de ellos está replicado mediante numerosas instancias distribuidas geográficamente por diferentes lugares del mundo.

Los servidores raíz **no conocen directamente la dirección IP** del dominio que estamos buscando. Su función es indicar qué servidores son responsables del **dominio de nivel superior (TLD)** correspondiente.

Por ejemplo, si estamos buscando:

```text
www.aules.edu.gva.es
```

el servidor raíz puede indicar qué servidores se encargan del TLD `.es`.

---

### 6.3 Consulta al servidor de nivel superior (TLD)

El resolver recursivo consulta entonces a un **servidor TLD** (*Top-Level Domain*).
![Descripción de la imagen](./img_5/img_5_8.png){.marco .margintop10}

Un TLD es la parte final de un nombre de dominio, como:

```text
.com
.es
.org
.net
```

El servidor TLD no proporciona necesariamente la dirección IP del equipo que buscamos. Su función es indicar cuáles son los **servidores DNS autoritativos** encargados del dominio correspondiente.

Por ejemplo, los servidores responsables del TLD `.es` pueden indicar qué servidores DNS son autoritativos para:

```text
aules.edu.gva.es
```

---

### 6.4 Consulta al servidor de nombres autoritativo

El resolver recursivo consulta finalmente a uno de los **servidores DNS autoritativos** responsables de la zona correspondiente.
![Descripción de la imagen](./img_5/img_5_9.png){.marco .margintop10}

Un servidor autoritativo dispone de la **información oficial de la zona DNS que administra**. Esta información contiene diferentes registros DNS que permiten conocer los servicios asociados a los nombres del dominio.

Por ejemplo, un registro **A** puede asociar un nombre con una dirección IPv4:

```text
www.aules.edu.gva.es  →  195.77.20.168
```

Para IPv6 se utiliza normalmente un registro **AAAA**.

Un dominio puede disponer de **varios servidores autoritativos**, proporcionando redundancia y disponibilidad.

---

### 6.5 Resolución final y almacenamiento en caché

El resolver recursivo recibe la respuesta del servidor autoritativo y se la proporciona al dispositivo que realizó la consulta.
![Descripción de la imagen](./img_5/img_5_6.png){.marco .margintop10}

El navegador ya puede utilizar la dirección IP obtenida para establecer una conexión con el servicio correspondiente.

Además, el resolver puede almacenar la respuesta en su **caché DNS** durante el tiempo indicado por el **TTL** del registro.

De esta forma, si otro dispositivo realiza posteriormente la misma consulta, el resolver puede responder utilizando la información almacenada en caché sin tener que volver a consultar a los servidores raíz, TLD y autoritativos.

---

### 6.6 Resumen del proceso

De forma simplificada, podemos representar la resolución de un nombre de dominio de la siguiente manera:

<!-- ```text
              Cliente
                 │
                 │ Consulta DNS
                 ▼
        ┌─────────────────┐
        │ DNS recursivo   │
        │    Resolver     │
        └────────┬────────┘
                 │
                 │ 1. Consulta
                 ▼
        ┌─────────────────┐
        │ Servidor raíz   │
        └────────┬────────┘
                 │
                 │ Indica el TLD
                 ▼
        ┌─────────────────┐
        │ Servidor TLD    │
        │     (.es)       │
        └────────┬────────┘
                 │
                 │ Indica los servidores
                 │ autoritativos
                 ▼
        ┌─────────────────────┐
        │ Servidor autoritativo│
        └──────────┬──────────┘
                   │
                   │ Registro A / AAAA
                   ▼
              Dirección IP
                   │
                   ▼
              DNS Resolver
                   │
                   ▼
                Cliente
``` -->

```mermaid
flowchart TD
    A[Cliente] -->|1. Consulta DNS| B[DNS recursivo<br/>Resolver]
    B -->|2-3. Consulta a servidor raíz | C[Servidor raíz]
    C -->|4-5. Consulta a servidor TLD| D["Servidor TLD<br/>(.es)"]
    D -->|6-7. Indica los servidores<br/>autoritativos| E[Servidor autoritativo]
    E -->|Registro A / AAAA| F[Dirección IP]
    F -->|192.0.2.1| G[DNS Resolver]
    G -->|8. Entrega de IP a cliente <br/>192.0.2.1| H[Cliente]
    H -->|192.0.2.1| I["Servidor (web)"]
```

!!! tip "Resumen de los que hemos visto"

    1. El **cliente no suele consultar directamente a los servidores raíz, TLD y autoritativos**. 
    1. Normalmente realiza una consulta a un **resolver DNS recursivo**, que se encarga de realizar las consultas necesarias y devolver finalmente la respuesta al cliente.
    1. Por tanto, debemos distinguir entre:

          | Servidor DNS                 | Función principal                                                 |
          | ---------------------------- | ----------------------------------------------------------------- |
          | **DNS recursivo (Resolver)** | Realiza la búsqueda en nombre del cliente y devuelve la respuesta |
          | **Servidor raíz (Root)**     | Indica qué servidores gestionan el TLD solicitado                 |
          | **Servidor TLD**             | Indica qué servidores son autoritativos para el dominio           |
          | **Servidor autoritativo**    | Proporciona la información oficial de la zona DNS                 |

    4. Esta jerarquía permite que el DNS sea un sistema **distribuido, escalable y resistente**, capaz de gestionar una enorme cantidad de  nombres de dominio sin depender de un único servidor central.

---

## 7 - Jerarquía de nombres DNS

El sistema DNS está organizado mediante una **estructura jerárquica**, similar a un árbol invertido. En la parte superior se encuentra la **raíz (`.`)** y, a medida que descendemos por la jerarquía, encontramos los diferentes dominios y subdominios.

Si tenemos el siguiente nombre:
![Descripción de la imagen](./img_5/img_5_11.png){.margintop10}

<!-- ```text
www.edu.gva.es
``` -->

Su estructura jerárquica sería:
![Descripción de la imagen](./img_5/img_5_12.png){.margintop10}

<!-- ```text
.
└── es
    └── gva
        └── edu
            └── www
``` -->

Cada nivel representa una parte diferente de la jerarquía DNS.

### 7.1 La raíz DNS

En la parte superior de la jerarquía se encuentra la **raíz DNS**, representada mediante un punto:

```text
.
```

La raíz es el nivel superior de todo el sistema DNS.

Un nombre de dominio completamente cualificado (*FQDN, Fully Qualified Domain Name*) podría escribirse de la siguiente manera:

![Descripción de la imagen](./img_5/img_5_11.png){.margintop10}

Normalmente este punto final no se escribe cuando utilizamos un nombre de dominio en un navegador pero forma parte de la estructura completa del nombre.
![Descripción de la imagen](./img_5/img_5_11.jpeg){.margintop10}

---

### 7.2 Dominios de nivel superior (TLD)

Por debajo de la raíz se encuentran los **dominios de nivel superior**, conocidos como **TLD (*Top-Level Domain*)**.

Algunos ejemplos son:

```text
.com
.org
.net
.es
.edu
```

Existen diferentes tipos de TLD. Por ejemplo:

- **gTLD (*generic Top-Level Domain*)**: `.com`, `.org`, `.net`, etc.
- **ccTLD (*country code Top-Level Domain*)**: `.es`, `.fr`, `.it`, `.de`, etc.

En el caso de:

```text
www.edu.gva.es
```

el TLD es:

```text
.es
```

---

### 7.3 Dominio

A la izquierda del TLD encontramos otros niveles de la jerarquía.

En el caso de:

```text
www.edu.gva.es
```

Un dominio dentro del TLD `.es` sería.

```text
gva.es
```

<!-- ![Descripción de la imagen](./img_5/img_5_10.jpeg){.marco .margintop10} -->

<!-- ```text
www . edu . gva . es
 │     │     │    │
 │     │     │    └── TLD
 │     │     └─────── Dominio
 │     └───────────── Subdominio
 └─────────────────── Nombre de host
``` -->

<!-- Es importante tener en cuenta que los términos **dominio** y **subdominio** dependen del nivel que estemos analizando.

Por ejemplo:

```text
gva.es
```

es un dominio dentro de `.es`.

A su vez:

```text
edu.gva.es
```

es un subdominio de `gva.es`.

Y:

```text
www.edu.gva.es
```

es un nombre situado dentro de `edu.gva.es`. -->

---

### 7.4 Subdominios

Un **subdominio** es un dominio que se encuentra por debajo de otro dominio dentro de la jerarquía DNS.

En el caso de:

```text
gva.es
```

podría tener diferentes subdominios:

```text
edu.gva.es
san.gva.es
just.gva.es
```

Y, a su vez, `edu.gva.es` podría tener otros niveles:

```text
www.edu.gva.es
moodle.edu.gva.es
correo.edu.gva.es
```

Los subdominios permiten organizar diferentes servicios, departamentos o recursos dentro de una misma estructura de nombres.

---

### 7.5 FQDN

Un **FQDN (*Fully Qualified Domain Name*)**, o **nombre de dominio completamente cualificado**, identifica de forma completa una posición dentro de la jerarquía DNS.

En el caso de tendríamos:

```text
www.edu.gva.es.
```


<!-- ```text
.          → raíz
es         → TLD
gva        → dominio
edu        → subdominio
www        → nombre situado dentro de edu.gva.es
``` -->

<!-- El FQDN permite identificar un nombre de manera inequívoca dentro de la jerarquía DNS. -->

!!! tip "Importante"
    Los nombres DNS se interpretan **de derecha a izquierda**.

### 7.6 Nombre de host

En una red, un **host** es un dispositivo o sistema que puede comunicarse mediante una red.

En DNS, un nombre como `www.edu.gva.es` puede utilizarse para identificar un servicio o un host.

Por ejemplo, podríamos tener:

```text
www.edu.gva.es
correo.edu.gva.es
ftp.edu.gva.es
```

Cada nombre podría estar asociado mediante DNS a una dirección IP diferente:

```text
www.edu.gva.es       → 192.168.1.10
correo.edu.gva.es    → 192.168.1.20
ftp.edu.gva.es       → 192.168.1.30
```

!!! warning "Importante"

    - Cada nombre DNS **no representa necesariamente un único equipo físico**.  
    - Un mismo servicio puede estar distribuido entre varios servidores y una misma dirección IP puede utilizarse para diferentes nombres.

---

### 7.7 Zona DNS

Una **zona DNS** es una parte de la jerarquía DNS que está administrada por una organización o servidor DNS determinado.

La zona contiene los **registros DNS** que proporcionan información sobre los nombres y servicios que administra.

Por ejemplo, una organización podría administrar la zona:

```text
edu.gva.es
```

y dentro de ella tener:

```text
www.edu.gva.es
correo.edu.gva.es
ftp.edu.gva.es
```

La zona podría contener registros como:

```text
www.edu.gva.es      → 192.168.10.10
correo.edu.gva.es   → 192.168.10.20
ftp.edu.gva.es      → 192.168.10.30
```

!!! warning "Dominio y zona no son exactamente lo mismo"

    1. Aunque en muchos ejemplos sencillos un dominio y una zona pueden parecer equivalentes, **dominio y zona son conceptos diferentes**.
    1. Un dominio representa una parte de la **jerarquía de nombres DNS**, mientras que una zona representa una parte de esa jerarquía que está **administrativamente gestionada mediante servidores DNS autoritativos**.
    1. Un dominio puede contener diferentes subdominios y estos pueden estar delegados en otras zonas.  
    En nuestro ejemplo:
    ```mermaid
    flowchart TD
        A[edu.gva.es] --> X((　))
        X --> B[Zona A]
        X --> C[Zona B]
        B --> D[www.edu.gva.es </br>+</br>correo.edu.gva.es]
        C --> E[ftp.edu.gva.es]
    style X fill:none,stroke:none
    ```
    La organización puede administrar directamente `edu.gva.es`, mientras que `www.edu.gva.es`, `correo.edu.gva.es` y `rrhh.empresa.es` pueden estar delegados en otros servidores DNS.

<!-- ```text
                empresa.es
                    │
          ┌─────────┴─────────┐
          │                   │
      ventas.empresa.es   rrhh.empresa.es
          │                   │
       Zona A                Zona B
``` -->

---

### 7.8 Resumen de la jerarquía DNS

Podemos resumir los diferentes conceptos mediante la siguiente imagen:

![Descripción de la imagen](./img_5/img_5_10.jpeg){.marco .margintop10}

De esta forma, el DNS organiza los nombres mediante una estructura jerárquica en la que cada nivel puede ser administrado de forma independiente.

| Concepto | Significado | Ejemplo |
||||
| **Raíz** | Nivel superior de la jerarquía DNS | `.` |
| **TLD** | Dominio de nivel superior | `.es` |
| **Dominio** | Nombre registrado dentro de un TLD | `gva.es` |
| **Subdominio** | Dominio situado dentro de otro dominio | `edu.gva.es` |
| **FQDN** | Nombre DNS completamente cualificado (incluye el punto raíz final) | `www.edu.gva.es.` |
| **Host** | Equipo o servicio identificado mediante un nombre | `www.edu.gva.es` |
| **Zona** | Parte de la jerarquía administrada por unos servidores autoritativos concretos | `edu.gva.es` (zona delegada, con sus propios servidores autoritativos dentro del dominio `gva.es`) |

## 8 - Servidores DNS públicos y privados

No todos los servidores DNS tienen la misma función ni están disponibles para los mismos usuarios. 

Dependiendo de quién pueda utilizarlos y de dónde se encuentren, podemos distinguir entre **servidores DNS públicos** y **servidores DNS privados**.

---

### 8.1 Servidores DNS públicos

Un **servidor DNS público** es un servidor DNS que ofrece su servicio de resolución de nombres a usuarios y dispositivos de Internet de forma pública.

Estos servidores suelen estar gestionados por empresas, organizaciones o proveedores de servicios de Internet y pueden ser utilizados por cualquier usuario que tenga acceso a Internet.

Algunos ejemplos conocidos son:

| Servicio DNS          | Dirección IPv4 |
| --------------------- | -------------- |
| **Google Public DNS** | `8.8.8.8`      |
| **Google Public DNS** | `8.8.4.4`      |
| **Cloudflare DNS**    | `1.1.1.1`      |
| **Cloudflare DNS**    | `1.0.0.1`      |
| **Quad9**             | `9.9.9.9`      |

Por ejemplo, podemos configurar un ordenador para que utilice:

```text
Servidor DNS preferido: 1.1.1.1
Servidor DNS alternativo: 1.0.0.1
```

A partir de ese momento, las consultas DNS realizadas por el dispositivo podrán enviarse a los servidores de Cloudflare.

!!! tip "Importante"
    - Un servidor DNS público **no significa que sea un servidor raíz ni un servidor autoritativo**.
    - Por ejemplo, `1.1.1.1` es un **resolver DNS recursivo público**. Recibe consultas de los clientes y, cuando es necesario, realiza las consultas correspondientes a otros servidores DNS de la jerarquía.

---

### 8.2 ¿Por qué utilizar un DNS público?

Existen diferentes motivos para utilizar un servidor DNS público en lugar del servidor DNS proporcionado automáticamente por nuestro proveedor de Internet.

#### 8.2.1 Rendimiento

Algunos proveedores de DNS público disponen de una infraestructura distribuida por diferentes partes del mundo. Esto permite que las consultas puedan ser atendidas desde servidores cercanos al usuario.

El tiempo necesario para obtener una respuesta DNS se denomina habitualmente **latencia DNS**.

Una menor latencia puede hacer que la resolución de nombres sea más rápida.

---

#### 8.2.2 Disponibilidad y redundancia

Los grandes proveedores de DNS público utilizan infraestructuras distribuidas y redundantes.

Si uno de sus servidores o centros de datos deja de funcionar, otros servidores pueden continuar atendiendo las consultas.

Esto proporciona una elevada **disponibilidad** del servicio.

---

#### 8.2.3 Seguridad

Algunos servicios DNS públicos incorporan mecanismos de seguridad adicionales, como el bloqueo de determinados dominios asociados a:

- Malware.
- Phishing.
- Botnets.
- Otros tipos de amenazas.

Por ejemplo, algunos resolvers públicos están diseñados específicamente para proporcionar una capa adicional de protección frente a determinados dominios maliciosos.

!!! warning "DNS y seguridad"
    - El uso de un DNS público **no garantiza por sí mismo que una conexión sea segura**.
    - DNS se encarga principalmente de resolver nombres. La seguridad de la comunicación dependerá también de otros mecanismos, como **HTTPS/TLS**, firewalls, sistemas de detección de intrusiones y otros controles de seguridad.

---

### 8.3 Servidores DNS privados

Un **servidor DNS privado** es un servidor DNS que está destinado a una organización, red o conjunto limitado de usuarios.

A diferencia de un servidor DNS público, no está pensado para que cualquier usuario de Internet pueda realizar consultas libremente.

Los servidores DNS privados son muy habituales en:

- Empresas.
- Centros educativos.
- Organismos públicos.
- Redes domésticas.
- Centros de datos.
- Redes virtuales en la nube.

!!! example "Ejemplo de red empresarial"
    ![Descripción de la imagen](./img_5/img_5_13.png){.marco .margintop10 .marginbottom10}
    **Dónde:**  

    - `10.0.0.0/24` es la red de la empresa.
    - `10.0.0.10` es el servidor DNS interno.
    - `10.0.0.20` es el servidor Web de la empresa.
    - `10.0.0.101` es un dispositivo conectado a la red (p.e.: impresora) con el nombre DNS **impresora.empresa.local**
    - `10.0.0.102` otro dispositivo conectado a la red (p.e.: nas) con el nombre DNS **nas.empresa.local** 
    
    !!! Warning "Estos nombres pueden (suelen) no existir en el DNS público de Internet"

---

### 8.4 DNS privado y acceso a Internet

Un servidor DNS privado no tiene por qué limitarse a resolver nombres internos.

También puede actuar como **resolver recursivo** para los dispositivos de la organización.

Si miramos el siguiente esquema veremos que el servidor DNS puede resolver tanto `servidor.empresa.local` utilizando sus **zonas internas** como `www.google.com`, `www.wikipedia.org` y `www.aules.edu.gva.es` realizando consultas recursivas hacia otros servidores DNS.

![Descripción de la imagen](./img_5/img_5_14.png){.marco .margintop10 .marginbottom10}

### 8.5 Servidor DNS privado en una red local

En una red local, los equipos suelen obtener automáticamente la dirección del servidor DNS mediante el protocolo **DHCP**.

!!! example "Configurción dee red devuelta por el servidor DHCP"
    ```text
    Configuración recibida mediante DHCP

    Dirección IP:       192.168.10.101
    Máscara:            255.255.255.0
    Puerta de enlace:   192.168.10.1
    Servidor DNS:       192.168.10.10
    ```

    **Dónde:**

    - El ordenador cliente recibe la IP `192.168.10.101`.
    - El ordenador cliente utilizará `192.168.10.10` para realizar consultas DNS.
    - El ordenador cliente utilizará `192.168.10.1` como puerta de enlace es decir para acceder a internet.
    - El servidor DNS privado podría resolver tanto nombres internos como nombres de Internet.

!!! example "Ejemplo de consulta DNS interna"
    ![Descripción de la imagen](./img_5/img_5_15.png){ .margintop10 .marginbottom10}

!!! example "Ejemplo de consulta DNS externa"
    ![Descripción de la imagen](./img_5/img_5_16.png){ .margintop10 .marginbottom10}

---

### 8.6 Comparativa DNS público vs. DNS privado

Podemos comparar ambos tipos de servidores:

| Característica           | DNS público                  | DNS privado                          |
| ------------------------ | ---------------------------- | ------------------------------------ |
| Acceso                   | Público                      | Restringido                          |
| Usuarios                 | Cualquier usuario            | Usuarios de una organización o red   |
| Uso habitual             | Resolver nombres de Internet | Resolver nombres internos y externos |
| Ejemplo                  | `1.1.1.1`                    | `192.168.10.10`                      |
| Administración           | Proveedor externo            | Organización                         |
| Nombres internos         | Normalmente no               | Sí                                   |
| Uso en empresas          | Posible                      | Muy habitual                         |
| Accesible desde Internet | Generalmente sí              | Normalmente no                       |

---

## 9 - Evolución del protocolo DNS y seguridad

El protocolo DNS ha evolucionado para adaptarse a las necesidades cada vez mayores de las redes y, especialmente, para solucionar algunos de sus problemas de seguridad.

Dos de las principales tecnologías relacionadas con esta evolución son **DDNS (Dynamic DNS)** y **DNSSEC (DNS Security Extensions)**.

### 9.1 DDNS

**El DDNS (Dynamic DNS o DNS dinámico)** permite actualizar automáticamente los registros de un servidor DNS cuando cambia la dirección IP asociada a un nombre de dominio.

Su principal utilidad es permitir que un dispositivo o servidor cuya dirección IP es **dinámica** pueda seguir siendo accesible mediante un nombre de dominio, aunque su dirección IP cambie.

!!! example "ejemplo"
    Imaginemos un servidor al que queremos acceder utilizando el nombre:

    ```text
    servidor.midominio.com
    ```

    Si el servidor tiene una dirección IP dinámica, esta podría cambiar periódicamente:

    ```text
    servidor.midominio.com → 80.25.10.100
    ```

    y posteriormente:

    ```text
    servidor.midominio.com → 80.25.15.200
    ```

    El servicio DDNS se encarga de actualizar el registro DNS para que el nombre continúe apuntando a la dirección IP actual.

    Un mecanismo habitual consiste en que un dispositivo o servicio con conocimiento del cambio de IP comunique la nueva dirección al servidor DNS para actualizar el registro correspondiente.

    En determinadas redes, el **servidor DHCP** puede participar en este proceso. Cuando asigna o modifica una dirección IP, puede actualizar también los registros DNS asociados. De esta forma, **DHCP y DNS pueden trabajar conjuntamente** para mantener actualizada la información de nombres y direcciones.

    !!! warning "Importante:"
        DDNS no es un protocolo DNS diferente. Es un mecanismo o servicio que permite realizar **actualizaciones dinámicas de los registros DNS**.

### 9.2 DNSSEC

**DNSSEC (Domain Name System Security Extensions o extensiones de seguridad para el DNS)** es un conjunto de extensiones que permite añadir **autenticidad e integridad** a la información proporcionada por DNS.

El funcionamiento tradicional de DNS presenta un problema: un atacante podría intentar proporcionar al cliente una respuesta DNS falsa. 

!!! example "Ejemplo"
    Ante una consulta como:

    ```text
    www.banco.com → ¿cuál es su dirección IP?
    ```

    un atacante podría intentar conseguir que el cliente recibiera una dirección IP incorrecta:

    ```text
    www.banco.com → 203.0.113.50
    ```

    DNSSEC utiliza **firmas digitales** para que el resolver DNS pueda comprobar que los datos recibidos son auténticos y que no han sido modificados.

    Por tanto, DNSSEC permite proteger principalmente:

    - **La autenticidad:** comprobar que los datos DNS proceden de la zona DNS que tiene autoridad sobre ellos.
    - **La integridad:** comprobar que los datos no han sido modificados durante su transmisión.

    !!! warning "Importante"
        
        - DNSSEC **no cifra** las consultas ni las respuestas DNS. Por tanto, no proporciona confidencialidad.
        - Tampoco garantiza por sí mismo que el usuario esté conectado directamente con su servidor DNS real. Su objetivo es permitir que el resolver pueda **validar criptográficamente la autenticidad de los datos DNS recibidos**.

    !!! warning "Importante"
        
        - DNSSEC protege la información DNS, pero **no protege la disponibilidad del servicio**. Por tanto, no evita los ataques de denegación de servicio (DoS o DDoS).  
        - Además, las respuestas DNSSEC suelen ser de mayor tamaño debido a la información criptográfica que contienen. Esto puede contribuir a que determinadas configuraciones de DNS sean utilizadas en **ataques de amplificación DNS**, aunque DNSSEC no sea la causa de estos ataques.

    !!! note "En resumen"
        DNSSEC proporciona **autenticidad e integridad**, pero no **confidencialidad ni disponibilidad**.

### 9.3 Envenenamiento de la caché DNS

Uno de los principales problemas de seguridad del DNS tradicional es que, si un atacante consigue introducir información DNS falsa en la caché de un servidor DNS, puede conseguir que las consultas de los usuarios sean redirigidas a direcciones IP incorrectas.

Este ataque se conoce como **DNS cache poisoning o envenenamiento de la caché DNS**.

!!! example "Ejemplo"
    Un usuario quiere acceder a la web de su banco:

    ```text
    www.banco.com
    ```
    Normalmente, el servidor DNS debería proporcionar la dirección IP legítima:
    ```text
    www.banco.com → 198.51.100.20
    ```
    Sin embargo, si un atacante consigue introducir un registro falso en la caché DNS:
    ```text
    www.banco.com → 203.0.113.50
    ```

    Los usuarios que reciban esa respuesta podrían ser enviados a un servidor controlado por el atacante.

    El objetivo podría ser mostrar una página web falsa que imite a la original para intentar obtener **credenciales de acceso, datos personales u otra información confidencial**.

    Este tipo de ataque puede utilizarse, por ejemplo, como parte de una campaña de **phishing**.

    !!! success "Prevención contra el dead cache poisoning" 
        DNSSEC ayuda a prevenir el problema del ataque por "dead cache poisoning" porque permite al resolver DNS comprobar mediante firmas digitales que los registros DNS recibidos son auténticos y no han sido modificados.

    !!! warning "Importante"
        - No debemos confundir el **envenenamiento de la caché DNS** con el hecho de que un servidor DNS haya sido comprometido. 
        - En el primer caso, el atacante intenta introducir información DNS falsa en la caché de un resolver; en el segundo, el propio servidor DNS puede haber sido tomado bajo control por el atacante.

### 9.4 Ataques Man-in-the-Middle

Un ataque **Man-in-the-Middle (MITM)**, o **hombre en el medio**, se produce cuando un atacante consigue situarse entre dos dispositivos que se están comunicando.

!!! example "Ejemplo"
    Imaginemos que un usuario cree estar comunicándose directamente con el servidor de su banco:
    ```text
    Cliente --→ Banco
    ```

    En un ataque MITM, el atacante intenta situarse entre ambos:
    ```text
    Cliente --→ Atacante --→ Banco
    Cliente ←-- Atacante ←-- Banco
    ```

    El atacante puede recibir el tráfico, analizarlo y, dependiendo de las circunstancias y de las protecciones utilizadas, intentar modificarlo antes de reenviarlo.

    !!! warning "Importante"
        - Un ataque MITM no es específico de DNS. **Puede producirse en diferentes tipos de comunicaciones de red**. 
        - Además, utilizar DNSSEC no sustituye a mecanismos como **HTTPS/TLS**, que son los encargados de proteger la comunicación entre el navegador y el servidor web.

## 10 - Registros DNS

### 10.1 Introducción

- Los **registros DNS** son datos que contienen información sobre los nombres de dominio y los servicios asociados a ellos. 

    !!! example "Ejemplo"
        Un registro de tipo **A** permite asociar un nombre de dominio con **una dirección IPv4**:

        ```text
        www.ejemplo.com → 192.0.2.10
        ```

- En los **servidores DNS autoritativos**, estos registros pueden almacenarse en **archivos de zona**. Un archivo de zona es un archivo de texto que contiene los registros DNS y determinadas directivas que describen una zona DNS.

    !!! example "Ejemplo"
        Un archivo de zona puede contener registros como:

        ```text
        ejemplo.com.      IN    A       192.0.2.10
        www               IN    A       192.0.2.10
        mail              IN    A       192.0.2.20
        ```

- La **sintaxis de los archivos de zona** establece cómo deben escribirse estos registros y directivas para que el servidor DNS pueda interpretarlos correctamente.

    !!! example "Ejemplo"
        Cuando un usuario introduce en su navegador una dirección como:

        ```text
        https://www.ejemplo.com/index.html
        ```

        el navegador necesita conocer la dirección IP asociada al nombre de host **[www.ejemplo.com](http://www.ejemplo.com)**. Para obtenerla, se inicia una **consulta DNS**.

        El equipo del usuario normalmente realiza la consulta a un **servidor DNS recursivo** o *resolver*. Este servidor puede disponer de la respuesta en su **caché**. Si no la tiene, puede realizar consultas a otros servidores DNS hasta encontrar la información necesaria.

- En una resolución DNS pueden intervenir diferentes tipos de servidores, entre ellos:

    - **Servidores DNS recursivos:** reciben las consultas de los clientes y se encargan de obtener la respuesta.
    - **Servidores DNS raíz:** indican qué servidores son responsables de los diferentes dominios de nivel superior (*Top-Level Domains* o  TLD), como `.com`, `.org` o `.es`.
    - **Servidores DNS de TLD:** indican cuáles son los servidores autoritativos responsables de un dominio concreto.
    - **Servidores DNS autoritativos:** contienen la información oficial de una zona DNS y proporcionan los registros correspondientes.

### 10.2 TTL (Time To Live)

- Los registros DNS incluyen un valor denominado **TTL (Time To Live)**.
- El TTL indica **durante cuánto tiempo puede mantenerse un registro DNS en la caché de un servidor DNS recursivo antes de que deba volver a consultarse**.

    !!! example "Ejemplo"
        Si un registro tiene:

        ```text
        www.ejemplo.com.    3600    IN    A    192.0.2.10
        ```

        el valor `3600` representa un TTL de **3600 segundos**, es decir, **1 hora**.

        Durante ese periodo, un servidor DNS recursivo puede utilizar la información almacenada en su caché sin tener que volver a consultar al servidor autoritativo.

        !!! warning "Importante" 
            el TTL **no indica cada cuánto tiempo se actualiza el registro en el servidor DNS autoritativo**. Indica cuánto tiempo otros servidores pueden conservar ese registro en su caché.

### 10.3 Tipos de Registros DNS

#### 10.3.1 Registro A (Address)

- Los registros de direcciones, o registros A, son los registros DNS más utilizados. Crean una conexión directa entre **una dirección IPv4** y un nombre de dominio.
- Permiten que un navegador web cargue un sitio utilizando un nombre de dominio legible, evitando que el usuario tenga que recordar complejas direcciones IP numéricas.
- Redundancia: Es posible configurar múltiples registros A para un mismo dominio, lo que proporciona respaldo y redundancia en caso de fallos.
- Seguridad: Se utiliza también en listas negras basadas en DNS (DNSBL) para bloquear correos provenientes de fuentes de spam conocidas.

!!! tip "Sintaxis típica"
    midominio.com. IN A 192.0.2.15.

#### 10.3.2 Registro AAAA (Quad A)

Funciona de manera similar al registro A, pero conecta nombres de dominio **con direcciones IPv6**.
Aunque menos común que IPv4, su adopción global va en aumento para resolver el problema del agotamiento de las direcciones IPv4 tradicionales.

!!! tip "Sintaxis típica"
    midominio.net. IN AAAA 2001:0db8:85a3:0000:0000:8a2e:0370:1234

#### 10.3.3 Registro CNAME (Canonical Name)

Los registros de nombres canónicos, o registros CNAME, dirigen un dominio de alias a un dominio canónico. 
Los registros CNAME se usan a menudo para asignar un nombre de dominio con un alias al dominio principal que lleva el registro A o AAAA.

!!! example "Ejemplo"

    - En lugar de crear dos registros A para `www.example.com` y `product.example.com`, puede vincular `product.example.com` a un **registro CNAME** que luego se **vincula a un registro A** para `example.com`.
    - El valor es que si la dirección IP cambia para el dominio raíz, solo se tendrá que actualizar el registro A y el CNAME se actualizará en consecuencia.
    - Restricciones de configuración:
        - No se puede ubicar un registro CNAME en el dominio de raíz.
        - Los registros de servidores de correo (MX) y servidores de nombres (NS) nunca deben estar dirigidos a un CNAME.
        - Aunque técnicamente es posible apuntar un CNAME a otro CNAME, esta práctica no se recomienda porque resulta ineficaz y ralentiza la velocidad de carga.

#### 10.3.4 Registro DNAME

Los registros de nombres de delegación, o registros DNAME, se utilizan para redirigir varios subdominios con un registro y apuntarlos a otro dominio.

!!! example "Ejemplo"

    - Un registro DNAME que vincule `domain.com` a `example.com` vinculará `product.domain.com`, `trial.domain.com`, y `blog.domain.com` a `example.com`. 
    - Estos registros son útiles para administrar dominios a gran escala y para administrar cambios de nombres de dominio al garantizar que los subdominios estén vinculados correctamente.

#### 10.3.5 Registros CAA

Los registros de autorización de autoridad de certificación, o registros CAA, permiten a los propietarios de dominios especificar qué **autoridades de certificación (CA)** pueden emitir certificados para su dominio.

Una CA es una organización que valida la identidad de los sitios web y los conecta a claves criptográficas mediante la emisión de certificados digitales.

#### 10.3.5 Registro NS (Nameserver)

- Especifica qué servidor de nombres o servidor DNS en particular actúa como la autoridad autoritativa para un dominio o subdominio.

!!! warning "Importante"
    - El registro NS indica qué servidor **alberga físicamente los archivos de zona del dominio**. 
    - Sin un registro NS debidamente configurado, es imposible cargar o acceder a un sitio web.

#### 10.3.5 Registro MX (Mail Exchange)

Los registros MX son indispensables para la recepción de correos electrónicos bajo el nombre de dominio.

Indica cuáles son los servidores de correo autorizados para recibir los mensajes mediante el protocolo SMTP.

!!! example "Sintaxis típica"
    midominio.com. IN MX 10 mail.midominio.com..

#### 10.3.6 Registro TXT

Permite que un administrador pueda almacenar notas de texto en el registro. Estos registros se suelen utilizar para la seguridad del correo electrónico.

#### 10.3.7 Registros CERT

Los certificados, o registros CERT, almacenan certificados que verifican la autenticidad de todas las partes involucradas.  

Este tipo de registro es particularmente valioso cuando se protege y encripta información confidencial.

#### 10.3.8 Registros SOA

Los registros de inicio de autoridad, o registros SOA, almacenan información administrativa importante sobre un dominio. Esta información puede incluir la dirección de correo electrónico del administrador del dominio, información sobre las actualizaciones del dominio y cuándo un servidor debe actualizar su información.

#### 10.3.9 Registros PTR

Los registros de puntero, o registros PTR, funcionan en la dirección opuesta a los registros A. Se utilizan para **conectar una dirección IP con un nombre de dominio, en lugar de un nombre de dominio con una dirección IP**.

Cuando una búsqueda de DNS comienza con una dirección IP, encuentra el nombre de host correspondiente. Estos registros se utilizan para detectar spam comprobando si las direcciones IP y las direcciones de correo electrónico asociadas son utilizadas por servidores de correo electrónico legítimos. El host del servidor debe configurar los registros PTR.

## 11 - Herramientas de Diagnóstico Técnico de Registros DNS

Para verificar y solucionar problemas con las zonas DNS, los administradores de sistemas y profesionales de redes emplean herramientas de terminal populares:

!!! tip "nslookup"
    Permite consultar de forma rápida la dirección IP asociada a un dominio y ver registros básicos como A, MX o NS.

!!! tip "dig (Domain Information Groper)"
    dig (Domain Information Groper): Ofrece información mucho más profunda y detallada sobre las consultas DNS, incluyendo los tiempos de respuesta del servidor y la jerarquía de autoridad.


<!-- # hasta aqui

https://www.cloudflare.com/es-es/learning/dns/dns-records/
https://www.ibm.com/es-es/think/topics/dns-records
https://www.site24x7.com/es/learn/dns-record-types.html
https://blog.infranetworking.com/registros-dns-que-son-y-cuales-tipos-hay/
https://www.digicert.com/es/faq/dns/what-are-dns-records
https://www.webempresa.com/blog/que-es-un-registro-dns-y-que-tipos-hay.html
https://easydmarc.com/blog/es/8-tipos-comunes-de-registros-dns/


# hasta aqui -->

<!-- https://notebook.google.com/notebook/3ba0b1e5-23cc-414c-a66b-1591bdf88c4a -->

<!-- PAJA -->
<!-- https://sri.codeandcoke.com/doku.php?id=sri:t2
https://ioc.xtec.cat/materials/FP/Recursos/fp_smx_m07_/web/fp_smx_m07_htmlindex/WebContent/u1/a2/continguts.html
https://serviciosgm.readthedocs.io/es/latest/windows/dns/index.html
http://127.0.0.1:5500/docs/SMX/SMX_2/SX/sxe/UD02/2._Servei_DNS/1_introducci.html
https://www.youtube.com/watch?v=TwMAS7Iha30
https://asir.readthedocs.io/es/latest/Tema_3_DNS/Index.html -->
<!-- file:///C:/Users/titan/Documents/GitHub/githubpages/Apuntes/docs/SMX/SMX_2/SX/admin/recursos/tema3dns.pdf -->
<!-- https://www.youtube.com/watch?v=EfSbT3gJUFY&t=47s -->

<!-- para nat -->
<!-- tipo de elementos de red -->
<!-- https://itadmins.es/networking-ii-dispositivos-de-red-y-tipos-de-trafico/ -->

<!-- # NAT -->
<!-- https://www.manageengine.com/latam/oputils/direcciones-ip-fundamentos.html
https://www.redeszone.net/tutoriales/redes-cable/calcular-subnetting-ip-red-mascara-subred-ipv4/
https://www.1nce.com/es-es/recursos/iot-knowledge-base/que-es-el-mecanismo-nat
https://openwebinars.net/blog/nat-que-es-y-para-que-sirve/
-->

<!-- https://www.webempresa.com/blog/servidor-dns-como-solucionar-problemas-habituales.html -->
<!-- https://www.dreamhost.com/blog/es/nameservers-vs-dns-guia/ -->

<!-- pracrica DNS -->
<!-- # Práctica - Instalación y configuración de un servidor DNS con BIND9 en AWS

## 1 - Objetivos

En esta práctica crearemos una pequeña red dentro de **Amazon Web Services (AWS)** formada por tres instancias EC2.

Una de las instancias actuará como **servidor DNS** utilizando BIND9 y las otras dos actuarán como clientes.

Configuraremos:

* Una VPC propia.
* Dos subredes.
* Una puerta de enlace a Internet.
* Una tabla de enrutamiento.
* Grupos de seguridad.
* Tres instancias EC2 con Ubuntu Server.
* Un servidor DNS BIND9.
* Una zona DNS directa.
* Dos zonas DNS inversas.
* Registros A, CNAME, NS, SOA y PTR.
* Resolución DNS desde los clientes.
* Reenvío de consultas DNS hacia Internet.

Al finalizar la práctica tendremos una arquitectura similar a:

```text
                            INTERNET
                                │
                                │
                      ┌─────────▼─────────┐
                      │ Internet Gateway │
                      └─────────┬─────────┘
                                │
                    VPC: 10.0.0.0/16
                                │
               ┌────────────────┴────────────────┐
               │                                 │
     Subred servidores                    Subred clientes
      10.0.1.0/24                          10.0.2.0/24
               │                                 │
       ┌───────▼────────┐             ┌──────────┴──────────┐
       │   DNS-SERVER   │             │                     │
       │ Ubuntu Server  │      ┌──────▼──────┐       ┌──────▼──────┐
       │     BIND9      │      │  CLIENTE-1  │       │  CLIENTE-2  │
       │   10.0.1.10    │      │ 10.0.2.10   │       │ 10.0.2.20   │
       └────────────────┘      └─────────────┘       └─────────────┘
```

Utilizaremos el dominio:

```text
smr.test
```

Por tanto:

```text
dns.smr.test       → 10.0.1.10
cliente1.smr.test  → 10.0.2.10
cliente2.smr.test  → 10.0.2.20
```

!!! note "¿Por qué utilizamos smr.test?"

```
Para una práctica es preferible utilizar un dominio reservado para pruebas como `.test`.

No utilizaremos `.local`, ya que este sufijo tiene un significado especial relacionado con **mDNS (Multicast DNS)** y puede provocar resultados inesperados en algunos sistemas operativos.
```

---

# 2 - Creación de la VPC

Accedemos a:

```text
VPC → Your VPCs → Create VPC
```

Creamos:

```text
Name:           VPC-DNS-SMR
IPv4 CIDR:      10.0.0.0/16
Tenancy:        Default
```

Nuestra red completa será:

```text
10.0.0.0/16
```

Esto nos proporciona direcciones desde:

```text
10.0.0.0
```

hasta:

```text
10.0.255.255
```

---

# 3 - Creación de las subredes

Crearemos dos subredes dentro de la VPC.

## 3.1 Subred de servidores

Accedemos a:

```text
VPC → Subnets → Create subnet
```

Seleccionamos:

```text
VPC-DNS-SMR
```

y configuramos:

```text
Subnet name:        SUBNET-SERVIDORES
IPv4 subnet CIDR:   10.0.1.0/24
```

## 3.2 Subred de clientes

Creamos una segunda subred:

```text
Subnet name:        SUBNET-CLIENTES
IPv4 subnet CIDR:   10.0.2.0/24
```

Nuestra arquitectura queda:

```text
VPC
10.0.0.0/16

├── SUBNET-SERVIDORES
│   10.0.1.0/24
│
└── SUBNET-CLIENTES
    10.0.2.0/24
```

!!! note "Direcciones reservadas por AWS"

```
AWS reserva determinadas direcciones dentro de cada subred.

Por esta razón utilizaremos direcciones como `.10` y `.20` para nuestras máquinas.
```

---

# 4 - Crear un Internet Gateway

Para poder acceder a Internet desde las máquinas necesitaremos una puerta de enlace de Internet.

Accedemos a:

```text
VPC → Internet Gateways → Create Internet Gateway
```

Nombre:

```text
IGW-DNS-SMR
```

Después seleccionamos:

```text
Actions → Attach to a VPC
```

y escogemos:

```text
VPC-DNS-SMR
```

---

# 5 - Configuración de la tabla de rutas

Accedemos a:

```text
VPC → Route Tables
```

Creamos una tabla:

```text
Name:       RT-DNS-SMR
VPC:        VPC-DNS-SMR
```

Añadimos la siguiente ruta:

```text
Destination       Target
────────────────────────────────
10.0.0.0/16       local
0.0.0.0/0         IGW-DNS-SMR
```

Posteriormente asociamos las dos subredes:

```text
SUBNET-SERVIDORES
SUBNET-CLIENTES
```

a esta tabla de rutas.

Las dos serán, por tanto, **subredes públicas**.

---

# 6 - Creación de los grupos de seguridad

Crearemos dos grupos de seguridad.

## 6.1 Grupo de seguridad de los clientes

Creamos:

```text
Name: SG-CLIENTES
VPC:  VPC-DNS-SMR
```

Reglas de entrada:

```text
Tipo        Puerto      Origen
────────────────────────────────────────────
SSH         TCP 22      My IP
ICMP        ---         10.0.0.0/16
```

!!! warning "SSH"

````
Para SSH utilizaremos **My IP** en lugar de abrir el puerto 22 a:

```text
0.0.0.0/0
```

De esta forma reducimos la exposición de nuestras instancias a Internet.
````

Dejaremos permitidas las conexiones salientes.

## 6.2 Grupo de seguridad del servidor DNS

Creamos:

```text
Name: SG-DNS
VPC:  VPC-DNS-SMR
```

Reglas de entrada:

```text
Tipo          Protocolo     Puerto      Origen
────────────────────────────────────────────────────
SSH           TCP           22          My IP
DNS           UDP           53          SG-CLIENTES
DNS           TCP           53          SG-CLIENTES
ICMP          ICMP          ---         10.0.0.0/16
```

!!! warning "UDP y TCP"

```
DNS utiliza principalmente **UDP 53**, pero también puede utilizar **TCP 53**.

Por tanto, debemos permitir ambos protocolos.
```

No es necesario permitir DNS desde:

```text
0.0.0.0/0
```

Nuestro servidor DNS será exclusivamente para los equipos de nuestra red privada.

---

# 7 - Creación del servidor DNS

Accedemos a:

```text
EC2 → Instances → Launch instance
```

Configuramos:

```text
Name: DNS-SERVER
```

Seleccionamos una imagen:

```text
Ubuntu Server 24.04 LTS
```

Seleccionamos un tipo de instancia pequeño disponible en AWS Academy, por ejemplo:

```text
t2.micro
```

o:

```text
t3.micro
```

dependiendo de las opciones disponibles en el laboratorio.

Seleccionamos nuestra clave SSH.

En configuración de red:

```text
VPC:                VPC-DNS-SMR
Subnet:             SUBNET-SERVIDORES
Auto-assign public IP: Enable
Security Group:     SG-DNS
```

Configuramos manualmente como dirección IPv4 privada:

```text
10.0.1.10
```

!!! warning "Dirección privada"

````
Es importante que el servidor DNS mantenga siempre la misma dirección IP privada.

Si los clientes tienen configurado:

```text
DNS = 10.0.1.10
```

el servicio dejaría de funcionar si cambiara la dirección del servidor.
````

---

# 8 - Creación de CLIENTE-1

Creamos otra instancia:

```text
Name: CLIENTE-1

Sistema:
Ubuntu Server 24.04 LTS

VPC:
VPC-DNS-SMR

Subnet:
SUBNET-CLIENTES

Private IPv4:
10.0.2.10

Public IPv4:
Enable

Security Group:
SG-CLIENTES
```

---

# 9 - Creación de CLIENTE-2

Creamos:

```text
Name: CLIENTE-2

Sistema:
Ubuntu Server 24.04 LTS

VPC:
VPC-DNS-SMR

Subnet:
SUBNET-CLIENTES

Private IPv4:
10.0.2.20

Public IPv4:
Enable

Security Group:
SG-CLIENTES
```

Al finalizar tendremos:

| Máquina    | Dirección privada | Función        |
| ---------- | ----------------: | -------------- |
| DNS-SERVER |       `10.0.1.10` | Servidor BIND9 |
| CLIENTE-1  |       `10.0.2.10` | Cliente DNS    |
| CLIENTE-2  |       `10.0.2.20` | Cliente DNS    |

---

# 10 - Comprobar la conectividad

Nos conectamos mediante SSH a las máquinas.

Desde CLIENTE-1 comprobamos:

```bash
ping -c 4 10.0.1.10
```

También:

```bash
ping -c 4 10.0.2.20
```

Desde CLIENTE-2:

```bash
ping -c 4 10.0.1.10
```

Si funciona, disponemos de comunicación entre las instancias.

!!! question "¿Por qué pueden comunicarse si están en subredes diferentes?"

````
Las dos subredes pertenecen a:

```text
10.0.0.0/16
```

y la tabla de rutas de la VPC dispone automáticamente de una ruta:

```text
10.0.0.0/16 → local
```

que permite la comunicación entre las subredes de la VPC, siempre que los grupos de seguridad y ACL lo permitan.
````

---

# 11 - Instalar BIND9

Nos conectamos a:

```text
DNS-SERVER
```

Actualizamos los repositorios:

```bash
sudo apt update
```

Instalamos BIND9:

```bash
sudo apt install bind9 bind9-utils dnsutils -y
```

Comprobamos el servicio:

```bash
sudo systemctl status named
```

Podemos comprobar que escucha en el puerto 53:

```bash
sudo ss -lntup | grep :53
```

---

# 12 - Configuración general de BIND9

Editamos:

```bash
sudo nano /etc/bind/named.conf.options
```

Configuramos:

```text
options {
        directory "/var/cache/bind";

        recursion yes;

        allow-query {
                localhost;
                10.0.0.0/16;
        };

        allow-recursion {
                localhost;
                10.0.0.0/16;
        };

        listen-on {
                127.0.0.1;
                10.0.1.10;
        };

        listen-on-v6 { none; };

        forwarders {
                10.0.0.2;
        };

        dnssec-validation auto;
};
```

Guardamos el archivo.

!!! info "Forwarders"

````
Nuestro servidor será autoritativo para:

```text
smr.test
```

pero no conoce todos los dominios de Internet.

Cuando un cliente pregunte por:

```text
www.google.com
```

BIND9 reenviará la consulta al resolver DNS proporcionado por AWS:

```text
10.0.0.2
```
````

El proceso será:

```text
CLIENTE-1
     │
     │ www.google.com
     ▼
DNS-SERVER
10.0.1.10
     │
     │ no pertenece a smr.test
     ▼
DNS AWS
10.0.0.2
     │
     ▼
Internet
```

---

# 13 - Declarar la zona directa

Editamos:

```bash
sudo nano /etc/bind/named.conf.local
```

Añadimos:

```text
zone "smr.test" {
        type master;
        file "/etc/bind/db.smr.test";
        allow-update { none; };
};
```

Ahora debemos crear el archivo de zona.

---

# 14 - Crear la zona directa

Creamos:

```bash
sudo nano /etc/bind/db.smr.test
```

Introducimos:

```text
$TTL 300

@       IN      SOA     dns.smr.test. admin.smr.test. (
                        2026090201      ; Serial
                        3600            ; Refresh
                        600             ; Retry
                        86400           ; Expire
                        300             ; Negative Cache TTL
)

@               IN      NS      dns.smr.test.

dns             IN      A       10.0.1.10
cliente1        IN      A       10.0.2.10
cliente2        IN      A       10.0.2.20

www             IN      CNAME   cliente1
```

Tenemos los siguientes registros:

```text
dns.smr.test       → 10.0.1.10
cliente1.smr.test  → 10.0.2.10
cliente2.smr.test  → 10.0.2.20
www.smr.test       → cliente1.smr.test
```

!!! info "El punto final"

````
En nombres completos (*Fully Qualified Domain Names* o FQDN) veremos frecuentemente:

```text
dns.smr.test.
```

El punto final representa la raíz del espacio de nombres DNS.
````

---

# 15 - Comprobar la zona directa

Antes de reiniciar BIND debemos comprobar la configuración.

Ejecutamos:

```bash
sudo named-checkconf
```

Si todo es correcto no aparecerá ningún mensaje.

Comprobamos después la zona:

```bash
sudo named-checkzone smr.test /etc/bind/db.smr.test
```

Deberíamos obtener algo similar a:

```text
zone smr.test/IN: loaded serial 2026090201
OK
```

!!! warning "Muy importante"

````
Siempre que modifiquemos el archivo de zona debemos incrementar el valor:

```text
Serial
```

Por ejemplo:

```text
2026090201
2026090202
2026090203
```
````

---

# 16 - Reiniciar BIND9

Ejecutamos:

```bash
sudo systemctl restart named
```

Comprobamos:

```bash
sudo systemctl status named
```

También podemos utilizar:

```bash
sudo journalctl -u named -n 50 --no-pager
```

para consultar los últimos mensajes del servicio.

---

# 17 - Probar el servidor DNS localmente

Desde DNS-SERVER ejecutamos:

```bash
dig @127.0.0.1 cliente1.smr.test
```

También:

```bash
dig @10.0.1.10 cliente1.smr.test
```

Debemos encontrar:

```text
ANSWER SECTION:

cliente1.smr.test.  300  IN  A  10.0.2.10
```

Probamos:

```bash
dig @10.0.1.10 cliente2.smr.test
```

Resultado:

```text
cliente2.smr.test.  300  IN  A  10.0.2.20
```

Probamos el CNAME:

```bash
dig @10.0.1.10 www.smr.test
```

También podemos utilizar:

```bash
nslookup cliente1.smr.test 10.0.1.10
```

---

# 18 - Comprobar la resolución de Internet

Nuestro servidor DNS también debe ser capaz de resolver nombres externos.

Probamos:

```bash
dig @10.0.1.10 www.google.com
```

Si obtenemos una respuesta, significa que:

```text
BIND9 → 10.0.0.2 → Internet
```

está funcionando correctamente.

---

# 19 - Configurar la resolución inversa

Hasta ahora podemos hacer:

```text
cliente1.smr.test → 10.0.2.10
```

Queremos ahora conseguir también:

```text
10.0.2.10 → cliente1.smr.test
```

Para ello utilizaremos registros **PTR**.

Tenemos dos redes:

```text
10.0.1.0/24
10.0.2.0/24
```

Crearemos una zona inversa para cada una.

---

# 20 - Declarar las zonas inversas

Editamos:

```bash
sudo nano /etc/bind/named.conf.local
```

El archivo completo quedará:

```text
zone "smr.test" {
        type master;
        file "/etc/bind/db.smr.test";
        allow-update { none; };
};

zone "1.0.10.in-addr.arpa" {
        type master;
        file "/etc/bind/db.10.0.1";
        allow-update { none; };
};

zone "2.0.10.in-addr.arpa" {
        type master;
        file "/etc/bind/db.10.0.2";
        allow-update { none; };
};
```

!!! question "¿Por qué 2.0.10?"

````
Para la red:

```text
10.0.2.0/24
```

DNS utiliza el dominio especial:

```text
in-addr.arpa
```

y escribe los octetos de la red en orden inverso:

```text
10.0.2
    ↓
2.0.10
    ↓
2.0.10.in-addr.arpa
```
````

---

# 21 - Zona inversa de 10.0.1.0/24

Creamos:

```bash
sudo nano /etc/bind/db.10.0.1
```

Introducimos:

```text
$TTL 300

@       IN      SOA     dns.smr.test. admin.smr.test. (
                        2026090201
                        3600
                        600
                        86400
                        300
)

@       IN      NS      dns.smr.test.

10      IN      PTR     dns.smr.test.
```

Esto establece:

```text
10.0.1.10 → dns.smr.test
```

---

# 22 - Zona inversa de 10.0.2.0/24

Creamos:

```bash
sudo nano /etc/bind/db.10.0.2
```

Introducimos:

```text
$TTL 300

@       IN      SOA     dns.smr.test. admin.smr.test. (
                        2026090201
                        3600
                        600
                        86400
                        300
)

@       IN      NS      dns.smr.test.

10      IN      PTR     cliente1.smr.test.
20      IN      PTR     cliente2.smr.test.
```

Ahora:

```text
10.0.2.10 → cliente1.smr.test
10.0.2.20 → cliente2.smr.test
```

---

# 23 - Comprobar las zonas inversas

Comprobamos:

```bash
sudo named-checkconf
```

Después:

```bash
sudo named-checkzone 1.0.10.in-addr.arpa /etc/bind/db.10.0.1
```

y:

```bash
sudo named-checkzone 2.0.10.in-addr.arpa /etc/bind/db.10.0.2
```

Si todo es correcto aparecerá:

```text
OK
```

Reiniciamos:

```bash
sudo systemctl restart named
```

---

# 24 - Probar la resolución inversa

Ejecutamos:

```bash
dig @10.0.1.10 -x 10.0.1.10
```

Deberíamos obtener:

```text
10.1.0.10.in-addr.arpa.  IN PTR dns.smr.test.
```

Probamos CLIENTE-1:

```bash
dig @10.0.1.10 -x 10.0.2.10
```

Resultado esperado:

```text
10.2.0.10.in-addr.arpa.  IN PTR cliente1.smr.test.
```

Probamos CLIENTE-2:

```bash
dig @10.0.1.10 -x 10.0.2.20
```

Resultado:

```text
20.2.0.10.in-addr.arpa.  IN PTR cliente2.smr.test.
```

---

# 25 - Configurar los clientes para utilizar nuestro DNS

Hasta este momento hemos realizado consultas indicando explícitamente:

```bash
dig @10.0.1.10 cliente1.smr.test
```

Queremos que los clientes utilicen automáticamente:

```text
10.0.1.10
```

como su servidor DNS.

En AWS podemos hacerlo mediante un **DHCP Options Set**.

Accedemos a:

```text
VPC → DHCP option sets → Create DHCP options set
```

Configuramos:

```text
Name:
DHCP-DNS-SMR
```

Como nombre de dominio:

```text
smr.test
```

Como servidor DNS:

```text
10.0.1.10
```

!!! warning "Importante"

````
No debemos escribir aquí:

```text
AmazonProvidedDNS
```

junto con nuestro servidor.

Queremos que las máquinas consulten directamente a:

```text
10.0.1.10
```

BIND9 será quien reenvíe las consultas externas al resolver de AWS.
````

---

# 26 - Asociar el DHCP Options Set a la VPC

Accedemos a:

```text
VPC → Your VPCs
```

Seleccionamos:

```text
VPC-DNS-SMR
```

Después:

```text
Actions → Edit VPC settings
```

En:

```text
DHCP options set
```

seleccionamos:

```text
DHCP-DNS-SMR
```

Guardamos los cambios.

La arquitectura DNS pasa a ser:

```text
                     VPC
                 10.0.0.0/16
                       │
                DHCP de AWS
                       │
        entrega DNS = 10.0.1.10
                       │
             ┌─────────┴──────────┐
             │                    │
        CLIENTE-1            CLIENTE-2
        10.0.2.10            10.0.2.20
             │                    │
             └─────────┬──────────┘
                       │
                       ▼
                 DNS-SERVER
                  10.0.1.10
                       │
           ┌───────────┴────────────┐
           │                        │
       smr.test                otros dominios
           │                        │
     responde BIND              forwarder
                                    │
                                    ▼
                               10.0.0.2
                               DNS de AWS
```

---

# 27 - Actualizar la configuración de los clientes

Los cambios de las opciones DHCP no tienen por qué aparecer inmediatamente en una instancia que ya está funcionando.

En una práctica podemos reiniciar CLIENTE-1 y CLIENTE-2 para que vuelvan a obtener su configuración de red.

Desde cada cliente:

```bash
sudo reboot
```

Después volvemos a conectarnos mediante SSH.

---

# 28 - Comprobar qué DNS utiliza CLIENTE-1

Ejecutamos:

```bash
resolvectl status
```

Debemos localizar una información similar a:

```text
DNS Servers: 10.0.1.10
DNS Domain: smr.test
```

También podemos ejecutar:

```bash
resolvectl dns
```

Debemos comprobar que aparece:

```text
10.0.1.10
```

!!! warning "/etc/resolv.conf"

````
En Ubuntu moderno no siempre debemos interpretar directamente:

```bash
cat /etc/resolv.conf
```

porque Ubuntu utiliza normalmente `systemd-resolved`.

Es posible encontrar:

```text
nameserver 127.0.0.53
```

Esto no significa necesariamente que nuestro DNS esté mal configurado.

`127.0.0.53` corresponde al *stub resolver* local de `systemd-resolved`.

Para conocer los servidores DNS reales utilizaremos:

```bash
resolvectl status
```
````

---

# 29 - Realizar consultas sin especificar el servidor DNS

Desde CLIENTE-1:

```bash
dig cliente2.smr.test
```

Ya no escribimos:

```text
@10.0.1.10
```

El cliente debe utilizar automáticamente nuestro servidor DNS.

También podemos ejecutar:

```bash
nslookup cliente2.smr.test
```

Resultado esperado:

```text
Name:    cliente2.smr.test
Address: 10.0.2.20
```

---

# 30 - Probar resolución mediante ping

Desde CLIENTE-1:

```bash
ping -c 4 cliente2.smr.test
```

El nombre deberá resolverse como:

```text
10.0.2.20
```

Desde CLIENTE-2:

```bash
ping -c 4 cliente1.smr.test
```

deberá resolverse como:

```text
10.0.2.10
```

!!! question "¿Qué estamos demostrando?"

````
El comando `ping` no realiza la resolución DNS por sí mismo.

Antes de poder enviar los mensajes ICMP necesita conocer la dirección IP del destino.

Por tanto:

```text
ping cliente2.smr.test
         │
         ▼
     consulta DNS
         │
         ▼
     10.0.2.20
         │
         ▼
      ICMP Echo
```
````

---

# 31 - Probar la resolución inversa desde los clientes

Desde CLIENTE-1:

```bash
dig -x 10.0.2.20
```

Resultado esperado:

```text
cliente2.smr.test.
```

También:

```bash
nslookup 10.0.2.20
```

Deberá devolver:

```text
cliente2.smr.test
```

---

# 32 - Comprobar dominios de Internet

Desde CLIENTE-1:

```bash
dig www.google.com
```

También:

```bash
nslookup www.google.com
```

La comunicación será:

```text
CLIENTE-1
10.0.2.10
     │
     │ Consulta DNS
     ▼
DNS-SERVER
10.0.1.10
     │
     │ Forward
     ▼
Amazon DNS
10.0.0.2
     │
     ▼
Resolución DNS de Internet
```

Así conseguimos que **todas las consultas DNS de nuestros clientes pasen primero por nuestro servidor BIND9**.

---

# 33 - Observar las consultas DNS

Esta parte es especialmente interesante para comprender el funcionamiento del protocolo.

En DNS-SERVER instalamos `tcpdump`:

```bash
sudo apt install tcpdump -y
```

Ejecutamos:

```bash
sudo tcpdump -i any port 53 -nn
```

Ahora, desde CLIENTE-1:

```bash
dig cliente2.smr.test
```

En DNS-SERVER podremos observar los paquetes DNS.

También podemos realizar:

```bash
dig www.google.com
```

En este caso podremos observar:

```text
CLIENTE-1 → DNS-SERVER
```

y posteriormente:

```text
DNS-SERVER → DNS AWS
```

---

# 34 - Observar únicamente las consultas del CLIENTE-1

En DNS-SERVER:

```bash
sudo tcpdump -i any host 10.0.2.10 and port 53 -nn
```

Después, desde CLIENTE-1:

```bash
dig cliente2.smr.test
```

---

# 35 - Comprobar la caché DNS

Desde CLIENTE-1 ejecutamos:

```bash
dig www.google.com
```

Observamos:

```text
Query time
```

en el resultado.

Repetimos:

```bash
dig www.google.com
```

La segunda consulta puede resolverse más rápidamente porque BIND9 puede disponer ya de la información en su **caché**.

Podemos visualizar estadísticas básicas de BIND mediante:

```bash
sudo rndc stats
```

---

# 36 - Añadir un nuevo registro DNS

Editamos:

```bash
sudo nano /etc/bind/db.smr.test
```

Añadimos:

```text
servidorweb     IN      A       10.0.2.10
```

Incrementamos también el Serial:

```text
2026090201
```

a:

```text
2026090202
```

Comprobamos:

```bash
sudo named-checkzone smr.test /etc/bind/db.smr.test
```

Si es correcto:

```bash
sudo systemctl reload named
```

Desde CLIENTE-2:

```bash
dig servidorweb.smr.test
```

Resultado esperado:

```text
servidorweb.smr.test.  IN  A  10.0.2.10
```

---

# 37 - Comprobar el TTL

En nuestra zona tenemos:

```text
$TTL 300
```

Esto corresponde a:

```text
300 segundos = 5 minutos
```

Desde CLIENTE-1:

```bash
dig cliente2.smr.test
```

En la sección:

```text
ANSWER SECTION
```

podremos observar el TTL.

Por ejemplo:

```text
cliente2.smr.test.    300    IN    A    10.0.2.20
```

---

# 38 - Comandos de diagnóstico

Durante la práctica serán especialmente útiles los siguientes comandos.

Comprobar el estado de BIND:

```bash
sudo systemctl status named
```

Reiniciar BIND:

```bash
sudo systemctl restart named
```

Recargar la configuración:

```bash
sudo systemctl reload named
```

Comprobar la sintaxis general:

```bash
sudo named-checkconf
```

Comprobar la zona directa:

```bash
sudo named-checkzone smr.test /etc/bind/db.smr.test
```

Comprobar la zona inversa:

```bash
sudo named-checkzone 2.0.10.in-addr.arpa /etc/bind/db.10.0.2
```

Consultar los logs:

```bash
sudo journalctl -u named -n 50 --no-pager
```

Comprobar puertos:

```bash
sudo ss -lntup | grep :53
```

Consultar un registro A:

```bash
dig cliente1.smr.test
```

Consultar únicamente el resultado:

```bash
dig +short cliente1.smr.test
```

Resultado:

```text
10.0.2.10
```

Consultar un registro específico:

```bash
dig A cliente1.smr.test
```

Consultar el registro NS:

```bash
dig NS smr.test
```

Consultar el registro SOA:

```bash
dig SOA smr.test
```

Consultar un CNAME:

```bash
dig CNAME www.smr.test
```

Realizar resolución inversa:

```bash
dig -x 10.0.2.10
```

Utilizar un DNS concreto:

```bash
dig @10.0.1.10 cliente1.smr.test
```

Utilizar `nslookup`:

```bash
nslookup cliente1.smr.test
```

Comprobar los DNS configurados en Ubuntu:

```bash
resolvectl status
```

Capturar tráfico DNS:

```bash
sudo tcpdump -i any port 53 -nn
```

---

# 39 - Pruebas finales

Antes de considerar terminada la práctica deben funcionar todas las siguientes pruebas.

Desde CLIENTE-1:

```bash
dig dns.smr.test
```

Debe devolver:

```text
10.0.1.10
```

Ejecutamos:

```bash
dig cliente1.smr.test
```

Debe devolver:

```text
10.0.2.10
```

Ejecutamos:

```bash
dig cliente2.smr.test
```

Debe devolver:

```text
10.0.2.20
```

Ejecutamos:

```bash
dig www.smr.test
```

Debe resolver el CNAME.

Ejecutamos:

```bash
dig -x 10.0.2.10
```

Debe devolver:

```text
cliente1.smr.test
```

Ejecutamos:

```bash
dig -x 10.0.2.20
```

Debe devolver:

```text
cliente2.smr.test
```

Ejecutamos:

```bash
dig www.google.com
```

Debe resolver un dominio de Internet.

Finalmente:

```bash
ping cliente2.smr.test
```

debe resolver:

```text
10.0.2.20
```

---

# 40 - Funcionamiento final de la arquitectura

Cuando CLIENTE-1 quiere comunicarse con:

```text
cliente2.smr.test
```

ocurre:

```text
CLIENTE-1
10.0.2.10
     │
     │ "¿Cuál es la IP de cliente2.smr.test?"
     │ UDP/53
     ▼
DNS-SERVER
10.0.1.10
     │
     │ consulta su zona
     │ smr.test
     ▼
cliente2.smr.test = 10.0.2.20
     │
     ▼
CLIENTE-1
     │
     │ ya conoce la IP
     ▼
10.0.2.20
CLIENTE-2
```

Sin embargo, si pregunta por:

```text
www.google.com
```

BIND no es autoritativo para ese dominio:

```text
CLIENTE-1
     │
     │ www.google.com
     ▼
DNS-SERVER
10.0.1.10
     │
     │ forward
     ▼
DNS de AWS
10.0.0.2
     │
     ▼
Internet
     │
     ▼
respuesta
     │
     ▼
DNS-SERVER
     │
     ▼
CLIENTE-1
```

Por tanto, nuestro servidor BIND9 realiza **dos funciones diferentes**:

1. Es **servidor DNS autoritativo** para:

   ```text
   smr.test
   ```

2. Actúa como **servidor DNS recursivo con reenvío** para el resto de dominios.

---

# 41 - Resultado de la práctica

Al finalizar tendremos configurada la siguiente infraestructura:

```text
VPC 10.0.0.0/16
│
├── SUBNET-SERVIDORES 10.0.1.0/24
│
│   └── DNS-SERVER
│       10.0.1.10
│       │
│       ├── BIND9
│       ├── Zona directa: smr.test
│       ├── Zona inversa: 1.0.10.in-addr.arpa
│       ├── Zona inversa: 2.0.10.in-addr.arpa
│       └── Forwarder: 10.0.0.2
│
└── SUBNET-CLIENTES 10.0.2.0/24
    │
    ├── CLIENTE-1
    │   10.0.2.10
    │
    └── CLIENTE-2
        10.0.2.20

DNS configurado mediante DHCP:
10.0.1.10
```

Los clientes podrán resolver tanto nombres internos:

```text
dns.smr.test
cliente1.smr.test
cliente2.smr.test
www.smr.test
```

como nombres de Internet:

```text
www.google.com
www.ubuntu.com
www.wikipedia.org
```

utilizando siempre nuestro servidor BIND9 como servidor DNS. -->
