---
cicle: CFGS - Desarrollo de aplicaciones web
title: "Introducción a la nube pública"
module number: 
lesson: UD. 7 - Dockers e introducción a Cloud Formation  
author: Javier Egea Blasco  
year: 25-26  
keywords: DAW, Optativa, AWS
layout: default  
schedule: 96h - 3h/s 
---

# **UT. 6 - Dockers y Cloud Formation**
![Descripción de la imagen](../AWS/ut7/doc-1.webp){ .trescinco }
<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:** |
|-|
| **RA. 3:** Diseña y configura redes virtuales y servicios de cómputo en la nube, aplicando buenas prácticas de seguridad, estrategias de balanceo de carga, escalado automático y aprovechando tecnologías serverless, contenedores y máquinas virtuales según casos de uso específicos.|

|**Criterios de evaluación de la unidad didáctica:**|
|-|
|**d)** Se ha realizado la selección de servicios de computación adecuados según casos de uso.|

| **Resultados de aprendizaje de la unidad didáctica:** |
|-|
| **RA. 4:** Gestiona servicios de almacenamiento y bases de datos en la nube, seleccionando tecnologías adecuadas para casos específicos, y diseña arquitecturas escalables y resilientes utilizando herramientas de monitoreo y optimización para mejorar el rendimiento.|

|**Criterios de evaluación de la unidad didáctica:**|
|-|
|**d)** Se ha diseñado arquitecturas escalables y resilientes basadas en las mejores prácticas.|
|**e)** Se ha hecho uso de herramientas de monitoreo y recomendaciones de optimización.|

## **1 - Docker**
### **1.1 - Introducción**
Docker es una plataforma que permite crear, empaquetar y ejecutar aplicaciones dentro de **contenedores**.  
**Un contenedor** es un entorno aislado que contiene todo lo necesario para ejecutar una aplicación: código, librerías, configuraciones y dependencias.

### **1.2 - ¿Cómo Funciona Docker?**
Docker funciona mediante **imágenes**, **contenedores** y **mecanismos de aislamiento a nivel de sistema operativo** gestionados por el motor de ejecución **Docker engine**.

### **1.3 - Conceptos clave de docker**
![Descripción de la imagen](../AWS/ut7/doc-2.png){ .sietecinco }

- **Docker Engine**  
Docker Engine es el motor de contenedores de Docker. Utiliza funciones del sistema operativo (especialmente del kernel de Linux) para crear entornos aislados llamados contenedores.
    - **Docker Engine está compuesto por:**
        - Docker Daemon (dockerd)
        - Docker CLI
        - API REST de Docker  

    - **Sus funciones principales son:**  
        - Construir imágenes
        - Ejecutar y supervisar contenedores
        - Gestionar redes, volúmenes y almacenamiento
        - Descargar imágenes desde registros (Docker Hub, **AWS ECR**, etc.)


- **Imagen:**  

    - **La imagen** es **una plantilla de solo lectura** que se utiliza para **crear contenedores**. A partir de una imagen pueden crearse **múltiples contenedores**.
    - Las imágenes, además de tener su sistema de ficheros predefinido, tienen una serie de parámetros predefinidos (comandos, de variables de entorno, etc.) con valores por defecto y que se pueden personalizar en el momento de crear el contenedor.
    - **Docker Engine** permite crear nuevas imágenes basándose en imágenes existentes, normalmente mediante un **Dockerfile**.
    - **Una imagen** está formada por **capas** (layers). Al construir **una nueva imagen**, Docker reutiliza las capas de la imagen original y añade **únicamente las capas modificadas**.  
<br>

- **Contenedor (container)**:  
Un contenedor es un paquete ejecutable independiente que incluye todo lo necesario para ejecutar una aplicación: código, tiempo de ejecución, herramientas del sistema, librerías y configuración. Los contenedores comparten el kernel del sistema anfitrión, lo que los hace ligeros y eficientes.  

    - Son instancias ejecutables de una imagen.  
    - Pueden ser creados, arrancados, detenidos, reiniciados y eliminados.
    - Cada contenedor Docker posee un identificador único (ID) de 64 caracteres (normalmente se utiliza la versión corta de 12 caracteres).
    - Los comandos de Docker aceptan tanto el ID completo como el reducido.
    - Es posible referirse a un contenedor usando solo los primeros caracteres de su ID, siempre que dicho prefijo sea único.  
