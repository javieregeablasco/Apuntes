---
title: CFGS - Desarrollo de Aplicaciones Web
lesson: UD. 3 - AWS Academy  
author: Javier Egea Blasco  
year: Año 25-26  
keywords: DAW, Optativa, AWS
---

![Descripción de la imagen](../AWS/ut3/awsdemy.png){ .sietecinco }

<br>

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:** |
|-|
| **RA. 1:** Comprende los fundamentos de la computación en la nube, sus ventajas frente a sistemas tradicionales, el marco de adopción, los principios de migración y los aspectos clave de facturación, como estimación y optimización de costos.|  


|**Criterios de evaluación de la unidad didáctica:**|
||
|**d)** Se han identificado los principios básicos de la facturación y costos en la nube.|
|**e)** Se ha hecho uso correcto de herramientas para estimar y gestionar presupuestos.| 

<br>


## **Preliminares**
Descargar una distribución de **Linux ligera** (Lubuntu, Mint) e instalarla sobre una máquina virtual.

## **Learner Lab**
### **Invitación a Learner Lab** 
En vuestros **correos corporativos** habréis recibido un mensaje de **AWS Academy**.

![alt text](../AWS/ut3/invi.png)

Si habéis recibido ese correo, significa que se os ha dado de alta en un laboratorio (Leaner Lab) donde haremos la formación del curso.  
Este laboratorio cuenta con un presupuesto de 50$. Como lo veremos a lo largo del curso, convendrá **administrarlo correctamente**.  
Si se excede el límite de 50$, el acceso quedará bloqueado y no será posible recuperar los trabajos realizados en él.

### **Registro en AWS Academy**
1. Hacer click en **Comenzar** y registraros en el servicio que se indica.
1. Luego os saldrá una ventana que os pedirá de acceder a vuestra cuenta de **Canvas**.  
Si no tenéis cuenta de Canvas, pinchar en **Create my account**.  
<br>
![Descripción de la imagen](../AWS/ut3/canvas.png){ .cincozero }
<br>

1. Un vez registrados, podréis acceder a vuestra cuenta de AWS Academy.  
<br>
![Descripción de la imagen](../AWS/ut3/panel.png){ .cincozero }

### **Acceso al curso**
Pinchar en el curso. Si es la primera vez que usáis el **Learner Lab** sólo os aparecerá un curso.   
<br>
![Descripción de la imagen](../AWS/ut3/login.png){ .cincozero }
<br>

### **Acceder al laboratorio**
1. Seguir el enlace **Launch AWS Acedemy Leaner Lab**.  
<br>
![Descripción de la imagen](../AWS/ut3/course.png){ .cien }
<br>  

1. El siguiente paso será lanzar el laboratorio de AWS.  
Previamente tendremos que conceder permisos y decir que nos hemos leído los términos
de uso.  
<br>
![Descripción de la imagen](../AWS/ut3/terms.png){ .cincozero }
<br>

1. Una vez aceptados los términos y condiciones, esperar a que aparezca el spinner de **vocareum**  
<br>
![Descripción de la imagen](../AWS/ut3/voca.png){ .cincozero }
<br>  

1. Si todo ha ido bien, accederemos al **Learner Lab**.  
<br>
![Descripción de la imagen](../AWS/ut3/learnerlab.png){ .cien }
<br>  

### **Lanzar el laboratorio**
Para poder acceder a la consola de AWS y poder empezar a usar sus servicios pulsaremos **Start Lab**.  
Una vez iniciado, dispondremos de una sesión de 4 horas de duración para hacer las prácticas. Si vemos que nos vamos a quedar cortos de tiempo, siempre podremos pulsar de nuevo **Start Lab** antes de que finalicen las 4 horas.  

<br>
![Descripción de la imagen](../AWS/ut3/llon.png)
<br> 

**Consecuencias de apurar el tiempo del learner lab:**  
1. Se cierra la sesión al llegar al tiempo máximo autorizado.  
2. Todas los servicios se paran, es decir, **dejamos de pagar por utilizarlos**.   
3. **Seguimos pagando por tener creados esos servicios**. Por lo cual, durante las prácticas, **siempre** se deberá eliminar los **servicios** que ya no utilizaremos. 

