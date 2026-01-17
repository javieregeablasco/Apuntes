---
cicle: CFGS - Desarrollo de aplicaciones web
title: "Introducción a la nube pública"
module number: 
lesson: UD. 8 - Sistemas de almacenamiento y bases de datos en AWS
author: Javier Egea Blasco  
year: 25-26  
keywords: DAW, Optativa, AWS
layout: default  
schedule: 96h - 3h/s 
---

# **UT. 8 - Sistemas de almacenamiento y bases de datos en AWS**

![Descripción de la imagen](./ut8/ut8-1.png){.sietecinco}    
   
 
<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:** |
|-|
| **RA. 4:** Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento.|

|**Criterios de evaluación de la unidad didáctica:**|
|-|
|**a)** Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube.|
|**b)** Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube.|
|**c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.|
 


## **1 - Sistemas de almacenamiento en AWS**
### **1.1 - Introducción**

![Descripción de la imagen](./ut8/ut8-2.png){.trescinco}    

Existen multitud de sistemas de almacenamiento en AWS pero, podemos dividirlos en tres grandes categorías, principalmente en función de cómo se accede a los datos y del tipo de uso al que están orientados:

- **Almacenamiento de objetos**:  
Amazon S3 (buckets S3), orientado a datos altamente escalables como imágenes, vídeos o copias de seguridad.
- **Almacenamiento en bloques**:  
Amazon EBS (ya visto en una unidad anterior), utilizado como discos persistentes que se adjuntan a instancias EC2.
- **Almacenamiento de archivos**:  
Amazon EFS, que proporciona sistemas de archivos compartidos, accesibles desde múltiples instancias.

 
 

### **1.2 - Diferencias en almacenamiento por objetos, bloques y archivos**
Las diferencias fundamentales entre el almacenamiento por bloques, archivos y objetos se centran en la forma en que se estructuran, acceden y modifican los datos, así como en su rendimiento y escalabilidad.

---

#### **1.2.1 - Almacenamiento por Bloques (Amazon EBS)**

![Descripción de la imagen](./ut8/ut8-3.png){.unocinco}    

En el almacenamiento por bloques, los datos se dividen en bloques independientes que funcionan de forma similar a un disco duro tradicional.


- **Modificación de datos:**   
Si se cambia una parte de la información, solo se debe modificar el bloque específico que la contiene, lo que permite baja latencia y alto rendimiento.  
Esto lo hace especialmente adecuado para aplicaciones con operaciones de lectura y escritura frecuentes.

- **Conectividad:**  
Los volúmenes Amazon EBS se adjuntan a instancias EC2 y actúan como **discos persistentes**.  
Normalmente, un volumen EBS solo puede estar conectado a una única instancia EC2, excepto en configuraciones específicas como EBS Multi-Attach.

- **Persistencia:**  
Los datos no se pierden al detener una instancia EC2, ya que el volumen EBS es independiente de la vida de la instancia.  

- **Casos de uso:**  
Bases de datos relacionales.  
Sistemas operativos de EC2.  
Aplicaciones que requieren baja latencia y alto IOPS.

---

#### **1.2.2 - Almacenamiento de Archivos (Amazon EFS)**

![Descripción de la imagen](./ut8/ut8-4.png){.unocinco}    

Este sistema ofrece **un almacenamiento compartido** al que pueden acceder simultáneamente múltiples instancias.

- **Protocolo y estructura:**  
Utiliza el protocolo de sistemas de archivos de red (NFS) y se comporta de manera similar a un NAS (Network Area Storage).  

- **Escalabilidad y disponibilidad:**  
Es elástico y escala de forma automática a medida que se agregan o eliminan archivos, llegando a niveles de petabytes sin interrumpir las aplicaciones ni necesitar intervención humana.  
Además, es un servicio altamente disponible, diseñado para operar en múltiples zonas de disponibilidad.  

- **Casos de uso:**  
Big Data y entornos de análisis.  
Sistemas de archivos compartidos.  
CMS como WordPress.  
Contenedores y microservicios con almacenamiento compartido.

---

#### **1.2.3 - Almacenamiento de Objetos (Amazon S3)**

![Descripción de la imagen](./ut8/ut8-5.png){.unocinco} 

En el almacenamiento por objetos, los datos se almacenan como objetos dentro de contenedores llamados buckets.

Cada objeto incluye el **archivo en sí**, un **identificador único (key)** y **metadatos** que ayudan a catalogarlo.  

- **Modificación de datos:**  
A diferencia del almacenamiento por bloques, una modificación en un objeto requiere volver a cargar el archivo entero.  

- **Acceso y escalabilidad:**   
Los objetos son accesibles desde cualquier lugar mediante una URL (sujeto a políticas de seguridad).  
Es una solución extremadamente escalable y, aunque es más lenta en escritura que EBS, es más sencilla y barata.
Es un servicio altamente duradero (99,999999999%) y prácticamente ilimitado en capacidad.  