<br>

- **Dockerfile:**  
Un Dockerfile es un archivo de texto que contiene instrucciones para construir una imagen Docker, incluyendo la imagen base, los paquetes necesarios y la configuración del entorno.  
<br>

- **Registro (registry):**  
Las imágenes Docker se almacenan en registros, que actúan como repositorios de imágenes de contenedores. Docker Hub es el registro público más conocido, aunque las organizaciones suelen emplear registros privados como **AWS ECR**.  
<br>

- **Contenerización:**  
El proceso de empaquetar una aplicación y todas sus dependencias en un contenedor se conoce como contenerización. Gracias a ello, los contenedores pueden ejecutarse de forma uniforme en cualquier sistema que disponga de Docker.

### **1.4 - Kubernetes**
Kubernetes es un sistema que gestiona clusters de servidores y se encarga de ejecutar contenedores (normalmente Docker o cualquier imagen compatible con el estándar OCI) de forma:

- Distribuida
- Resiliente
- Escalable
- Automatizada

Fue desarrollado por Google basándose en más de 10 años de experiencia gestionando contenedores internamente (Borg), y actualmente lo mantiene la Cloud Native Computing Foundation (CNCF).  

<br>

#### **1.4.1 - ¿Para qué sirve Kubernetes?**
Kubernetes ayuda a:

- Ejecutar aplicaciones distribuidas en muchos contenedores.
- Escalar de forma automática cuando aumenta la carga.
- Reiniciar contenedores si fallan.
- Distribuir la carga entre múltiples nodos.
- Actualizar versiones de la aplicación sin interrupciones (rolling updates).
- Programar contenedores en nodos disponibles.
- Gestionar redes y almacenamiento persistente para contenedores.

Es decir, permite ejecutar aplicaciones complejas en producción sin preocuparte de la infraestructura paso a paso.

<br>

#### **1.4.2 - Conceptos básicos de Kubernetes**
Lista de los recursos más importantes dentro de un cluster:

1. **Nodo (Node)**  
Máquina física o virtual donde Kubernetes ejecuta contenedores.  
Puede ser:

    - Master node → gestiona el cluster
    - Worker node → ejecuta las aplicaciones

2. **Pod**  
Es la unidad mínima en Kubernetes.  
Un Pod puede contener uno o varios contenedores que funcionan como una unidad.

3. **Deployment**  
Define:
    - Cuántos Pods se necesitan
    - cómo se actualizan
    - cómo se mantienen en ejecución
    - Kubernetes garantiza que el estado deseado coincida con el estado real.

4. **Service**

    - Abstracción de red:
    - Permite que los Pods sean accesibles dentro o fuera del cluster.

Tipos comunes:

- ClusterIP (interno)
- NodePort
- LoadBalancer (externo, usado en nubes como AWS)

5. **Namespace**
Sirve para organizar recursos dentro del cluster (útil en empresas con varios equipos/proyectos).

6. **Volúmenes (Volumes)**
Permiten persistir datos incluso cuando los Pods mueren y se recrean.




## **2 - ¿Cómo desplegar contenedores en AWS?**
AWS ofrece múltiples herramientas para facilitar el trabajo con contenedores. Estas herramientas permiten **almacenar imágenes**, **orquestar contenedores**, **escalar aplicaciones**, y **ejecutarlas sin necesidad de administrar servidores**.

## **2.1 - Amazon ECR (Elastic Container Registry)**
Amazon ECR es un registro de contenedores donde almacenar las imágenes Docker.

**Funciones principales:**

- Almacenar imágenes Docker a nivel empresarial.
- Integración nativa con ECS, EKS, Lambda y CodePipeline.
- Control de acceso mediante IAM.
- Alta disponibilidad y cifrado en reposo.

ECR es el punto de partida para desplegar contenedores en AWS, ya que las imágenes deben estar accesibles desde los servicios que las ejecutan.

