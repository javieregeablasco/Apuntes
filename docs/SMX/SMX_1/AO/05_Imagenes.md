---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Aplicaciones ofimáticas
module number: 0223
lesson: UD. 6 - Tratamiento de imágenes  
author: Javier Egea Blasco  
year: 25-26  
keywords: SMX, AO
layout: default  
schedule: 224h - 7h/w
---

![Descripción de la imagen](./img/UT5/img-1.png){ .doscinco .marginbottom40 }

|**Resultados de aprendizaje de la unidad didáctica:**|
|:-|
|**RA. 5:** Manipula imágenes digitales analizando las posibilidades de distintos programas y aplicando técnicas de captura y edición básicas.|

|Criterios de evaluación de la unidad didáctica:|
|:-|
|**a)** Se han analizado los distintos formatos de imágenes.|
|**b)** Se ha realizado la adquisición de imágenes con periféricos.|
|**c)** Se ha trabajado con imágenes a diferentes resoluciones, según su finalidad.|
|**d)** Se han empleado herramientas para la edición de imagen digital.|
|**e)** Se han importado y exportado imágenes en diversos formatos.|

## 1 - Introducción

Disponemos de muchos formatos de imagenes. Algunos se estan popularizando con el auge de las nuevas tecnologías, como el formato EebP, mientras que otros formatos como el GIF o el TIFF se han quedado un poco atrás.  
Las imágenes digitales son una parte fundamental de la informática y se utilizan en una amplia variedad de aplicaciones, desde la edición de fotografías hasta el diseño gráfico y la creación de contenido multimedia. En esta unidad didáctica, se explorarán los conceptos básicos relacionados con las imágenes digitales, incluyendo los formatos de archivo, la adquisición de imágenes, la resolución y las herramientas de edición.

## 2 - Tipos de imágenes digitales

Las imágenes digitales se pueden clasificar en dos categorías principales: imágenes **rasterizadas** y imágenes **vectoriales**.  
Las imágenes rasterizadas están compuestas por **píxeles**, mientras que las imágenes vectoriales están formadas por **código** que define la imagen. Ambos tipos de imágenes tienen sus propias ventajas y desventajas como se muestra en la siguiente tabla:

| Tipo de imagen | Ventajas | Desventajas |
| --- | --- | --- |
| Rasterizada | - Ideal para fotografías y gráficos con muchos detalles. <br> - Es compatible con la mayoría de los programas de edición de imágenes. | - La calidad de la imagen puede degradarse al ampliarla. <br> - El tamaño del archivo puede ser grande, especialmente para imágenes de alta resolución. |
| Vectorial | - Es ideal para gráficos y logotipos que requieren escalabilidad. <br> - El tamaño del archivo suele ser más pequeño que el de las imágenes rasterizadas. | - No es adecuada para fotografías o gráficos con muchos detalles. <br> - Puede no ser compatible con algunos programas de edición de imágenes. |

!!! Exercise "Ejercicio"
    - Descargar las imagenes de los siguientes enlaces:  
    [imagen svg](./img/UT5/imagensvg.svg)  
    [imagen raster](./img/UT5/img-2.png)  
    - Escalar las imágenes.
    - Evidenciar la perdida de resolución de la imagen rasterizada.

## 2 - Formatos de imagen

### 2.1 - Formatos de imagenes rasterizadas (raster)

También conocidas como Mapas de Bits (bitmap) están compuestas por una cuadrícula de píxeles individuales. Su principal limitación es que pierden calidad al ampliarse, mostrándose borrosas o "pixeladas".  

Los formatos más comunes incluyen JPG/JPEG, PNG, GIF, TIFF, WebP y RAW, cada uno con sus propias características y usos específicos.

#### 2.1.1 - Formato JPG y JPEG

![imagen](./img/UT5/img-3.png){ .leftunocero .margintop10 .marginbottom20}

El formato JPEG (Joint Photographic Experts Group) es un formato de imagen muy común debido a su eficiencia en la compresión de imágenes fotográficas.  

Utiliza **compresión con pérdida**, al reducir el tamaño del archivo eliminando información de la imagen que el ojo humano no puede percibir fácilmente.

#### 2.1.2 - Formato PNG

![imagen](./img/UT5/img-4.webp){ .leftunodos .margintop10 .marginbottom20}

El formato PNG (Portable Network Graphics) destaca por la posibilidad de **comprimir imágenes sin pérdidas** y de ofrecer una profundidad de color de hasta 24 bits por píxel.  

El formato PNG soporta tanto la transparencia como la semitransparencia (gracias al canal alfa integrado).  
A causa del proceso de compresión sin pérdidas, los archivos son relativamente grandes, hecho que deberemos tener en cuenta a la hora de realizar documentos.

#### 2.1.3 - Formato BMP

![imagen](./img/UT5/img-5.webp){ .leftunodos .margintop10 .marginbottom20}

El formato BMP (Windows bitmap), inicialmente desarrollado para sistemas operativos Microsoft e IBM es un formato de almacenamiento para mapas de bits con una profundidad de color de hasta 24 bits por píxel.

El formato de imagen sin comprimir asigna a cada píxel un valor cromático, por lo que los archivos suelen ser muy grandes, motivo por el que el formato no es adecuado para su uso en aplicaciones ofimáticas.

#### 2.1.4 - Formato GIF

![imagen](./img/UT5/img-6.webp){ .leftunodos .margintop10 .marginbottom20}

El formato GIF (Graphics Interchange Format) es un formato de imagen rasterizada que utiliza compresión sin pérdidas (LZW) y está limitado a 8 bits, es decir, hasta 256 colores.