- **Estructura lógica:**   
Aunque la consola permita navegar mediante "carpetas", en realidad no existen los directorios como tal, el sistema utiliza las keys (nombres de archivo que incluyen prefijos) para simular una jerarquía.  

- **Casos de uso:**  
Copias de seguridad y archivado  
Alojamiento de sitios web estáticos  
Aplicaciones móviles  
Data Lakes y análisis de datos  

<br>

#### **1.2.4 - Resumen**
| Característica | Amazon EBS            | Amazon EFS           | Amazon S3             |
| -------------- | --------------------- | -------------------- | --------------------- |
| Tipo           | Bloques               | Archivos             | Objetos               |
| Acceso         | Una EC2 (normalmente) | Varias EC2           | HTTP/HTTPS            |
| Modificación   | A nivel de bloque     | A nivel de archivo   | Objeto completo       |
| Latencia       | Muy baja              | Baja                 | Mayor                 |
| Escalabilidad  | Limitada por volumen  | Automática           | Ilimitada             |
| Persistencia   | Independiente de EC2  | Independiente de EC2 | Total                 |
| Casos típicos  | BBDD, SO              | CMS, compartido      | Backups, web estática |



### **1.3 - Tarea RA4-CEa-1 - Creación de un Amazon EFS**
#### **1.3.1 - Escenario propuesto**
![Descripción de la imagen](./ut8/EFS/efs-1.png){.cincozero} 

El escenario básico consistirá en 2 instancias y una puerta de enlace a internet para poder conectarnos a ellas.

- Una EC2 estará en la zona de disponibilidad a.
- La otra EC2 estará en otra zona de disponibilidad (p.e. b).

Por otra parte crearemos un EFS y su grupo de seguridad. Para mayor seguridad del EFS, el grupo de seguridad solo aceptará conexiones entrantes desde los grupos de seguridad de las instancias EC2. 

Para terminar, instalaremos un cliente NFS en las instancias EC2 para poder comunicarse con el EFS. Además añadiremos una directiva que forzará el encriptado de los datos durante las transferencias entre instancias EC2 y NFS. 

---

#### **1.3.2 - Creación de la infraestructura básica**
Creamos la VPC, las subredes, el IGW y configuramos la tabla de enrutamiento.

![Descripción de la imagen](./ut8/EFS/efs-2.png){.cien .marco} 

---

#### **1.3.3 - Lanzamiento de las EC2**
Primero crearemos el mismo grupo de seguridad para las 2 instancias y luego lanzaremos las instancias. Cada una en una subred distinta.

![Descripción de la imagen](./ut8/EFS/efs-3.png){.cien .marco} 

---

#### **1.3.4 - Lanzamiento del EFS**
- Antes de nada, crearemos un grupo de seguridad para el EFS y lo configuraremos para que solo acepte conexiones NFS desde los grupos de seguridad de las instancias que hemos creado.  
![Descripción de la imagen](./ut8/EFS/efs-3-1.png){.cien .marco .margintopbottom20} 
 

- Accedemos a los recursos de AWS EFS y creamos nuestro primer EFS.
![Descripción de la imagen](./ut8/EFS/efs-4.png){.cincozero .marco .margintopbottom20} 

- Pulsamos personalizar para ver las diferentes configuraciones disponibles.
    - Paso 1
![Descripción de la imagen](./ut8/EFS/efs-5.png){.sietecinco .marco .margintopbottom20}  
    - Paso 2  
    Elegimos los grupos de seguridad de los puntos de montaje para que el NFS solo acepte conexiones desde las instancias EC2 que hemos creado anteriormente.
![Descripción de la imagen](./ut8/EFS/efs-6.png){.sietecinco .marco .margintopbottom20}  
    - Paso 3  
    Seleccionamos la política para el cifrado en tránsito.
![Descripción de la imagen](./ut8/EFS/efs-7.png){.sietecinco .marco .margintopbottom20}  
    - Paso 4  
    Revisamos y creamos el NFS.
![Descripción de la imagen](./ut8/EFS/efs-8.png){.sietecinco .marco .margintopbottom20}  

#### **1.3.5 - Cliente NFS sobre instancias EC2**
!!! warning "Repetiremos los pasos siguientes en cada instancia EC2"

!!! tip "Crear el punto de montaje"
Accedemos a las intancias EC2 y creamos el punto de montaje 
```bash
mkdir ~/efs
```
![Descripción de la imagen](./ut8/EFS/efs-9.png){.trescinco }  

<br>

!!! tip "Instalar el cliente NFS"
Normalmente el cliente NFS ya debería estar instalado. 
```bash
sudo yum -y install nfs-utils
```
![Descripción de la imagen](./ut8/EFS/efs-10.png){.cincozero }  

