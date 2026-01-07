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
|**d)** Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas.|


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
- Antes de nada crearemos un grupo de seguridad para el EFS y lo configuraremos para que solo acepte conexiones NFS desde las instancias que hemos creado.  
![Descripción de la imagen](./ut8/EFS/efs-3.png){.cien .marco .margintopbottom20} 
 

- Accedemos a los recursos de AWS EFS y creamos nuestro primer EFS.
![Descripción de la imagen](./ut8/EFS/efs-4.png){.cincozero .marco .margintopbottom20} 

- Pulsamos personalizar para ver las diferentes configuraciones disponibles.
    - Paso 1
![Descripción de la imagen](./ut8/EFS/efs-5.png){.sietecinco .marco .margintopbottom20}  
    - Paso 2  
    Elegimos los grupos de seguridad de los puntos de montaje para que el NFS solo acepte conexiones desde las instancias EC2 que hemos creado anteriormente.
![Descripción de la imagen](./ut8/EFS/efs-6.png){.sietecinco .marco .margintopbottom20}  
    - Paso 3  
    Seleccionamos las políticas de acceso que impiden el acceso a la raíz de NFS así como el cifrado en tránsito.
![Descripción de la imagen](./ut8/EFS/efs-7.png){.sietecinco .marco}  
    - Paso 4  
    Revisamos y creamos el NFS.
![Descripción de la imagen](./ut8/EFS/efs-8.png){.sietecinco .marco}  

#### **1.3.5 - Cliente NFS sobre instancias EC2**
!!! warning "Repetiremos los pasos siguientes en cada instancia EC2"

!!! tip "Crear el punto de montaje"
Accedemos a las intancias EC2 y creamos el punto de montaje 
```bash
mkdir ~/efs-punto-montaje
```
![Descripción de la imagen](./ut8/EFS/efs-9.png){.cincozero }  

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

!!! tip "Montar el EFS con el helper de helper de AWS EFS"
Realizaremos el montaje utilizando **el nombre de DNS** del sistema de archivos.

![Descripción de la imagen](./ut8/EFS/efs-12.png){.cien .marco }  
```bash
sudo mount -t efs -o tls fs-0e32c02f9eb3ebd7e.efs.us-east-1.amazonaws.com efs-punto-montaje/ 
```
![Descripción de la imagen](./ut8/EFS/efs-13.png){.cien }  



<!-- 4. Create a file on the file system
5. Add a file system policy to enforce encryption in-transit
6. Unmount (make sure to change directory out of efs-mount-point first)
sudo umount ~/efs-mount-point
4. Mount again using the EFS client (what happens?) -->

 

<!-- trabajar sobre esta:

https://youtu.be/ExM6gaE0708?si=n5OU7lA5IPfRkquU&t=470 -->

<!-- https://youtu.be/aAOC6oS445s?si=C2y71T_qttZtbaK7&t=1061 -->

<!-- https://apuntes.de/aws/elastic-file-storage-system/#gsc.tab=0 -->
<!-- https://www.youtube.com/watch?v=GG8PAAOUGBg -->
<!-- https://apuntes.de/aws-certificacion-csaa/buckets/#gsc.tab=0 -->
<!-- https://aitor-medrano.github.io/iabd2223/cloud/03s3.html -->
 
<br>

#### **5.5.7 - Condiciones de entrega de la tarea RA4-CEe**
!!! warning "Condiciones de la entrega"
    1. Adjuntar a la tarea la plantilla final (tarea guiada + rol IAM + Instalación automática de Nginx).
    1. Realizar capturas de pantalla del mapa de recursos de la VPC desplegada.
    1. Realizar capturas de pantalla del servidor Nginx desplegado.
    1. Comentar brevemente cada captura para entender a qué corresponde y subir el documento a la tarea correspondiente de AULES.


### **5.6 - CloudFormation + IaC + CDK**
![Descripción de la imagen](../AWS/ut7/cloudformation/WIP.avif){ .doscinco }<br>

<!-- apuntes de s3 -->
<!-- https://www.youtube.com/watch?v=9jOdbA1yk4U -->
<!-- https://www.youtube.com/watch?v=mDRoyPFJvlU -->
<!-- https://www.youtube.com/watch?v=C4calFCtlHg -->

    

 
 
