---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Aplicaciones ofimáticas
module number: 0223
lesson: UD. 6 - Captura y edición de videos  
author: Javier Egea Blasco  
year: 25-26  
keywords: SMX, AO
layout: default  
schedule: 224h - 7h/w
---

![Descripción de la imagen](./img/UT5/img-1.png){ .doscinco .marginbottom40 }

|**Resultados de aprendizaje de la unidad didáctica:**|
|:-|
|**RA. 6:** Manipula secuencias de video analizando las posibilidades de distintos programas y aplicando técnicas de captura y edición básicas.|

|Criterios de evaluación de la unidad didáctica:|
|:-|
|**a)** Se han reconocido los elementos que componen una secuencia de video.|
|**b)** Se han estudiado los tipos de formatos y códecs más empleados.|
|**c)** Se han importado y exportado secuencias de video.|
|**d)** Se han capturado secuencias de video con recursos adecuados.|
|**e)** Se han elaborado video tutoriales.|

## 1 - Introducción

El vídeo digital es una parte fundamental de la informática moderna y se utiliza en una amplia variedad de aplicaciones, desde el streaming en plataformas digitales hasta la videoconferencia o la creación de contenido en redes sociales.  
En esta unidad didáctica, se explorarán los conceptos básicos relacionados con el vídeo digital (códecs, framerate, resolución...).

## 2 - Tipos de vídeo digital

- Una de las clasificaciones más importantes del vídeo digital se basa en su método de escaneo: vídeo progresivo y vídeo entrelazado.

- El **vídeo progresivo** muestra todas las líneas de cada fotograma de forma secuencial en un mismo instante, mientras que el **vídeo entrelazado** divide cada fotograma en dos campos (líneas pares e impares) que se muestran en momentos alternos.  
!!! tip "Ejemplo de exploración entrelazada"
    ![Descripción de la imagen](./img/UT6/vid-1.webp){ .margintopbottom10 }
- En la actualidad, el formato predominante es el **progresivo**, ya que se adapta mejor a las pantallas digitales modernas y evita los artefactos visuales propios del entrelazado.  
!!! tip "Ejemplo de diferencias de nitidez entre exploración progresiva y entrelazada (efecto combing)"  
    ![Descripción de la imagen](./img/UT6/vid-2.webp){ .margintopbottom10 }

### 3 - Fomato de video digital

El formato de vídeo digital define cómo se representa, codifica y almacena un vídeo. Incluye parámetros como resolución, tasa de fotogramas, bitrate, códec y otros aspectos relacionados con la calidad y el tamaño del archivo.

#### 3.1 Resolución y relación de aspecto

##### 3.1.1 - Resolución

La resolución indica el número de píxeles que componen cada fotograma (ancho × alto).
![Descripción de la imagen](./img/UT6/vid-3.webp){ .margintopbottom10 }

!!!tip "Resolución de 720 (HD)"
Es la resolución más baja considerada HDTV (1280 × 720 píxeles). Se utiliza para contenido ligero o web, aunque hoy en día resulta limitada, ya que la mayoría de pantallas soportan resoluciones superiores.

!!!tip "Resolución de 1080 (Full HD)"
La resolución 1920 × 1080 píxeles, conocida como Full HD, es el estándar más extendido. Ofrece buena calidad de imagen con un tamaño de archivo moderado y es habitual en televisores y dispositivos móviles.

!!!tip "Resolución de 2K o QHD (Quad High Definition)"
Incluye resoluciones como 2048 × 1080 (2K) y 2560 × 1440 (QHD). Proporciona mayor detalle y permite más flexibilidad en edición, reencuadre y uso en pantallas grandes.

!!!tip "Resolución de 4K (Ultra HD)"
La resolución 3840 × 2160 píxeles (UHD) ofrece gran nivel de detalle. Es útil especialmente en edición y postproducción, ya que permite recortar o ajustar la imagen sin pérdida notable de calidad.

!!!tip "Resolución de 8K"
Con 7680 × 4320 píxeles, es una resolución muy alta poco utilizada en consumo. Se emplea principalmente en producción profesional para efectos visuales y reencuadres sin pérdida de calidad.

##### 3.1.2 - Relación de aspecto

La relación de aspecto es la proporción entre el ancho y el alto de una imagen, expresada como dos números (por ejemplo, 16:9 o 4:3).

No indica la calidad, sino la forma del vídeo (horizontal, vertical o cuadrada).
![Descripción de la imagen](./img/UT6/vid-5.png){ .margintopbottom10 }