También instalaremos el cliente de Amazon EFS **para instancias de Amazon linux**.  
```bash
sudo yum install -y amazon-efs-utils
```
![Descripción de la imagen](./ut8/EFS/efs-11.png){.cincozero }  

<br>

!!! tip "Montar el EFS con el helper de AWS EFS"
Realizaremos el montaje utilizando **el nombre de DNS** del sistema de archivos (podeís ver el comando completo pulsando **Asociar**).

![Descripción de la imagen](./ut8/EFS/efs-12.png){.cien .marco }  
![Descripción de la imagen](./ut8/EFS/efs-12-1.png){.cien .marco }  
```bash
sudo mount -t efs -o tls fs-003ab364472cbdb19:/ efs
```
![Descripción de la imagen](./ut8/EFS/efs-13.png){.sietecinco }  

<br>

!!! tip "Primera prueba del EFS"
Nos cambiamos al directorio donde hemos montado el EFS y hacemos una prueba de escritura.
![Descripción de la imagen](./ut8/EFS/efs-14.png){.cincozero }  

Si ahora, desde la otra instancia añadimos contenido al archivo de texto y lo leemos de nuevo, podremos ver la modificaciones aportadas.
![Descripción de la imagen](./ut8/EFS/efs-15.png){.cuatrozero }  

#### **1.3.6 - Condiciones de la entrega de la tarea RA4-CEa-1**
!!! warning "Condiciones de entrega"
    1. Montar el ejemplo anterior.
    1. Realizar capturas de pantalla del mapa de recursos de la VPC desplegada.
    1. Realizar capturas de pantalla de las 2 instanciasaccediendo al NFS.    
    1. Adjuntar las capturas a un documento, y comentar brevemente cada captura.
    1. Subir el documento a AULES en la tarea correspondiente. 

### **1.4 - Tarea RA4-CEa-2 - Creación de un bucket S3**
#### **1.4.1 - Creación del bucket S3**
Accedemos al servicio S3 para crear el bucket. Es importante recordar que el espacio de **nombres (namespace) de S3 es global**, por lo que el nombre debe ser **único en todo el mundo**. Sin embargo, **S3 es un servicio regional**, por lo que deberemos seleccionar la región más cercana a nuestras instancias para minimizar la latencia.

