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

![Descripción de la imagen](./img/UT6/vid-6.JPG){ .cincocero .marginbottom40 }

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

## 3 - Conceptos básicos de vídeo digital

El formato de vídeo digital define cómo se representa, codifica y almacena un vídeo. Incluye parámetros como resolución, tasa de fotogramas, bitrate, códec y otros aspectos relacionados con la calidad y el tamaño del archivo.

### 3.1 Resolución y relación de aspecto

#### 3.1.1 - Resolución

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

#### 3.1.2 - Relación de aspecto

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

        Un vídeo es, en esencia, una sucesión de imágenes (fotogramas) que, al reproducirse a gran velocidad, crean la ilusión de movimiento.

### 3.2 - Fotogramas por segundo / Framerate

- Es la unidad mínima de una secuencia de vídeo.

- El framerate (FPS) indica cuántas imágenes se muestran por segundo (ej. 24, 30 o 60 fps).

- A mayor tasa de fotogramas, mayor es la fluidez del movimiento percibido.

### 3.3 - Codificación y descodificación de vídeo digital

Para codificar y decodificar la información de vídeo se utilizan los códecs (codificador/descodificador), que son algoritmos encargados de comprimir y descomprimir los datos audiovisuales.

Su función es reducir el tamaño del archivo sin perder una calidad significativa, lo que resulta esencial para el almacenamiento, la edición y la transmisión en streaming.

#### 3.3.1 - Tipos de compresión en vídeo

La compresión que aplican los códecs modernos se basa principalmente en dos técnicas complementarias:

- **Compresión espacial** (intra-frame):  
Reduce la información dentro de un mismo fotograma eliminando redundancias entre píxeles. Se comprimen zonas con colores o patrones similares.
- **Compresión temporal** (inter-frame):  
Aprovecha la similitud entre fotogramas consecutivos, almacenando solo los cambios entre ellos en lugar de cada imagen completa.

#### 3.3.2 - Codecs de vídeo

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

!!!tip "Códecs más utilizados actualmente"

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

### 3.4 - Tasa de bits / Bitrate

El bitrate o tasa de bits es la cantidad de datos que se codifican o transmiten por segundo en un video, normalmente medida en Mbps (megabits por segundo). Un bitrate más alto suele implicar mayor calidad de imagen y mejor fidelidad de color, pero también genera archivos más grandes.

Es un factor clave en la calidad del video, aunque su impacto depende también del códec y del tipo de compresión utilizados, por lo que no debe considerarse de forma aislada frente a la resolución u otros parámetros.

### 3.5 - Contenedores de vídeo

Los contenedores de vídeo son formatos de archivo que empaquetan y estructuran flujos de datos de vídeo, audio, subtítulos y metadatos en un solo archivo. A diferencia de los códecs, no determinan la compresión, sino cómo se almacena.

Los más comunes incluyen MP4, MOV, MKV, AVI y WebM.

!!! tip "Características de los contenedores de vídeo más utilizados"

    - **MP4 (MPEG-4 Part 14):**  
    El estándar más extendido. Ofrece excelente compatibilidad con la web, dispositivos móviles y   reproductores multimedia.

    - **MOV (QuickTime File Format):**  
    Desarrollado por Apple, utilizado comúnmente en edición de vídeo profesional.

    - **MKV (Matroska):**  
    Contenedor de código abierto muy versátil, capaz de almacenar múltiples pistas de audio, vídeos y   subtítulos en un solo archivo.

    - **AVI (Audio Video Interleave):**  
    Uno de los formatos más antiguos y compatibles, desarrollado por Microsoft.

    - **WebM:**  
    Optimizado para la web y HTML5, ofrece alta calidad con buena compresión.

    - **MXF (Material Exchange Format):**  
    Estándar profesional utilizado en la industria de la televisión y el cine.

Para elegir el mejor, se debe considerar la compatibilidad con el reproductor final y el propósito del vídeo (streaming vs. almacenamiento).

### 3.5 - Audio en un vídeo

El audio complementa la información visual y mejora significativamente la experiencia del espectador. Un vídeo sin audio puede resultar incompleto o difícil de interpretar, especialmente cuando depende de diálogos, narración o efectos sonoros.

En un proyecto audiovisual, el audio puede clasificarse en varias categorías:

#### 3.5.1 - Tipos de audio en un vídeo

- **Voz o diálogo:**  
Es el elemento principal cuando hay personas hablando (entrevistas, explicaciones, narraciones).
- **Música:**  
Se utiliza para generar emociones, marcar ritmo o reforzar el mensaje.
- **Efectos de sonido (SFX):**  
Añaden realismo o enfatizan acciones (pasos, puertas, ambiente, etc.).
- **Sonido ambiente:**  
Refleja el entorno donde se desarrolla la escena (ruido de ciudad, naturaleza, interiores, etc.).

#### 3.5.2 - Calidad del audio