## **2.2 - Amazon ECS (Elastic Container Service)**
Amazon ECS es la plataforma de orquestación de contenedores de AWS. Permite ejecutar contenedores Docker en dos modos: **EC2** y **Fargate**.

### **2.2.1 - ECS sobre EC2**
- Los contenedores se ejecutan en instancias EC2 administradas (parcial o totalmente) por el usuario.
- El usuario decide el tamaño, tipo y cantidad de máquinas.
- Dependiendo de la opción elegida, puede requerir aplicar parches, gestionar capacidad y asegurar servidores.

### **2.2.2 - ECS con Fargate**
- Es un servicio **serverless**: no requiere gestionar máquinas.
- Ejecuta contenedores sin preocuparte por **servidores ni escalado**.
- Pago por uso de cada contenedor.
- Ideal para aplicaciones basadas en microservicios o arquitecturas distribuidas.

## **2.3 - Amazon EKS (Elastic Kubernetes Service)**
Amazon EKS permite desplegar contenedores utilizando Kubernetes, el estándar de orquestación más extendido.

- AWS gestiona el control plane.
- El usuario gestiona los nodos (EC2) o Fargate como backend.
- Total compatibilidad con imágenes Docker o de cualquier estándar OCI.
- Es ideal si se necesita mantener compatibilidad con Kubernetes o en un entorno multi-cloud.

## **2.4 - AWS Lambda**
AWS Lambda permite empaquetar funciones en imágenes Docker de hasta 10 GB.

Esto ofrece ventajas como:

- Usar dependencias complejas no soportadas en Lambda tradicional.
- Migrar aplicaciones que ya se ejecutan en contenedores.
- Unificar pipelines de CI/CD basados en Docker.
- Lambda ejecuta el contenedor como una función serverless, sin servidores.

## **2.5 - AWS App Runner**
AWS App Runner es un servicio de alto nivel para desplegar aplicaciones web y APIs directamente desde:  

- Un repositorio de código
- Una imagen Docker en ECR

Es ideal para desarrolladores que quieren centrarse en el código y dejar toda la infraestructura a AWS.

# **3 - ECR**

<!-- https://medium.com/@pankajaswal888/how-to-set-up-and-use-aws-elastic-container-registry-ecr-4add47a93063 -->
<!-- https://dondeaprendoaws.com/blog/como-desplegar-contenedores-en-aws/ -->
<!-- https://dev.to/chinmay13/how-to-push-docker-image-to-public-and-private-aws-ecr-repository-56k5 -->

<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/Docker/CEFIRE/UD6/UD%2006.01%20-%20Docker%20Compose.pdf -->
<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/Docker/CEFIRE/UD5/UD%2005.01%20-%20Redes%20y%20vol%C3%BAmenes%20en%20Docker.pdf -->
<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/Docker/CEFIRE/UD4/UD%2004.01%20-%20Gesti%C3%B3n%20de%20imagenes%20en%20Docker.pdf -->
<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/Docker/CEFIRE/UD3/UD%2003.02%20-%20Docker%20CheatSheet%20-%20Version%20UD03.pdf -->
<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/Docker/CEFIRE/UD3/UD%2003.01%20-%20Principales%20acciones%20con%20Docker.pdf -->

<!-- https://kinsta.com/es/blog/que-es-docker/ -->

#### **1.2.3 - Configuración de la interconexión**
 
#### **1.2.4 - Configuración de la tablas de enrutamiento**

#### **1.2.5 - Configuración de los grupos de seguridad de las instancias**

#### **1.2.6 - Pruebas de conexión**

### **1.3 - Transit Gateway**  

#### **1.3.1 - Escenario**

#### **1.3.2 - Creación del transit gateway**


#### **1.3.3 - Conexiones del transit gateway**

#### **1.3.4 - Modificar las tablas de enrutamiento de las VPC's**


#### **1.3.5 - Pruebas de conexión**

#### **1.3.6 - Pruebas adicionales**
 
### **1.4 - Tarea RA3-CEd**
## **2 - Equilibrado y escalado de infraestructuras**
### **2.1 - Introducción**

### **2.2 - Elastic Load Balancing (ELB)**

