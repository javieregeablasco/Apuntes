---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Aplicaciones ofimáticas
module number: 0223
lesson: UD. 8 - Agenda electrónica y comunicación  
author: Javier Egea Blasco  
year: 25-26  
keywords: SMX, AO
layout: default  
schedule: 224h - 7h/w
---

![Descripción de la imagen](./08-correo/img/correo-1.png){ .sietecinco .marginbottom40 }

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:** |
| :--- |
| **RA8. Realiza operaciones de gestión del correo y la agenda electrónica, relacionando necesidades de uso con su configuración.** |

|**Criterios de evaluación de la unidad didáctica:**||
|-|-|
|**a)** Se han descrito los elementos que componen un correo electrónico.|5%|
|**b)** Se han analizado las necesidades básicas de gestión de correo y agenda electrónica.|20%|
|**c)** Se han configurado distintos tipos de cuentas de correo electrónico.|20%|
|**d)** Se han conectado y sincronizado agendas del equipo informático con dispositivos móviles.|15%|
|**e)** `Se ha operado con la libreta de direcciones.`|5%|
|**f)** Se ha trabajado con todas las opciones de gestión de correo electrónico (etiquetas, filtros, carpetas, entre otros).|30%|
|**g)** `Se han utilizado opciones de agenda electrónica.`|5%|

!!! warning "Nota:"
    El criterio de evaluación **e)** `Se ha operado con la libreta de direcciones.` y **g)** `Se han utilizado opciones de agenda electrónica.` serán evaluados durante la FCT.

## 1 - Introducción

En esta unidad didáctica se van a tratar los aspectos relacionados con la gestión del correo electrónico y la agenda electrónica. Se analizarán las necesidades básicas de gestión de correo y agenda electrónica, se configurarán distintos tipos de cuentas de correo electrónico, se conectarán y sincronizarán agendas del equipo informático con dispositivos móviles, se operará con la libreta de direcciones, se trabajará con todas las opciones de gestión de correo electrónico (etiquetas, filtros, carpetas, entre otros) y se utilizarán opciones de agenda electrónica.

<!-- https://fricardoac.wordpress.com/wp-content/uploads/2015/02/aplicaciones-ofimaticas-2013-grado-medio-mcgraw-hill.pdf -->
<!-- https://www.youtube.com/playlist?list=PLsn5l7yNsIbUUJTfswpCdcIMYHGbEhG13 -->

## 2 - El correo electrónico

El correo electrónico es uno de los sistemas de comunicación más utilizado en el ámbito profesional y personal. Permite enviar y recibir mensajes de texto, archivos adjuntos, imágenes, entre otros. Para utilizar el correo electrónico es necesario configurar una cuenta de correo electrónico en un cliente de correo electrónico o en un servicio de correo electrónico en línea.

Existen otros sistemas de comunicación instantánea como el chat, las videollamadas, entre otros, pero el correo electrónico sigue siendo una herramienta fundamental para la comunicación en el ámbito profesional y personal.

### 2.1 - Funcionamiento del correo electrónico

El correo electrónico funciona a través de un sistema de servidores de correo electrónico que se encargan de enviar y recibir los mensajes de correo electrónico. Cuando un usuario envía un mensaje de correo electrónico, el mensaje se envía al servidor de correo electrónico del remitente, que luego lo envía al servidor de correo electrónico del destinatario. El servidor de correo electrónico del destinatario recibe el mensaje y lo almacena en la bandeja de entrada del destinatario, donde el destinatario puede acceder a él.

### 2.2 - Sistemas involucrados en el correo electrónico

El correo electrónico involucra varios sistemas, entre ellos:

**Fase de envío:**

- **Mail User Agent (MUA):** Es el sistema que permite a los usuarios enviar y recibir mensajes de correo electrónico. Es el cliente de correo electrónico que se utiliza para acceder al correo electrónico, como Microsoft Outlook, Google Gmail, entre otros.
- **Protocolos de correo electrónico:** Son los protocolos que se utilizan para enviar y recibir mensajes de correo electrónico. Los protocolos más comunes son **SMTP (Simple Mail Transfer Protocol), POP3 (Post Office Protocol version 3) e IMAP (Internet Message Access Protocol)**.

**Fase de recepción:**

- **Mail Transfer Agent (MTA):** Es el sistema encargado de enviar y recibir los mensajes de correo electrónico entre los servidores de correo electrónico. Es el sistema que se encarga de enrutar los mensajes de correo electrónico desde el servidor de correo electrónico del remitente hasta el servidor de correo electrónico del destinatario.
- **Seguridad y filtrado:** Es el sistema encargado de proteger el correo electrónico de posibles amenazas, como el spam, los virus, entre otros.
- **Mail Delivery Agent (MDA):** Es el sistema encargado de entregar los mensajes de correo electrónico a la bandeja de entrada del destinatario. 
- **Acceso al correo electrónico (IMAP/POP3):** Es el sistema que permite a los usuarios acceder a su correo electrónico a través de un cliente de correo electrónico o un servicio de correo electrónico en línea.

<!-- https://especialistashosting.com/blog/2016/12/como-funciona-el-correo-electronico/ -->
<!-- https://mailtrap.io/es/blog/smtp-relay/ -->
<!-- https://thecustomizewindows.com/2024/01/basics-of-mail-server-and-mail-transfer-agent-mta/ -->
<!-- https://www.google.com/search?client=firefox-b-d&hs=jHpp&sca_esv=3952bdc93efbafc6&sxsrf=ANbL-n4HybHTh7zLbfmHuZ1DmlntfPij5w:1777877403730&udm=2&fbs=ADc_l-bpk8W4E-qsVlOvbGJcDwpn60DczFdcvPnuv8WQohHLTaMb_WtLz8zQ41bNqiqMK_1FsVyo-5Z6JkhWuoPGkuRh7kwNpMSz91P5qhCEeQU0Q3JTMFazRYDiEAFxt0cgIaVJpgiwnJb72GZ6k_50xgNLITeRl5dfn7ULiOKPl8BmjMvqRdEVWIO1ZEwcVx284lL0cwJP8hwioVBEzBNX1w4wyvGgFA&q=mda+mua+servidor&sa=X&ved=2ahUKEwj75Om4hZ-UAxVnVqQEHXCqL9AQtKgLegQIFhAB&biw=1920&bih=904&dpr=1#sv=CAMSVhoyKhBlLWRabVN4VW1BT2VpV05NMg5kWm1TeFVtQU9laVdOTToOWkZhM0lFbEo4VzVxVU0gBCocCgZtb3NhaWMSEGUtZFptU3hVbUFPZWlXTk0YADABGAcg_Z3CowdKCBABGAEgASgB -->

| **Licencia Creative Commons:** | |
| - | - |
| ![alt text](../../../assets/by-nc-nd-eu_.png) | **Reconocimiento-NoComercial-CompartirIgual CC BY-NC-SA:**  No se permite un uso comercial de la obra original ni de las posibles obras derivadas, la distribución de la cuales se debe hace con una licencia igual a la que regula la obra original. |