!!!tip "Relaciones de aspecto habituales"
    !!!info "1:1 (Cuadrado)"
        Formato equilibrado, común en redes sociales.

    !!!info "9:16 (Vertical)"
        Formato móvil por excelencia. Usado en TikTok, Reels, Stories y Shorts.

    !!!info "16:9 (Panorámico)"
        Estándar actual en televisión, YouTube y contenido digital.

    !!!info "16:10"
        Similar a 16:9 pero ligeramente más alto. Común en monitores de ordenador y productividad.

    !!!info "4:3 (Clásico)"
        Formato antiguo de televisión. Hoy en desuso.

    !!!info "5:4"
        Formato cercano al cuadrado, usado en monitores antiguos. Poco habitual actualmente.

    !!!info "1.85:1 (Cinematográfico estándar)"
        Muy utilizado en cine. Similar a 16:9 pero ligeramente más ancho.

    !!!info "2.35:1 (Cinematográfico panorámico)"
        Formato muy ancho típico del cine moderno (CinemaScope). Sensación más épica.

    !!!info "21:9 (Ultrapanorámico)"
        Versión comercial del formato cinematográfico. Usado en monitores y cine.

#### 3.2 - Codificación y descodificación de vídeo digital

Para codificar y decodificar la información de vídeo se utilizan los códecs (codificador/descodificador), que son algoritmos encargados de comprimir y descomprimir los datos audiovisuales.

Su función es reducir el tamaño del archivo sin perder una calidad significativa, lo que resulta esencial para el almacenamiento, la edición y la transmisión en streaming.

##### 3.2.1 - Tipos de compresión en vídeo

La compresión que aplican los códecs modernos se basa principalmente en dos técnicas complementarias:

- **Compresión espacial** (intra-frame):  
Reduce la información dentro de un mismo fotograma eliminando redundancias entre píxeles. Se comprimen zonas con colores o patrones similares.
- **Compresión temporal** (inter-frame):  
Aprovecha la similitud entre fotogramas consecutivos, almacenando solo los cambios entre ellos en lugar de cada imagen completa.

##### 3.2.2 - Codecs de vídeo

Un códec de vídeo (codificador/descodificador) es un algoritmo encargado de comprimir y descomprimir datos de vídeo digital.

Su objetivo principal es reducir el tamaño de los archivos manteniendo la mayor calidad posible, facilitando así su almacenamiento, edición y transmisión.

Los códecs trabajan eliminando información redundante tanto dentro de cada fotograma (compresión espacial) como entre fotogramas consecutivos (compresión temporal). Gracias a esto, permiten manejar vídeos de alta resolución como Full HD, 4K o 8K sin requerir volúmenes de datos excesivos.

!!!tip "Tipos de códecs"
Los códecs pueden clasificarse en dos grandes grupos:

!!!info "Códecs con pérdida (lossy)"
Eliminan información que se considera poco perceptible para el ojo humano con el objetivo de reducir el tamaño del archivo.

Son los más utilizados en vídeo digital.

!!!info "Códecs sin pérdida (lossless)"
Conservan toda la información original del vídeo, sin pérdida de calidad, pero generan archivos mucho más grandes.

Se usan principalmente en entornos profesionales de edición.

!!!info "Códecs más utilizados actualmente"

- **MPEG-4**  
Códec de vídeo muy popular que ofrece altas tasas de compresión manteniendo una buena calidad de imagen. Se utiliza en diversas aplicaciones, como el streaming de vídeo, las videoconferencias y la edición.
- **H.264 (AVC)**  
Es el códec más extendido. Ofrece buen equilibrio entre calidad y tamaño y es compatible con prácticamente todos los dispositivos y plataformas.
- **H.265 (HEVC)**  
Evolución del H.264. Permite una compresión más eficiente (aproximadamente la mitad de tamaño para calidad similar), especialmente útil en 4K y 8K.
- **AV1**  
Códec moderno, libre de licencias en muchos casos, muy eficiente en streaming. Está siendo adoptado por plataformas como YouTube o Netflix.
- **VP8/VP9**
Desarrollado por Google como alternativa a H.264/H.265, muy utilizado en YouTube.
- **Códecs profesionales (ProRes, DNxHD/HR)**
Usados en producción y postproducción. Prioriza la calidad frente al tamaño, facilitando la edición.

#### 3.3 - Contenedores de vídeo

<!-- https://www.dacast.com/es/blog-es/que-es-un-codec-de-video/ -->
<!-- https://www.cloudflare.com/es-es/learning/video/video-encoding-formats/ -->
<!-- https://www.tuinstitutoonline.com/cursos/openshot_v1506/01video_formatos.php -->
<!-- Concepto	Ventajas	Desventajas
Vídeo Comprimido	

- Ideal para streaming y almacenamiento web.

- Compatible con casi todos los dispositivos.
	

- La calidad puede degradarse si la tasa de bits es muy baja.