<!-- bbdd
https://www.youtube.com/watch?v=vp_uulb5phM
https://www.youtube.com/watch?v=eK_umMYxZfM
https://www.youtube.com/watch?v=6E30Yr2UATw
https://www.youtube.com/watch?v=kNm0z_hRJlw
https://www.youtube.com/watch?v=wLTFaDebTBY
https://www.youtube.com/watch?v=BTg1JbmE3x4
https://www.youtube.com/watch?v=tykcCf-Zz1M -->

<!-- route 53... 
cloud formation... 
elastic load balancing
Amazon Simple Storage Service (S3) 
Amazon Elastic File System (EFS)
Amazon Elastic Block Store (EBS) -->
<!--  Building Highly Available Web Application 
https://skillbuilder.aws/learn/2WBTDQFGSV/building-highly-available-web-application/2RW7UC62ZE
recursos de BBDD y buckets:

https://aws.amazon.com/es/products/storage/
-->
  
  

 
## **Enlaces de interés**
Documentación de [AWS](https://docs.aws.amazon.com)   
Sistemas de almacenamiento en [AWS](https://aws.amazon.com/es/products/storage/)  
Sistemas de almacenamiento [EFS](https://aws.amazon.com/es/efs/) en AWS.  
Guía del usuario [EFS](https://docs.aws.amazon.com/es_es/efs/latest/ug/mounting-fs.html).  


<!-- === "RA 1"
    |RA1. Comprende los fundamentos de la computación en la nube, sus ventajas frente a sistemas tradicionales, el marco de adopción, los principios de migración y los aspectos clave de facturación, como estimación y optimización de costos.||
    |-|-|
    *|**a)** Se ha comprendido los conceptos fundamentales de la computación en la nube.|20%|  
    *|**b)** Se ha demostrado la capacidad para explicar las ventajas de la nube frente a sistemas tradicionales.|20%|  
    *|**c)** Se ha participado en actividades relacionadas con el ecosistema de servicios en la nube.|15%|
    *|**d)** Se han identificado los principios básicos de la facturación y costos en la nube.|15%|
    *|**e)** Se ha hecho uso correcto de herramientas para estimar y gestionar presupuestos.|15%|
    *|**f)** Se ha participado en actividades prácticas sobre gestión de costos.|15%|
      
=== "RA 2"
    |RA2. Identifica los componentes clave de la infraestructura global de la nube, diferenciando servicios principales, regiones, zonas de disponibilidad y aplicando medidas básicas de seguridad como el modelo de responsabilidad compartida, gestión de accesos y protección de datos.||
    |-|-|
    *|**a)** Se ha adquirido conocimiento de los componentes de una infraestructura global en la nube. |20%|
    *|**b)** Se ha demostrado la capacidad para explorar y describir las principales categorías de servicios disponibles.|20%|
    *|**c)** Se ha realizado una evaluación del uso adecuado de servicios básicos en ejercicios prácticos.|15%|
    *|**d)** Se ha comprendido el modelo de responsabilidad compartida en la nube.|15%|
    *|**e)** Se ha aplicado medidas de seguridad básicas mediante herramientas de gestión de acceso.|15%|
    *|**f)** Se han realizado ejercicios sobre gestión de usuarios y políticas de seguridad.|15%|

=== "RA 3"
    |RA3. Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos.||
    |-|-|
    *|**a)** Se ha realizado el diseño y configuración de redes virtuales privadas.|20%|
    *|**b)** Se ha aplicado buenas prácticas de seguridad en redes y arquitecturas.|20%|
    *|**c)** Se ha participado activamente en la creación y configuración de una red funcional.|15%|
    *|**d)** Se ha realizado la selección de servicios de computación adecuados según casos de uso.|15%|
    *|**e)** Se ha llevado a cabo la configuración y gestión de balanceo de carga y escalado automático.|15%|
    *|**f)** Se han desarrollado prácticas relacionadas con la optimización de recursos computacionales.|15%|

=== "RA 4"
    |RA4. Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento.||
    |-|-|
    |**a)** Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube.|20%|
    |**b)** Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube.|20%|
    |**c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.|20%|
    |**d)** Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas.|20%|
    *|**e)** Se ha hecho uso de herramientas de monitoreo y recomendaciones de optimización.|10%|
    *|**f)** Se ha participado en actividades que simulen el análisis y mejora de arquitecturas existentes.|10%| -->