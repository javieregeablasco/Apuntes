---
cicle: CFGS - Desarrollo de aplicaciones web
title: "Introducción a la nube pública"
module number: 
lesson: UD. 6 - Equilibrador de carga de red  
author: Javier Egea Blasco  
year: 25-26  
keywords: DAW, Optativa, AWS
layout: default  
schedule: 96h - 3h/s 
---

# **UT. 6 - Interconexión, equilibrado y escalado de infraestructuras**
![Descripción de la imagen](../AWS/ut6/elb.png){ .trescinco }
<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:** |
|-|
| **RA. 3:** Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos.|

|**Criterios de evaluación de la unidad didáctica:**|
|-|
|**d)** Se ha realizado la selección de servicios de computación adecuados según casos de uso.|
|**e)** Se ha llevado a cabo la configuración y gestión de balanceo de carga y escalado automático.|
    

| **Resultados de aprendizaje de la unidad didáctica:** |
|-|
| **RA. 4:** Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento.|

|**Criterios de evaluación de la unidad didáctica:**|
|-|
|**a)** Se ha realizado la diferenciación entre tecnologías de almacenamiento en la nube.|
|**b)** Se ha llevado a cabo la configuración y gestión de bases de datos en un entorno de nube.|
|**c)** Se ha trabajado en la resolución de problemas prácticos sobre almacenamiento y bases de datos.|
|**d)** Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas.|
|**e)** Se ha hecho uso de herramientas de monitoreo y recomendaciones de optimización.|

## **1 - Interconexiones de redes, peering y transit gateway**
En AWS, cada VPC (Virtual Private Cloud) es una red aislada. A veces, necesitamos que dos o más VPCs se comuniquen entre sí (por ejemplo, una VPC de frontend con otra de bases de datos o servicios compartidos).

Para estos casos, AWS ofrece dos mecanismos principales:

- VPC Peering Connection (conexiones directas punto a punto)
- Transit Gateway (conexión centralizada y escalable)



<!-- https://www.youtube.com/watch?v=qMppxz4Ou0A -->
<!-- route 53... 
cloud formation... 
elastic load balancing
Amazon Simple Storage Service (S3) 
Amazon Elastic File System (EFS)
Amazon Elastic Block Store (EBS) -->
<!-- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-stack.html 
Building Highly Available Web Application 
https://skillbuilder.aws/learn/2WBTDQFGSV/building-highly-available-web-application/2RW7UC62ZE
recursos de BBDD y buckets:

https://awsacademy.instructure.com/courses/64697/modules#module_773291
https://awsacademy.instructure.com/courses/64697/modules/items/5723370
https://aws.amazon.com/es/products/storage/
-->


    


<!-- <br>

## **Introducción**
peer connection
transit gateway
escalado automatico
elastic load balancing  -->
<!-- https://www.youtube.com/watch?v=89N3u6W01IQ -->
<!-- https://www.grycap.upv.es/cursocloudaws/contenido.php 
https://luisdieguez.com/tutorial-ansible-desde-0-herramienta-de-gestion-de-servidores/
https://ualmtorres.github.io/SeminarioDockerPresentacion/
https://www.youtube.com/watch?v=qNIniDftAcU
https://www.youtube.com/watch?v=TRLK6ZNpjB8

-->

<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/AWS/Arqui%20y%20despliegues%20en%20AWS/Tema%203/Tema%203.%20NAT%20Gateway,%20reglas%20encadenadas%20y%20subredes%20privadas.pdf -->

 <!-- file:///C:/Users/titan/Documents/Javier128/Modulos/DAW/DAW_2/AWS/UT/UT5/Tema%204/Tema%204.%20Peer%20connection%20y%20transit%20gw.pdf -->

<!-- 

https://www.youtube.com/watch?v=DSkO0ZJ8PxA



https://www.youtube.com/watch?v=lTUUJBa1dp4&list=PLDbrnXa6SAzV0J3Un9jRnbbFpuQH-_y-C&index=11

https://www.youtube.com/watch?v=iAYYssYrGms

https://www.youtube.com/watch?v=CGmTvukObOw -->


## **Enlaces de interés**
Documentación de [AWS](https://docs.aws.amazon.com)
[Elastic Load Balancing](https://docs.aws.amazon.com/es_es/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
https://docs.aws.amazon.com/es_es/vpc/latest/peering/what-is-vpc-peering.html
<!-- https://aws.amazon.com/es/products/storage/ -->