#### **2.2.1 - Escenario propuesto**

#### **2.2.2 - Instancias EC2**

#### **2.2.3 - Creación del balanceador de carga**

#### **2.2.4 - Editar los atributos del equilibrador de carga**

#### **2.2.5 - Comprobación del funcionamiento del equilibrador de carga**



<!--

<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/Docker/CEFIRE/UD3/UD%2003.01%20-%20Principales%20acciones%20con%20Docker.pdf -->
<!-- https://docs.aws.amazon.com/hands-on/latest/deploy-docker-containers/deploy-docker-containers.html -->
<!-- file:///C:/Users/titan/Documents/Javier128/Eclipse/Docker/CEFIRE/UD1/UD%2001.01%20-%20Introducci%C3%B3n%20a%20los%20contenedores%20y%20a%20Docker.pdf -->

### **2.3 - Auto Scaling** 

### **2.4 - Contenedores, Elastic Container Service (ECS) en AWS** 

<!-- https://www.youtube.com/watch?v=TRLK6ZNpjB8&list=PLGANiJnCt6o0CFEBUNBEDW-jvDJ2Ri38f 
https://youtu.be/TRLK6ZNpjB8?si=0KdAkFXZ_qHU3ol2&t=631 -->

<!-- texto 
https://dev.to/gbenga700/deploying-a-dockerized-web-application-with-aws-ecs-and-fargate-29bb
https://dondeaprendoaws.com/blog/como-desplegar-contenedores-en-aws/
https://medium.com/containers-on-aws/how-i-do-local-docker-development-for-my-aws-fargate-application-8957e3fdb50 -->

<!-- https://www.youtube.com/watch?v=aLJHB2CuqBU -->
<!-- cluster == compute power -->

<!-- https://www.youtube.com/watch?v=DSf7NWCtolw -->

<!-- https://www.youtube.com/watch?v=86Ys0LnMSnY -->
<!-- https://www.youtube.com/watch?v=qNIniDftAcU -->

### **2.5 - ECS + ELB en AWS** 
<!-- https://docs.aws.amazon.com/es_es/autoscaling/ec2/userguide/tutorial-ec2-auto-scaling-load-balancer.html -->

<!-- bbdd
https://www.youtube.com/watch?v=vp_uulb5phM
https://www.youtube.com/watch?v=eK_umMYxZfM
https://www.youtube.com/watch?v=6E30Yr2UATw
  https://www.youtube.com/watch?v=kNm0z_hRJlw
  https://www.youtube.com/watch?v=wLTFaDebTBY
  https://www.youtube.com/watch?v=BTg1JbmE3x4
  https://www.youtube.com/watch?v=tykcCf-Zz1M -->


<!-- ecs
https://prezi.com/p/5jffku-0bqyl/amazon-elastic-container-service-overview/
https://www.youtube.com/watch?v=TRLK6ZNpjB8
https://www.youtube.com/watch?v=qbEPae8YNbs
https://www.youtube.com/watch?v=NI34uF7VVP8
https://www.youtube.com/watch?v=86Ys0LnMSnY -->
<!-- file:///C:/Users/titan/Documents/Javier128/Modulos/DAW/DAW_2/AWS/UT/UT6/Tema%204/Tema%204.%20Peer%20connection%20y%20transit%20gw.pdf -->

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

https://aws.amazon.com/es/products/storage/ 


https://www.youtube.com/watch?v=lTUUJBa1dp4&list=PLDbrnXa6SAzV0J3Un9jRnbbFpuQH-_y-C&index=11

https://www.youtube.com/watch?v=iAYYssYrGms

https://www.youtube.com/watch?v=CGmTvukObOw -->

 
## **Enlaces de interés**
Documentación de [AWS](https://docs.aws.amazon.com)  
[Docker](https://www.oracle.com/cloud/cloud-native/container-registry/what-is-docker/#docker-explained) explained    
Amazon [Elastic Container Registry](https://docs.aws.amazon.com/es_es/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) Documentation    
[Repositorio privado](https://docs.aws.amazon.com/es_es/AmazonECR/latest/userguide/repository-create.html) de Amazon 
ECR    