Aunque esta limitación reduce su capacidad para representar imágenes complejas, puede ayudar a disminuir el tamaño del archivo en algunos casos.

Su principal ventaja es que permite animaciones, lo que lo hace popular para contenido visual dinámico.

#### 2.1.5 - Formato HEIF

![imagen](./img/UT5/img-7.png){ .leftunodos .margintop10 .marginbottom20}

El formato HEIF (High Efficiency Image Format) no es ampliamente utilizado, aunque tiene potencial debido a su eficiencia en la compresión de imágenes (mayor calidad y menor tamaño que JPEG).

HEIF es más común en dispositivos móviles, especialmente en productos de Apple, donde se usa por defecto para capturar fotos.

#### 2.1.6 - Formato WebP

![imagen](./img/UT5/img-8.png){ .leftunodos .margintop10 .marginbottom20}

El formato WEBP es una alternativa relativamente nueva y fue desarrollada por Google. Este formato utiliza una combinación de compresión sin pérdida y con pérdida para lograr tamaños de archivo más pequeños que los formatos de imagen anteriores.

El formato WEBP es **compatible con transparencia** y es compatible con imágenes animadas.

#### 2.1.7 - Formato TIFF

![imagen](./img/UT5/img-9.webp){ .leftunodos .margintop10 .marginbottom20}

Archivo de muy alta calidad y sin pérdida, utilizado fundamentalmente en la industria de impresión profesional debido a su gran tamaño. No se recomienda su uso en aplicaciones ofimáticas debido a su gran tamaño, aunque es ideal para la edición de imágenes de alta calidad.

#### 2.1.8 - Formato RAW

![imagen](./img/UT5/img-10.jpg){ .leftunodos .margintop10 .marginbottom20}

Contiene los datos "crudos" del sensor de la cámara sin procesar. Ofrece la máxima flexibilidad para la edición profesional, aunque genera archivos muy pesados. No es adecuado para su uso en aplicaciones ofimáticas, aunque es ideal para la edición de imágenes de alta calidad.

### 2.2 - Formatos de imagenes vectoriales

#### 2.2.1 - Formato SVG

![imagen](./img/UT5/img-11.webp){ .leftunodos .margintop10 .marginbottom20}

El formato SVG (Scalable Vector Graphics) es un formato de imagen vectorial **basado en XML** que soporta **transparencia y animaciones**.

Esto permite que las imágenes sean escalables sin perder calidad haciendolas ideales para gráficos e iconos de alta calidad en diferentes tamaños y resoluciones.

#### 2.2.2 - Formato EPS

![imagen](./img/UT5/img-12.png){ .leftunodos .margintop10 .marginbottom20}

El formato EPS (Encapsulated PostScript) se utiliza para guardar ilustraciones o trabajos de diseño gráfico en programas de ilustración como Adobe Illustrator y CorelDraw.

Utilizado principalmente en gráficos profesionales es útil para crear imágenes de alta calidad.

#### 2.2.3 - Formato PDF

![imagen](./img/UT5/img-13.webp){ .leftunodos .margintop10 .marginbottom20}

El formato PDF (Portable Document Format) es muy familiar como formato de documento, pero también puede utilizarse para guardar imágenes e ilustraciones.

Un archivo PDF se basa en el mismo lenguaje PostScript que el EPS. Es un vector con compresión sin pérdidas, lo que te permite ampliar una imagen PDF tanto como uno desea.

También es posible incluir elementos interactivos en un PDF, por ejemplo, enlaces y botones.

## 3 - Tarea RA4-CEa Formatos de imágenes

### 3.1 - Preguntas tipo test

!!! warning "Trabajo a realizar"
    - Para esta evaluación, deberéis responder a 20 preguntas tipo test.
    <!-- - Podéis descargar el archivo de texto desde el siguiente [enlace](./05_imagenes/tareas/RA5%20CEa.odt) -->
    - Subrayar la respuesta que consideráis correcta.

### 3.2 - Entrega de la tarea

!!! warning "Condiciones de entrega de la tarea"
    - Guardar el documento con RA5-CEa-NombreApellidos en formato **odt**, **formato nativo** de LibreOffice writer.
    - **No se aceptará ningun formato que no sea odb**.  
    - Subir la base de datos, a la tarea RA5-CEa de **Aules**.
    - A partir de momento de apertura de la tarea, dispondréis de **20 minutos** para subir vuestros trabajos. Pasado ese tiempo la tarea se cerrará y ya no será posible subir vuestras respuestas.

## 4 - Editor de imágenes digitales GIMP

GIMP (GNU Image Manipulation Program) es un programa de edición de imágenes digitales de código abierto y gratuito. Es una alternativa popular a programas comerciales como Adobe Photoshop. GIMP ofrece una amplia gama de herramientas y funciones para la manipulación de imágenes, incluyendo retoque fotográfico, composición de imágenes, creación de gráficos y mucho más.

### 4.1 - Descarga e instalación de GIMP

- Seguir el siguiente enlace para descargar GIMP: [https://www.gimp.org/downloads/](https://www.gimp.org/downloads/)
- Seleccionar la versión adecuada para tu sistema operativo (Windows, macOS o Linux).
- Seguir las instrucciones del asistente de instalación.

### 4.2 - Funciones básicas de GIMP




| **Licencia Creative Commons:** | |
| - | - |
| ![alt text](../../../assets/by-nc-nd-eu_.png) | **Reconocimiento-NoComercial-CompartirIgual CC BY-NC-SA:**  No se permite un uso comercial de la obra original ni de las posibles obras derivadas, la distribución de la cuales se debe hace con una licencia igual a la que regula la obra original. |