Un audio de mala calidad puede arruinar incluso un vídeo visualmente atractivo. Es importante considerar:

- **Claridad:**  
Evitar ruidos, interferencias o distorsión.
- **Volumen adecuado:**  
Ni demasiado bajo ni saturado.
- **Balance:**  
Ajustar correctamente la relación entre voz, música y efectos.
- **Sincronización:**  
El audio debe coincidir perfectamente con la imagen.

#### 3.5.3 - Tratamiento digital del sonido

El sonido se transmite en forma de ondas y los ordenadores trabajan con información digital. Por ese motivo el sonido deberá ser digitalizado antes de poder ser usado en el ordenador.

- **Muestreo (sampling):**  
El proceso de sampling del sonido consiste en tomar muestras de una señal sonora (muestreo) a intervalos constantes de tiempo (frecuencia de muestreo).

!!! tip "Ejemplo"
    Una frecuencia de 44.100 Hz (estándar de CD) significa que el ordenador "escucha" y registra el sonido 44.100 veces por segundo.

- **Digitalización (profundidad de bits):**  
Es la cantidad de bits empleados para guardar el valor de cada punto muestreado: a más bits, mayor calidad.  

!!! tip "Ejemplo"
    - **16 bits**: Ofrecen 65.536 niveles (calidad de CD).
    - **24 bits**: Proporcionan una precisión extrema, usada en estudios de grabación profesionales.

- **Importancia del muestro y la digitalización en la calidad del audio**  
![Descripción de la imagen](./img/UT6/vid-7.png){.marco .ochozero .margintopbottom10 }  
Una mayor frecuencia de muestreo permite capturar frecuencias más altas del sonido, aunque a partir de ciertos valores (como 44.1 kHz) no siempre supone una mejora perceptible para el oído humano.  
La profundidad de bits determina el rango dinámico y la precisión de la señal digital. Un mayor número de bits reduce el ruido de cuantificación y permite una reproducción más fiel y detallada del audio.

#### 3.5.4 - Canales de audio

Los canales de audio representan las distintas pistas independientes por las que se distribuye el sonido. El caso más común es el audio mono (un solo canal) y estéreo (dos canales: izquierdo y derecho), que permite una percepción espacial básica.

En sistemas más avanzados, como el audio multicanal (por ejemplo, 5.1 o 7.1), se añaden más canales para mejorar la inmersión y ubicar sonidos en distintas posiciones alrededor del oyente.

En general, cuantos más canales haya, mayor será la capacidad de recrear un entorno sonoro realista, aunque también aumenta la complejidad del sistema y los requisitos de almacenamiento y procesamiento.

#### 3.5.5 - Formatos de audio

Los formatos más comunes en vídeo digital incluyen:

- AAC (Advanced Audio Codec):  
Muy utilizado por su buena calidad y compresión eficiente.
- MP3 (MPEG Audio Layer III):  
Popular, aunque menos eficiente que AAC.
- WAV:  
Alta calidad sin compresión, pero ocupa más espacio.

**Nota:**  
A la hora de elegir un formato u otro, también se deberá tener en cuenta la compatibilidad de los mismos con el software / hardware de reproducción disponible.  

**Tabla resumen de los formatos de audio**  

|Formato de audio|Frecuencia de muestreo|Profundidad de bits|Calidad de audio|Compatibilidad|
|-|-|-|-|-|
|MP3|32 kHz, 44,1 kHz, 48 kHz|16 bits|Buena|Amplia|
|WAV|44,1 kHz, 48 kHz|16 bits, 24 bits|Excelente|Moderada|
|AAC|8 kHz – 96 kHz|16 bits, 24 bits|Muy buena|Amplia|

#### 3.5.6 - Edición de audio

Durante la postproducción, es habitual trabajar el audio para mejorar el resultado final:

- Eliminación de ruido
- Ajuste de niveles
- Ecualización
- Compresión
- Inserción de música y efectos

Programas como editores de vídeo o software específico de audio permiten realizar estos ajustes de forma precisa.

### 4 - 
<!-- ClipChamp -->
<!-- https://www.youtube.com/watch?v=m9nMhf6AQXw -->
<!-- openshot -->
 
<!-- Shotcut
Blender -->
<!-- https://www.dacast.com/es/blog-es/que-es-un-codec-de-video/ -->
<!-- https://www.cloudflare.com/es-es/learning/video/video-encoding-formats/ -->
<!-- https://www.tuinstitutoonline.com/cursos/openshot_v1506/01video_formatos.php -->
<!-- 
 -->

| **Licencia Creative Commons:** | |
| - | - |
| ![alt text](../../../assets/by-nc-nd-eu_.png) | **Reconocimiento-NoComercial-CompartirIgual CC BY-NC-SA:**  No se permite un uso comercial de la obra original ni de las posibles obras derivadas, la distribución de la cuales se debe hace con una licencia igual a la que regula la obra original. |