## **Panel de AWS**
Una vez que el enlace de AWS haya pasado a **color verde**, hacemos clic en él y accederemos al panel de control de AWS.


![Descripción de la imagen](../AWS/ut3/AWSCLI/awspanel.png)
<br>  

!!! Exercice "Ejercicio 1"  
    Localizar vuestras credenciales de usuario.

!!! Exercice "Ejercicio 2"  
    ¿En qué región nos encontramos nada más acceder con nuestra cuenta de alumno a AWS?    
    ¿Podemos acceder a otras regiones como, por ejemplo, España (Madrid)?
    ¿Podemos ver las zonas de disponibilidad dentro de la región que tenemos asignada?



## **Instalar el cliente de AWS CLI**
AWS CLI es el cliente de AWS mediante el cual podremos utilizar la terminal para poder
trabajar con nuestro entorno. 
En el siguiente [enlace](https://docs.aws.amazon.com/es_es/cli/latest/userguide/getting-started-install.html) encontraréis las instrucciones de instalación del CLI de AWS.    

Una vez finalizada la instalación podremos comprobar la versión instalada con el comando:
```bash
~ $ aws --version
```
![Descripción de la imagen](../AWS/ut3/AWSCLI/awsversion.png){ .sietecinco }

## **Introducir las credenciales del laboratorio en el cliente de AWS**
Tenemos el **laboratorio** en marcha y el **cliente** de AWS instalado. Para poder conectarnos desde nuestra máquina a nuestro cliente de AWS (y sobre todo a los servivios que crearemos en él) necesitaremos autenticarnos. Para ello  utilizaremos las credenciales del
laboratorio para configurar nuestro cliente.

1. Credenciales del laboratorio en el apartado AWS Details.  
<br>
![Descripción de la imagen](../AWS/ut3/AWSCLI/awscli1.png){ .cincozero }  
<br>

1. Credenciales de AWS CLI  
<br>
![Descripción de la imagen](../AWS/ut3/AWSCLI/awscli2.png){ .cincozero }  
<br>

1. Para cargar las credenciales del laboratorio en nuestra máquina usaremos **aws configure** y pondremos los datos que nos irá pidiendo.
```bash
~$ aws configure
```
<br>
![Descripción de la imagen](../AWS/ut3/AWSCLI/awsconfig.png){ .original }  
<br>

1. Para finalizar y poder conectarse desde nuestro cliente, haremos lo siguiente:
    - Accedemos a la carpeta **.aws** (creada con aws configure) de nuestra máquina y editamos el archivo **credentials**.  
    ```bash
    ~$ cd .aws
    ~$ .aws/nano credentials
    ```
    <br>
    ![Descripción de la imagen](../AWS/ut3/AWSCLI/awspanelnano.png){ .original }  
    <br>

    
    - A continuación borramos **todo el contenido** y copiamos **toda la información de AWS
Details**.  
<br>
![Descripción de la imagen](../AWS/ut3/AWSCLI/awscredencials.png){ .original }  
<br>

1. Si todo ha ido bien, al ejecutar el comando **aws sts get-caller-identity** nos devolverá:

![Descripción de la imagen](../AWS/ut3/AWSCLI/awssts.png){ .original }  
<br>

**Nota:**   
Habrá que repetir este proceso cada vez que cambie el token de sesión y necesitemos usar comandos de CLI desde nuestra máquina para trabajar sobre nuestra nube de AWS. No suele ser habitual, pero en caso de hacer **un reset del laboratorio** (borrado total de todo el entorno creado) es posible que haya que repetir el proceso. 

<br>
![Descripción de la imagen](../AWS/ut3/AWSCLI/awsreset.png){ .original }  
<br>

## **Cerrar el Learner Lab**
Para cerrar el **Learner Lab** basta con pulsar el botón de **End Lab**.  
Todos los servicios que tengamos se detendrán pero **seguirán existiendo y AWS nos facturará por tenerlos**.

<br>
![Descripción de la imagen](../AWS/ut3/AWSCLI/awsend.png){ .original }  
<br>

## **Costes de los servicios en AWS (y de la nube en general)**
En AWS **la facturación y la optimización de costos** son dos áreas básicas que todo usuario debe conocer para **evitar sorpresas en la factura** y aprovechar mejor los recursos. 

### **Conceptos básicos para la administración de costes en AWS**


* **Modelo de pago por uso**  
  Solo se paga por los recursos que se consumen (horas de cómputo, GB almacenados, transferencias de datos...).

* **Niveles gratuitos (Free Tier)**  
  AWS ofrece un nivel gratuito con ciertos límites (por ejemplo, 750 h/mes en EC2 t2.micro durante 12 meses) para aprender y probar servicios.

* **Precios regionales**  
  El coste puede variar entre regiones.


 
### **Consola de Billing & Cost Management**
  Desde la consola de AWS se puede:

  * Ver facturas detalladas por servicio y por región.
  * Configurar presupuestos y alertas.
  * Descargar informes para análisis.

### **Planes y estrategias de uso**  
En AWS existen varios **planes y estrategias de uso** que permiten **optimizar los costes**, es decir, pagar menos por un mismo recurso. 

#### **Instancias bajo demanda (On-Demand)**
* Se paga por **hora o segundo de uso**, sin compromisos a largo plazo.
* **Ventaja:** flexibilidad máxima, perfecto para cargas variables o temporales.
* **Desventaja:** es más caro que otros planes si el uso es continuo.

#### **Instancias reservadas (Reserved Instances, RI)**
* Compromiso a usar una instancia **por 1 o 3 años**, a cambio de un **descuento significativo** (30–70 %).
* **Tipos de pago:**
    1. Pago completo por adelantado: → máximo descuento.
    1. Pago parcial: → descuento medio.
    1. Pago mensual: → descuento menor, más flexible.
* **Ventaja:** ideal para cargas estables y continuas.
* **Desventaja:** compromiso a largo plazo.

#### **Savings Plans**
* Son similares a las RIs, pero más **flexibles**: no se está ligado a una instancia concreta.
* Compromiso a gastar **cierta cantidad de dinero** durante 1 o 3 años para obtener descuentos.
* **Tipos:**

    1. **Compute Savings Plans:** → se aplica a cualquier tipo de instancia EC2, incluso regiones o familias distintas.
    1. **EC2 Instance Savings Plans:** → descuentos específicos para una familia de instancias en una región.  

* **Ventaja:** combina ahorro y flexibilidad.

#### **Instancias Spot (Spot Instances)**
* Son **instancias sobrantes de AWS** que se venden a precio reducido (hasta 90 % más barato que On-Demand).
* **Ventaja:** muy barato para cargas **flexibles o tolerantes a interrupciones**, como procesamiento batch o pruebas.
* **Desventaja:** AWS puede interrumpir la instancia si necesita la capacidad.

#### **Optimización de almacenamiento y servicios adicionales**
Aunque no son “planes de uso” como tal, se combinan con ellos para reducir costes:
* **S3 Storage Classes:** Standard, Standard-IA, Glacier → para ajustar coste según frecuencia de acceso.
* **Lifecycle policies:** mover archivos automáticamente entre tipos de almacenamiento según antigüedad.
* **Auto Scaling:** encender y apagar instancias automáticamente según demanda.

#### **Resumen**

| Plan/Servicio               | Cuándo usarlo                    | Descuento/ventaja principal      |
| --------------------------- | -------------------------------- | -------------------------------- |
| On-Demand                   | Uso temporal o variable          | Flexibilidad máxima              |
| Reserved Instances          | Cargas estables y continuas      | 30–70 % de descuento             |
| Savings Plans               | Uso estable pero flexible        | Ahorro y flexibilidad combinados |
| Spot Instances              | Procesos batch o interrumpibles  | Hasta 90 % más barato            |
| Optimización almacenamiento | Datos según frecuencia de acceso | Reduce costes de almacenamiento  |

### **Aspectos básicos de la optimización de costos**

<!-- https://www.ackstorm.com/blog/herramientas-costes-aws/ 


---
https://dondeaprendoaws.com/blog/gestion-de-facturacion-de-aws-guia-completa/

https://www.prosperops.com/blog/aws-billing-and-cost-management/
https://www.cloudkeeper.com/aws-billing-cost-management

---
https://vergaracarmona.es/apuntes-aws-y-resumen-de-sus-servicios/#costes

38.1. - Administración de costes
• Cost Explorer: Una buena vista de todos los costes de AWS. Importante revisarlo
periódicamente y crear alguna alarma, para controlar los costes mensuales
• Budgets: Añade o crea presupuestos y alarmas para avisarte cuando tus costes pasan de un
umbral.
• Marketplace Subscriptions: Aquí dispones de todo un catálogo de soluciones de terceros,
listos para usar con la tecnología AWS, por ejemplo suscripciones de PFsese, Citrix,
Microsoft o distribuciones específicas de linux.
• ABC: AWS Billing Conductor es más fácil que nunca para los equipos de FinOps
configurar, generar y compartir las tarifas correctas con los usuarios finales,
independientemente de las tarifas que el cliente haya negociado con AWS

---

https://aws.amazon.com/es/getting-started/hands-on/control-your-costs-free-tier-budgets/?ref=gsrchandson&id=itprohandson
---
---




* **Elegir el tamaño adecuado de recursos**
  No usar instancias sobredimensionadas ni almacenamiento innecesario.
  → *Right-sizing*: ajusta el recurso al uso real.

* **Apagar o eliminar recursos no usados**
  Instancias EC2, volúmenes EBS, direcciones IP elásticas o snapshots olvidados generan costes aunque no se usen.

* **Reservar instancias**
  Para cargas estables puedes usar **Reserved Instances** o **Savings Plans**, que ofrecen descuentos del 30-70 % a cambio de un compromiso a 1 o 3 años.

* **Usar instancias Spot**
  Para trabajos flexibles o batch puedes usar instancias Spot (sobrantes) con descuentos de hasta el 90 %.

* **Optimizar almacenamiento**

  * S3 ofrece clases de almacenamiento más baratas para datos poco accedidos (*S3 Glacier*, *S3 Infrequent Access*).
  * Hacer *lifecycle policies* para mover datos automáticamente.

* **Elegir bien la región**

  * Algunas regiones son más baratas que otras.
  * También influye la latencia y las normativas.

* **Monitorizar y poner alertas**
  Configurar en Billing → *Budgets* y *Cost Anomaly Detection* para recibir avisos si los gastos superan un umbral.

---

## 3️⃣ Buenas prácticas generales

* Revisar la **AWS Pricing Calculator** antes de desplegar.
* Activar el **Cost Explorer** para analizar tendencias de gasto.
* Etiquetar recursos (*tags*) para saber a qué proyecto o departamento pertenece cada coste.
* Automatizar la limpieza de recursos huérfanos.

¿Quieres que te prepare una **actividad práctica** para que el alumnado explore la consola de facturación y configure alertas de presupuesto en AWS? (sirve mucho para interiorizar estos conceptos).


-->
## **Tarea 1 - Creación de una alerta de costes**
Ir a **Administración de facturación y costos** y crear una alerta de costos con las siguientes condiciones.  

1. Umbral de coste alcanzado: 5$.
2. Frecuencia de las alertas: Resúmenes semanales.


## **Enlaces de interés**
Documentación de [AWS](https://docs.aws.amazon.com).  
[Aspectos básicos de control de costes en AWS](https://aws.amazon.com/es/getting-started/cost-optimization-essentials)  
[Supervision y control de costes](https://docs.aws.amazon.com/es_es/res/latest/ug/cost-management.html)  
Tutorial para controlar los [costos de AWS](https://aws.amazon.com/es/getting-started/hands-on/control-your-costs-free-tier-budgets/?ref=gsrchandson&id=itprohandson)  
[Calculadora de costos](https://calculator.aws/#/)  