- El proceso de codificación requiere potencia de cálculo.
Vídeo Sin Pérdida (RAW)	

- Máxima calidad para postproducción profesional.

- Permite corrección de color extrema sin artefactos.
	

- El tamaño del archivo es inmenso (GB por minuto).

- Requiere hardware de almacenamiento muy rápido.

!!! Exercise "Ejercicio"
- Descargar los vídeos de los siguientes enlaces: -->

<!-- Vídeo HD MP4

Vídeo Baja Res

- Reproducir ambos vídeos a pantalla completa.
- Evidenciar la aparición de "artefactos" (cuadros) y falta de detalle en el vídeo de baja resolución frente al de alta.
2 - Formatos de vídeo
2.1 - Conceptos básicos de vídeo digital

Un vídeo es, en esencia, una sucesión de imágenes (fotogramas) que, al reproducirse a gran velocidad, crean la ilusión de movimiento.

    Fotograma (Frame):

    a) Es la unidad mínima de una secuencia de vídeo.

    b) El Frame Rate (FPS) indica cuántas imágenes se muestran por segundo (ej. 24, 30 o 60 fps).

    c) A mayor tasa de fotogramas, mayor es la fluidez del movimiento percibido.

    Resolución:

    Es la cantidad de píxeles que tiene cada fotograma. Se expresa como el número de píxeles horizontales por verticales.

    Ejemplo: Full HD (1920x1080) = 2.073.600 píxeles por fotograma.

    Tasa de bits (Bitrate):

    a) Se refiere a la cantidad de información procesada por unidad de tiempo (normalmente Mbps).

    b) Un bitrate alto mejora la calidad de la imagen, pero aumenta considerablemente el tamaño del archivo.

2.2 - Formatos y Contenedores de vídeo

Es importante distinguir entre el contenedor (la "caja" que guarda el vídeo y el audio) y el códec (el algoritmo que comprime los datos).

Los formatos más comunes incluyen MP4, MKV, AVI y MOV, cada uno con compatibilidades específicas.
2.1.1 - Formato MP4 (MPEG-4 Part 14)

Es el estándar de la industria actual. Es muy eficiente y compatible con prácticamente todos los dispositivos, desde móviles hasta televisores inteligentes. Suele utilizar el códec H.264 o H.265.
2.1.2 - Formato MKV (Matroska)

Es un contenedor de código abierto extremadamente flexible. Destaca por su capacidad para albergar una cantidad ilimitada de pistas de vídeo, audio y subtítulos en un solo archivo, siendo el preferido para cine en alta definición.
2.1.3 - Formato MOV (QuickTime)

Desarrollado originalmente por Apple. Es un formato de alta calidad muy utilizado en la edición de vídeo profesional. Permite almacenar vídeo con canal alfa (transparencia) si se usa el códec adecuado (como Apple ProRes).
2.1.4 - Formato AVI (Audio Video Interleave)

Uno de los formatos más antiguos desarrollado por Microsoft. Aunque es muy compatible, no es tan eficiente en compresión como los formatos modernos, lo que genera archivos más grandes para la misma calidad.
2.1.5 - Formato WebM

Desarrollado por Google para su uso en la web. Utiliza códecs de vídeo como VP8 o VP9 y es una alternativa libre de derechos al MP4, optimizada para la reproducción fluida en navegadores.
2.2 - Conceptos básicos de Códecs

El códec es el responsable de "comprimir" el vídeo para que no ocupe terabytes de espacio.

    H.264 (AVC): El más popular hoy en día. Equilibra perfectamente calidad y compatibilidad.

    H.265 (HEVC): El sucesor de H.264. Ofrece la misma calidad que su predecesor pero ocupando la mitad del espacio, ideal para vídeo 4K.

    AV1: Un códec moderno y abierto que busca sustituir a los anteriores sin costes de licencia, optimizado para el streaming de nueva generación.

2.3 - Formatos de intercambio y documentos
2.3.1 - Formato GIF (Animado)

Aunque técnicamente es un formato de imagen, se utiliza como un formato de "vídeo" corto sin sonido. Está limitado a 256 colores y suele generar archivos pesados si la duración es larga.
2.3.2 - Formato PDF (con vídeo incrustado)

El formato PDF permite la inclusión de archivos de vídeo multimedia que pueden ser reproducidos directamente desde el lector de documentos, facilitando presentaciones interactivas. -->

| **Licencia Creative Commons:** | |
| - | - |
| ![alt text](../../../assets/by-nc-nd-eu_.png) | **Reconocimiento-NoComercial-CompartirIgual CC BY-NC-SA:**  No se permite un uso comercial de la obra original ni de las posibles obras derivadas, la distribución de la cuales se debe hace con una licencia igual a la que regula la obra original. |