- Creación del bucket S3.
![Descripción de la imagen](./ut8/S3/s3-1.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Le damos un nombre único. Si hay errores de sintaxis o el nombre ya está asignado, aparecerá un error. 
![Descripción de la imagen](./ut8/S3/s3-2.png){.nuevezero .marco .margintop10 }  
![Descripción de la imagen](./ut8/S3/s3-9.png){.nuevezero .marco   }  
![Descripción de la imagen](./ut8/S3/s3-10.png){.nuevezero .marco  .marginbottom40 }  


- En **propiedad de objetos** dejamos la opción por defecto.
![Descripción de la imagen](./ut8/S3/s3-3.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- En **configuración de bloqueo de acceso público** dejamos la opción por defecto.
![Descripción de la imagen](./ut8/S3/s3-4.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- En **control de versiones de buckets** habilitamos el servicio (veremos el porqué más adelante). 
![Descripción de la imagen](./ut8/S3/s3-5.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Si queremos, podemos agregar una etiqueta.  
![Descripción de la imagen](./ut8/S3/s3-6.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Cifrado predeterminado: Dejamos las opciones por defecto.   
![Descripción de la imagen](./ut8/S3/s3-7.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Configuración avanzada. Dejamos el bloqueo de objeto desactivado.
![Descripción de la imagen](./ut8/S3/s3-8.png){.nuevezero .marco .margintop10  }
- !!! warning "Bloqueo de objetos"  
      - El S3 Object Lock (Bloqueo de Objetos) es una funcionalidad diseñada para evitar que los objetos **sean eliminados o sobrescritos**. 
      - Permite implementar modelos de almacenamiento WORM (Write Once, Read Many), lo cual es vital para **el cumplimiento normativo y la protección contra ataques de ransomware**.   

- Si todo ha ido bien tendremos nuestro bucket S3 creado.
![Descripción de la imagen](./ut8/S3/s3-11.png){.nuevezero .marco .margintop10 .marginbottom40 }  

#### **1.4.2 - Subir objetos al bucket S3**
- Arrastramos el objeto a subir y pulsamos cargar. 
![Descripción de la imagen](./ut8/S3/s3-12.png){.nuevezero .marco .margintop10   }  
![Descripción de la imagen](./ut8/S3/s3-15.png){.nuevezero .marco   .marginbottom40 }  

- Una vez subido el archivo podremos acceder a sus propiedades, permisos y versiones (si hemos habilitado el versionado de objetos en el bucket S3).
![Descripción de la imagen](./ut8/S3/s3-16.png){.nuevezero .marco .margintop10  .marginbottom40 }
- En **Propiedades** → **Clase de almacenamiento** podemos ver (y configurar) el tipo de almacenamiento (se aplican tarifas especificas a cada clase de almacenamiento).   
![Descripción de la imagen](./ut8/S3/s3-14.png){.nuevezero .marco .marginbottom40 .margintop20}  

- En **Permisos**, podemos ver las listas de control de acceso actuales del objeto.   
![Descripción de la imagen](./ut8/S3/s3-17.png){.nuevezero .marco .margintop10 .marginbottom40 }  

#### **1.4.3 - Acceder a los objetos de un bucket S3**
- Si intentamos acceder al objeto veremos que no es posible. Eso se debe a los permisos (lista de control de acceso (ACL)) del propio bucket.  
![Descripción de la imagen](./ut8/S3/s3-17-1.png){.nuevezero .marco .margintop10   }  
![Descripción de la imagen](./ut8/S3/s3-18.png){.sietezero    }  
![Descripción de la imagen](./ut8/S3/s3-13.png){.nuevezero .marco .marginbottom40 }  

#### **1.4.4 - Permitir acceso a los objetos de un bucket S3**
- Para permitir el acceso a los objetos volvemos al bucket S3 y editamos las reglas de bloqueo del acceso público.  
![Descripción de la imagen](./ut8/S3/s3-24.png){.nuevezero .marco .margintop10  }  
![Descripción de la imagen](./ut8/S3/s3-19.png){.nuevezero .marco  }  
![Descripción de la imagen](./ut8/S3/s3-20.png){.nuevezero .marco .marginbottom40}  

- Luego ya podremos editar las propiedades de los objetos de nuestro bucket S3.
![Descripción de la imagen](./ut8/S3/s3-21.png){.nuevezero .marco  .margintop10 }  
![Descripción de la imagen](./ut8/S3/s3-22.png){.nuevezero .marco   .marginbottom40 }  

- A partir de entonces **cualquier persona con el enlace** podrá acceder al objeto. 
![Descripción de la imagen](./ut8/S3/s3-23.png){.nuevezero .marco .margintop10 .marginbottom40 }  

#### **1.4.5 - Versionado de un objeto**
Como ya hemos comentado anteriormente, si no tenemos habilitado el versionado de objeto, volver a subir un archivo modificado de un mismo objeto implica **sobreescribir totalmente** el objeto anterior.  

Con el versionado de objetos, podemos crear versiones de un mismo objeto.

- Después de subir un objeto versionado, podremos ver las diferentes versiones existentes en el bucket S3.
![Descripción de la imagen](./ut8/S3/s3-25.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- **Tarea: Trabajo a realizar.** Como en el caso anterior deberemos habilitar las ACL para poder acceder al archivo. De lo contrario obtendremos un mensaje de error. 
![Descripción de la imagen](./ut8/S3/s3-26.png){.sietezero .margintop10 }  

#### **1.4.6 - Eliminación de un objeto versionado**
- Si eliminamos el objeto, **en teoría**, debería dejar de esatar disponible.  
![Descripción de la imagen](./ut8/S3/s3-27.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Vista después de la eliminación de objetos.
![Descripción de la imagen](./ut8/S3/s3-27-1.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Si habilitamos, **Mostrar versiones**, veremos que, aunque hayamos elminado el objeto, sus versiones siguen disponibles. Este proceder tiene la ventaja de poder recuperar objetos borrados por error, pero también tiene el inconveniente de cargos adicionales por parte de AWS.      
![Descripción de la imagen](./ut8/S3/s3-28-1.png){.nuevezero .marco .margintop10 .marginbottom40 }  


#### **1.4.7 - Eliminación de un bucket S3**
- Para eliminar un bucket S3, primero deberemos **vaciarlo**.
![Descripción de la imagen](./ut8/S3/s3-31.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Vaciamos el bucket S3.
![Descripción de la imagen](./ut8/S3/s3-32.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Una vez vaciado el bucket S3, podremos **eliminarlo definitivamente**.
![Descripción de la imagen](./ut8/S3/s3-33.png){.nuevezero .marco .margintop10 .marginbottom40 }  

#### **1.4.8 - Condiciones de la entrega de la tarea RA4-CEa-2**
!!! warning "Condiciones de entrega"
    1. Montar el ejemplo anterior.
    1. Editar las ACL de la versión 2 del objeto que subireis a vuestro bucket S3.
    1. **Realizar capturas que muestran el acceso mediante URL a las 2 versiones**. 
    1. Adjuntar las capturas a un documento, y comentar brevemente cada captura.
    1. Subir el documento a AULES en la tarea correspondiente. 

## **2 - Servicios de bases de datos en la nube (AWS)**
Los servicios de bases de datos en la nube permiten alojar el servidor de base de datos en la infraestructura de un proveedor de servicios en Internet. Este tipo de servicio se conoce como DBaaS (Database as a Service).

Estos servicios ofrecen muchas de las funcionalidades de un sistema gestor de bases de datos tradicional y, además, incluyen numerosas tareas que normalmente realiza un administrador de bases de datos (DBA), como el aprovisionamiento, las copias de seguridad, la alta disponibilidad, el parcheo o la monitorización.

De esta manera, se reduce el tiempo que un DBA dedica a tareas puramente administrativas, permitiéndole centrarse en actividades de mayor valor añadido, como el diseño de la arquitectura, la optimización del rendimiento o la seguridad de los datos.

Dependiendo del tipo de datos a almacenar, AWS ofrece distintos sabores de DBaaS:

- **Amazon RDS** (Relational Database Service): Para bases de datos relacionales tradicionales (SQL). Soporta motores como MySQL, PostgreSQL, SQL Server y Oracle.

- **Amazon Aurora**: Una base de datos diseñada por AWS que es compatible con MySQL y PostgreSQL pero optimizada para ser mucho más rápida y resiliente en la nube.

- **Amazon DynamoDB**: Un servicio NoSQL (llave-valor) para aplicaciones que necesitan una latencia de milisegundos a cualquier escala (muy usado en aplicaciones móviles y juegos).

### **2.1 - Bases de datos relacionales**
!!! tip "Amazon RDS"
- Amazon RDS es un servicio administrado que permite ejecutar bases de datos relacionales en la nube.  
Al tratarse de un servicio gestionado, RDS se encarga de tareas como la instalación, el mantenimiento y las copias de seguridad, permitiendo que los usuarios se centren en los datos y en el desarrollo de las aplicaciones.

- Una instancia de base de datos es un entorno aislado que puede contener **una o varias bases de datos**, dependiendo del motor seleccionado. Se accede a ella utilizando las mismas herramientas y aplicaciones que en una base de datos tradicional.

- Al crear una instancia en Amazon RDS, es necesario elegir el motor de base de datos. Los motores relacionales soportados por RDS son:
    - MariaDB
    - **MySQL**
    - PostgreSQL
    - **Amazon Aurora** (compatible con MySQL y PostgreSQL)
    - Microsoft SQL Server
    - Oracle

![Descripción de la imagen](./ut8/RDS/rds-1.png){.nuevezero .marco .margintop10 .marginbottom40 }  

- Los recursos de la instancia se definen mediante la clase de instancia y el tipo de almacenamiento, lo que permite ajustar el rendimiento y el coste según las necesidades.

!!! tip "Alta disponibilidad"
Una de las características más importantes de Amazon RDS es la posibilidad de configurar alta disponibilidad mediante una implementación Multi-AZ. En este modo, RDS crea automáticamente una instancia en espera en otra zona de disponibilidad dentro de la misma región y replica los datos de forma síncrona.

Si la instancia principal falla, RDS realiza un failover automático, promoviendo la instancia en espera como nueva instancia principal, lo que reduce el tiempo de inactividad.

![Descripción de la imagen](./ut8/RDS/rds-3.png){.cincozero .marco .margintop10 .marginbottom40 }  

!!! tip "Replicas de lectura"
Amazon RDS permite crear réplicas de lectura para los motores MySQL, MariaDB, PostgreSQL y Amazon Aurora. En este caso, los cambios realizados en la instancia principal se replican de forma asíncrona en la réplica.

Las réplicas de lectura permiten descargar las consultas de lectura de la instancia principal y mejorar el rendimiento. Estas réplicas pueden promocionarse manualmente a instancia principal y también pueden crearse en otra región, lo que resulta útil para mejorar la latencia de lectura o como apoyo en escenarios de recuperación ante desastres.

![Descripción de la imagen](./ut8/RDS/rds-2.png){.cincozero .marco .margintop10 .marginbottom40 }  

!!! tip "Supervisión"
Para monitorizar el rendimiento y el estado de una instancia de base de datos en Amazon RDS se utiliza el servicio **Amazon CloudWatch**. Las métricas y gráficos de rendimiento pueden visualizarse directamente desde la consola de Amazon RDS.

Además, es posible suscribirse a los eventos de Amazon RDS para recibir notificaciones sobre cambios relevantes en una instancia de base de datos, como tareas de mantenimiento o incidencias.



#### **2.1.1 - Amazon RDS con MySQL**

!!! tip "Preparación del entorno"
Para la infraestructura de red necesitaremos un mínimo de:

- Una VPC.
- Al menos dos subredes en zonas de disponibilidad distintas (preferiblemente privadas).
- Un grupo de seguridad para la base de datos.  
- La plantilla para lanzar esta infraestrucutura se puede descargar [aquí](./ut8/RDS/plantilla.yaml) 

---

!!! tip "Lanzar una instancia de Amazon RDS con MySQL"  
- Una vez creada la infraestructura, vamos a Aurora and RDS y pulsamos **crear una base de datos**.
![Descripción de la imagen](./ut8/RDS/rds-4.png){.cien .marco .margintop10 .marginbottom40 }  

- Seleccionamos **Configuración completa** y **MySQL**.  
![Descripción de la imagen](./ut8/RDS/rds-5.png){.cien .marco .margintop10 .marginbottom40 }  

- Seleccionamos **la versión del motor** que nos propone por defecto y **entorno de pruebas**.   
![Descripción de la imagen](./ut8/RDS/rds-6.png){.cien .marco .margintop10 .marginbottom40 }  

- **Disponibilidad y durabilidad**. Al seleccionar **entorno de pruebas**, **Amazon RDS** solo desplegará **una sola instancia (Single-AZ)**, **sin configuración de alta disponibilidad (Multi-AZ)**.   
![Descripción de la imagen](./ut8/RDS/rds-7.png){.cien .marco .margintop10 .marginbottom40 }  

- **Configuración:** Damos un identificador a nuestra instancia y introducimos una contraseña. 
![Descripción de la imagen](./ut8/RDS/rds-8.png){.cien .marco .margintop10 .marginbottom40 }  

- **Configuración de la instancia**. Dejamos los opciones por defecto.
![Descripción de la imagen](./ut8/RDS/rds-9.png){.cien .marco .margintop10 .marginbottom40 }  

- **Almacenamiento**. Dejamos las opciones por defecto. 
![Descripción de la imagen](./ut8/RDS/rds-10.png){.cien .marco .margintop10 .marginbottom40 }  

- **Conectividad 1/2**. Elegimos la VPC donde se desplegará la instancia de RDS y para poder acceder a ella, le daremos un IP pública. 
![Descripción de la imagen](./ut8/RDS/rds-11.png){.cien .marco .margintop10 .marginbottom40 }  

- **Conectividad 2/2**. Elegimos el grupo de seguridad que hemos creado con la plantilla y dejamos el resto de opciones con los valores por defecto.  
**Nota importante:** Exponer una instancia de bases de datos a internet **no se puede considerar una buena práctica del punto de vista de la seguridad informática**. 
![Descripción de la imagen](./ut8/RDS/rds-12.png){.cien .marco .margintop10 .marginbottom40 }  

---
!!! tip "Creación de la base de datos"

- Empezará después de pulsar **crear base de datos**. 
![Descripción de la imagen](./ut8/RDS/rds-13.png){.cien .marco .margintop10 .marginbottom40 }  

- **Punto de enlace**. Una vez creada la base de datos, podremos acceder a ella a través de su punto de enlace.
![Descripción de la imagen](./ut8/RDS/rds-14.png){.cien .marco .margintop10 .marginbottom40 }  

---
!!! tip "Conexión desde MySQL Workbench"
- Introducimos el punto de enlace, el usuario y la contraseña y probamos la conexión.
![Descripción de la imagen](./ut8/RDS/rds-15.png){.cincozero .marco .margintop10  .marginbottom40} 
- Vemos que la conexión se ha realizado correctamente... 
![Descripción de la imagen](./ut8/RDS/rds-16.png){.treszero .marco  .marginbottom40 .margintop10 }  
- ... y ya podemos trabajar con la base de datos.
![Descripción de la imagen](./ut8/RDS/rds-17.png){.cincozero .marco .margintop10 .marginbottom40 }  

#### **2.1.2 - Tarea RA4-CEb-1**
En esta tarea, realizaremos un escenario más realista donde la base de datos estará en una red privada y solo se podrá tener acceso a ella desde el grupo de seguridad de una instancia de la subred pública.  
Además usaremos las características de redundancia y disponibilidad (2 réplicas de lectura y despliegue multi-AZ) para mejorar la calidad del servicio.

- **Modificar la VPC**. En este caso RDS requiere de 3 subredes en 3 zonas de disponibilidad distintas, así pues, añadiremos 2 subredes (una pública y otra privada) a nuestra VPC.
![Descripción de la imagen](./ut8/RDS/ra4ceb-4.png){.cien .marco .margintop10 .marginbottom40 }  

- **Crear el servicio RDS com MySQL:** Esta vez elegimos **desarrollo y prueba** e implementación de clúster multi-AZ.
![Descripción de la imagen](./ut8/RDS/ra4ceb-1.png){ .marco .margintop10 .marginbottom40 }  

- En **configuración** elegimos **autoadministrado**.
![Descripción de la imagen](./ut8/RDS/ra4ceb-2.png){.cien .marco .margintop10 .marginbottom40 }  

- En **conectividad**, si hemos creado una instancia EC2 (para este case una máquina Ubuntu), elegimos **conectarse a un recurso de EC2**.
**Nota:** Por algún motivo desconocido AWS no reconoce automáticamente las nuevas subredes. Tendremos que añadirlas manualmente.
![Descripción de la imagen](./ut8/RDS/ra4ceb-3.png){.cien .marco .margintop10 .marginbottom40 }
Primero las seleccionamos.  
![Descripción de la imagen](./ut8/RDS/ra4ceb-5.png){.cien .marco .margintop10 .marginbottom40 }  
Le damos a refrescar y luego podremos continuar con la configuración de nuestro cluster RDS.  
![Descripción de la imagen](./ut8/RDS/ra4ceb-6.png){.cien .marco .margintop10 .marginbottom40 }  

- En **grupo de seguridad**, podemos elegir el que hemos creado en la práctica anterior.
![Descripción de la imagen](./ut8/RDS/ra4ceb-7.png){.cien .marco .margintop10 .marginbottom40 }  

- **Implementación del cluster RDS.** Después de crear la base de datos veremos el progreso de su despliegue.
![Descripción de la imagen](./ut8/RDS/ra4ceb-8.png){.cien .marco .margintop10 .marginbottom40 }  

- Con el despliegue finalizado, podremos ver los puntos de conexión (lectura/escritura y solo lectura).
![Descripción de la imagen](./ut8/RDS/ra4ceb-11.png){.cien .marco .margintop10 .marginbottom40 }  

- Modificamos el grupo de seguridad del cluster para que solo acepte conexiones desde el grupo de seguridad de la instancia EC2.  
<mark>Realizar captura de pantalla</mark> 
![Descripción de la imagen](./ut8/RDS/ra4ceb-10.png){.cien .marco .margintop10 .marginbottom40 }  

- También podemos ver como ha quedado la configuración del grupo de seguridad de la instancia EC2.  
**Nota:** En la imagen podemos ver el nuevo grupo de seguridad y también el de la práctica anterior. 
![Descripción de la imagen](./ut8/RDS/ra4ceb-9.png){.cien .marco .margintop10 .marginbottom40 }  

- Accedemos a la instancia y nos conectamos a la base de datos desde **el punto de acceso escritor**.  
<mark>Realizar captura de pantalla</mark> 
![Descripción de la imagen](./ut8/RDS/ra4ceb-12.png){.sietecinco .margintop10 .marginbottom40 }  
Creamos una base de datos.  
<mark>Realizar captura de pantalla</mark> 
![Descripción de la imagen](./ut8/RDS/ra4ceb-13.png){.treszero .margintop10 }  
![Descripción de la imagen](./ut8/RDS/ra4ceb-13-1.png){.doszero .marginbottom40 }  

- Si ahora accedemos desde **el punto de acceso lector** veremos que no podemos crear nada.  
<mark>Realizar captura de pantalla</mark> 
![Descripción de la imagen](./ut8/RDS/ra4ceb-14.png){.sietecinco .margintop10 .marginbottom40 }  

- Si provocamos **un fallo del cluster RDS** veremos como AWS se encarga de cambiar la instancia escritora a otra instancia del cluster **sin modificar los puntos de conexión**. 
![Descripción de la imagen](./ut8/RDS/ra4ceb-15.png){.cien .marco .margintop10 }  
![Descripción de la imagen](./ut8/RDS/ra4ceb-16.png){.cincozero .marco .marginbottom40 }
<mark>Realizar captura de pantalla</mark> 
![Descripción de la imagen](./ut8/RDS/ra4ceb-17.png){.cincozero .marco .margintop10 .marginbottom40 }  

!!! tip "¿Qué situaciones activan una conmutación por error?"
    El **failover** no solo ocurre cuando algo "explota". Se activa automáticamente ante:
    
    - Pérdida de disponibilidad en la zona de disponibilidad primaria.
    - Pérdida de conectividad de red con la instancia principal.
    - Fallo en el hardware de la unidad física.
    - Mantenimiento del sistema: Como cambios en el tipo de instancia o parches del sistema operativo (AWS realiza el failover para que el tiempo de inactividad sea mínimo).

    Cuando ocurre una conmutación por error, Amazon RDS cambia automáticamente la base de datos principal (primaria) a una instancia de respaldo (standby) ubicada en otra zona de disponibilidad. Esto sucede de forma transparente, minimizando el tiempo de inactividad. Durante este proceso, el tráfico de la base de datos se redirige a la nueva instancia primaria sin intervención del usuario. Después de la conmutación, la base de datos en la zona original se vuelve una instancia de respaldo y permanece en espera de posibles fallos futuros. Este enfoque asegura **alta disponibilidad y recuperación ante desastres** en entornos de producción.


!!! warning "Condiciones de entrega de la tarea RA4-CEb-1"
    1. Realizar capturas de pantalla de los puntos señalados.
    1. Comentar brevemente cada captura para entender a qué corresponde y subir el documento a la tarea correspondiente de AULES.
    1. Después de completar la tarea, **eliminar el cluster o restablecer inmediatamente el laboratorio**, al ser los costes del cluster **muy elevados**. 

---

#### **2.1.3 - Amazon RDS con Aurora**
!!! tip "Introducción:"  
**Amazon Aurora** es un motor de base de datos relacional compatible con **MySQL** y **PostgreSQL** diseñado específicamente para la nube. Se integra dentro del servicio gestionado **Amazon RDS**, facilitando la administración, el escalado y la seguridad de las bases de datos.
<br>

!!! tip "Ventajas Principales:"  

Al ser un motor nativo de AWS, Aurora ofrece beneficios superiores a las implementaciones tradicionales:

1. **Rendimiento:** Hasta 5 veces más rápido que MySQL estándar y 3 veces más que PostgreSQL.
1. **Coste-Efectividad:** Optimiza el uso de recursos mediante la separación de cómputo y almacenamiento.
1. **Alta Disponibilidad:**
    * Replica **6 copias de los datos** en 3 Zonas de Disponibilidad (AZ).
    * Soporta la pérdida de hasta 2 copias sin afectar la escritura.
1. **Backups Continuos:** Realiza copias de seguridad automáticas y constantes en **Amazon S3**, permitiendo la recuperación en cualquier punto del tiempo (PITR).

!!! tip "¿Por qué elegir Aurora sobre RDS MySQL estándar?"

1. **Almacenamiento Auto-escalable:** No es necesario pre-aprovisionar espacio; el almacenamiento crece automáticamente hasta 128 TiB (según la demanda).  
1. **Failover Veloz:** La conmutación por error (Failover) se completa generalmente en menos de 30 segundos, mejorando la continuidad del negocio.
1. **Arquitectura de Lectura:** Permite hasta 15 réplicas con una latencia de replicación de milisegundos, ya que todas las instancias comparten el mismo volumen de almacenamiento virtual.
![Descripción de la imagen](./ut8/EURORA/EUR-1.png){.cien .marco .margintop10 .marginbottom40 }  

!!! tip "Aurora serverless"
Amazon Aurora Serverless es una variante de Aurora que funciona bajo demanda, es decir, sin que tengas que gestionar instancias fijas de base de datos.

**Características principales:**

- **Escalado automático:** Ajusta de forma automática la capacidad de cómputo, escalando hacia arriba si hay picos de tráfico y hacia abajo, llegando a “pausarse” si hay pocas consultas.
- **Pago por uso:** Solo se paga por la capacidad de cómputo que realmente se usa. Esta capacidad se mide en ACUs (Aurora Capacity Units).
- **Gestión simplificada:** No es necesario calcular el tamaño ni el número de instancias.

!!! tip "Lanzar un clúster de Amazon RDS con Aurora" 
8/14
![Descripción de la imagen](../AWS/ut7/cloudformation/WIP.avif){ .doscinco }<br>

<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/AWS/Base%20Dades/Tema%202/tema2_RDS_Aurora.pdf -->
### **2.2 - Bases de datos NoSQL: Amazon DynamoDB**
<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/AWS/Base%20Dades/Tema%203/tema3_DynamoDB.pdf -->
### **2.3 - ElastiCache**
<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/AWS/Base%20Dades/Tema%204/tema4_ElastiCache.pdf -->
 


 
<br>
   
 
<!-- bbdd         
https://www.youtube.com/watch?v=ciRbXZqBl7M&list=PL9nWRykSBSFithc_PvHAR1MDIFodb2lHd

-->

<!-- route 53... 
cloud formation... 
elastic load balancing
Amazon Simple Storage Service (S3) 
Amazon Elastic File System (EFS)
Amazon Elastic Block Store (EBS) -->
<!--  Building Highly Available Web Application 
https://skillbuilder.aws/learn/2WBTDQFGSV/building-highly-available-web-application/2RW7UC62ZE
 
-->
  
  

 
## **Enlaces de interés**
Documentación de [AWS](https://docs.aws.amazon.com)   
Sistemas de almacenamiento en [AWS](https://aws.amazon.com/es/products/storage/)  
Sistemas de almacenamiento [EFS](https://aws.amazon.com/es/efs/) en AWS.  
Guía del usuario [EFS](https://docs.aws.amazon.com/es_es/efs/latest/ug/mounting-fs.html).  
Control de acceso a [buckets S3](https://docs.aws.amazon.com/es_es/AmazonS3/latest/userguide/about-object-ownership.html?icmpid=docs_amazons3_console)  
Base de datos relacionales [AWS RDS](https://aws.amazon.com/es/rds/)  
Guía del usuario del [AWS RDS](https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/Welcome.html)  
Guía del usuario de [Amazon Aurora](https://docs.aws.amazon.com/es_es/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)  

 
    |**b)** Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube.|20%|
    |**c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.|20%|
 




