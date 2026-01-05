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
![Descripción de la imagen](../AWS/ut8/ut8-1.png){ .trescinco }
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

Los sistemas de almacenamiento en AWS se dividen principalmente en cuatro grandes categorías, en función de cómo se accede a los datos y del tipo de uso al que están orientados:

- **Almacenamiento de objetos**: Amazon S3 (buckets S3), orientado a datos altamente escalables como imágenes, vídeos o copias de seguridad.
- **Almacenamiento en bloques**: Amazon EBS (ya visto en una unidad anterior), utilizado como discos persistentes que se adjuntan a instancias EC2.
- **Almacenamiento de archivos**: Amazon EFS, que proporciona sistemas de archivos compartidos accesibles desde múltiples instancias.
- **Soluciones híbridas**: AWS Storage Gateway, que permite integrar infraestructura local con servicios de almacenamiento en la nube de AWS.

<!-- https://openwebinars.net/blog/almacenamiento-en-aws/ -->
<!-- https://apuntes.de/aws-certificacion-csaa/buckets/#gsc.tab=0 -->
<!-- https://aitor-medrano.github.io/iabd2223/cloud/03s3.html -->

https://apuntes.de/aws-certificacion-csaa/buckets/#gsc.tab=0

### **1.2 - ¿Cómo Funciona Docker?**

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

    k -->

 
 
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