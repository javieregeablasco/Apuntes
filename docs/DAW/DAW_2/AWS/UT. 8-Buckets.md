<!-- https://www.youtube.com/watch?v=9jOdbA1yk4U -->
<!-- https://apuntes.de/aws-certificacion-csaa/buckets/#gsc.tab=0 -->

https://aws.amazon.com/es/products/storage/

<!-- https://www.youtube.com/watch?v=mDRoyPFJvlU -->
<!-- https://www.youtube.com/watch?v=C4calFCtlHg -->


Comparativa docente de los sistemas de almacenamiento en AWS
1. Clasificación didáctica básica (punto de partida)

Desde un enfoque pedagógico, es fundamental partir de una clasificación clara, equivalente a la que el alumnado ya conoce en entornos locales:

Tipo	Concepto conocido	Servicios AWS
Bloque	Disco duro / SSD	EBS, Instance Store
Archivos	Carpeta compartida / NAS	EFS, FSx
Objetos	Almacenamiento web	S3, Glacier

Este esquema facilita la transferencia de conocimiento desde sistemas tradicionales a la nube.

2. Almacenamiento en bloques (EBS vs Instance Store)
Característica	EBS	Instance Store
Persistencia	Sí	No
Asociado a EC2	Sí	Sí
Rendimiento	Alto	Muy alto
Snapshots	Sí	No
Uso docente típico	SO, BBDD	Caché
Enfoque didáctico

EBS se explica como el disco duro de una máquina virtual.

Instance Store sirve para introducir el concepto de almacenamiento efímero.

Práctica recomendada

Lanzar una EC2 con EBS y comprobar persistencia tras reinicio.

Comparar con Instance Store y analizar pérdida de datos.

3. Almacenamiento en archivos (EFS y FSx)
Amazon EFS (Linux)
Característica	EFS
Protocolo	NFS
Acceso concurrente	Sí
Escalado	Automático
Casos docentes	Web compartida, home users

Analogía docente: un servidor NAS en red local.

Amazon FSx (especialización)
Variante	Entorno	Caso docente
FSx Windows	Windows	Active Directory
FSx Lustre	HPC	Big Data
FSx NetApp	Enterprise	Replicación
FSx OpenZFS	Unix	Baja latencia

Claves didácticas:

No profundizar en todas las variantes.

Presentarlo como “EFS avanzado según necesidades”.

4. Almacenamiento de objetos (S3 y Glacier)
Característica	S3	Glacier
Tipo	Objetos	Archivado
Acceso	Inmediato	Lento
Coste	Medio	Muy bajo
Uso docente	Backups, web	Copias históricas
Concepto clave

No hay carpetas reales, solo objetos y metadatos.

Ideal para introducir arquitecturas desacopladas.

Práctica típica

Subir ficheros a un bucket.

Activar versionado.

Asociar políticas de ciclo de vida a Glacier.

5. Almacenamiento híbrido y migración
AWS Storage Gateway
Tipo	Analogía docente
File Gateway	NAS híbrido
Volume Gateway	SAN híbrida
Tape Gateway	Librería de cintas

Permite trabajar:

Migración progresiva

Integración on-prem ↔ cloud

Snow Family y DataSync
Servicio	Enfoque docente
DataSync	Transferencia automatizada
Snowball	Migración física

Ideal para explicar limitaciones del ancho de banda.

6. Relación con arquitecturas habituales (muy útil en clase)
Arquitectura	Almacenamiento
LAMP básica	EBS + S3
Web escalable	EFS + S3
2 capas	EBS (web + BBDD)
3 capas	EFS (web) + EBS (BBDD)
Backup	S3 + Glacier
7. Resumen pedagógico final
Pregunta docente	Servicio
¿Disco de una VM?	EBS
¿Carpeta compartida?	EFS
¿Datos web / backups?	S3
¿Archivado barato?	Glacier
¿Datos temporales?	Instance Store
¿Migración on-prem?	Storage Gateway
8. Propuesta de evaluación

Test conceptual: tipo de almacenamiento adecuado.

Práctica guiada: montar EC2 + EBS + S3.

Caso práctico: elegir almacenamiento para una empresa.



Unidad didáctica: Sistemas de almacenamiento en AWS
1. Identificación de la unidad

Ciclo formativo: CFGS Desarrollo de Aplicaciones Web (DAW) / Administración de Sistemas Informáticos en Red (ASIR)

Módulo profesional:

DAW: Despliegue de Aplicaciones Web / Diseño de Interfaces Web (contexto cloud)

ASIR: Implantación de Sistemas Operativos / Servicios en Red

Duración estimada: 6–8 horas

Unidad: Infraestructura cloud – Almacenamiento

2. Resultados de Aprendizaje (RA)

RA1. Analiza los distintos sistemas de almacenamiento en la nube ofrecidos por AWS, relacionándolos con soluciones de almacenamiento tradicionales.

RA2. Selecciona el sistema de almacenamiento más adecuado en función del tipo de aplicación, arquitectura y requisitos de persistencia, rendimiento y coste.

RA3. Implementa soluciones básicas de almacenamiento en AWS utilizando servicios dentro del Free Tier.

3. Criterios de Evaluación (CE)
Asociados al RA1

CE1.1 Identifica los tipos de almacenamiento en AWS (bloque, archivos y objetos).

CE1.2 Describe las características principales de EBS, EFS, S3 y Glacier.

CE1.3 Compara los sistemas de almacenamiento cloud con soluciones locales (disco, NAS, copias de seguridad).

Asociados al RA2

CE2.1 Justifica la elección de un sistema de almacenamiento según un caso práctico.

CE2.2 Relaciona arquitecturas web habituales con los servicios de almacenamiento adecuados.

CE2.3 Evalúa ventajas e inconvenientes de cada servicio en términos de coste, disponibilidad y rendimiento.

Asociados al RA3

CE3.1 Configura un volumen EBS asociado a una instancia EC2.

CE3.2 Crea y gestiona un bucket S3 con políticas básicas.

CE3.3 Verifica la persistencia y accesibilidad de los datos almacenados.

4. Contenidos
4.1 Conceptos previos

Almacenamiento local y en red

Persistencia de datos

Arquitecturas cliente-servidor

4.2 Almacenamiento en la nube

Introducción al almacenamiento cloud

Ventajas frente a infraestructuras on‑premise

4.3 Sistemas de almacenamiento en AWS
a) Almacenamiento en bloques

Amazon EBS

Instance Store

Casos de uso y limitaciones

b) Almacenamiento en archivos

Amazon EFS

Amazon FSx (visión general)

Comparación con NAS

c) Almacenamiento de objetos

Amazon S3

Concepto de objeto y bucket

Versionado y clases de almacenamiento

S3 Glacier (archivado)

4.4 Almacenamiento y arquitecturas web

Arquitectura LAMP en AWS

Arquitecturas de 2 y 3 capas

Separación de datos y aplicación

4.5 Buenas prácticas

Elección del almacenamiento adecuado

Control de costes

Seguridad básica (permisos y acceso)

5. Metodología

Explicación guiada con esquemas

Comparación con entornos locales conocidos por el alumnado

Prácticas paso a paso en AWS Free Tier

Resolución de casos prácticos

6. Actividades prácticas (AWS Free Tier)
Práctica 1. Uso de almacenamiento en bloques (EBS)

Objetivo: Comprender la persistencia de datos.

Crear una instancia EC2 (t2.micro)

Asociar un volumen EBS

Crear un archivo de prueba

Reiniciar la instancia y comprobar persistencia

Práctica 2. Almacenamiento de objetos con S3

Objetivo: Gestionar almacenamiento desacoplado.

Crear un bucket S3

Subir archivos

Activar versionado

Descargar versiones anteriores

Práctica 3. Comparativa EBS vs S3

Objetivo: Diferenciar tipos de almacenamiento.

Guardar datos en EBS y en S3

Analizar acceso, uso y persistencia

Documentar conclusiones

Práctica 4. Caso práctico guiado

Escenario: Empresa con una web corporativa y copias de seguridad.

Elegir almacenamiento para:

Aplicación web

Base de datos

Backups

Justificar la elección

7. Instrumentos de evaluación

Cuestionario teórico

Entrega de prácticas documentadas

Resolución de caso práctico

Rúbrica basada en RA y CE

8. Recursos

Cuenta AWS Free Tier

Consola de AWS

Guías paso a paso del profesor

Diagramas de arquitectura

9. Observaciones didácticas

Priorizar comprensión conceptual frente a complejidad técnica.

Evitar servicios fuera del Free Tier.

Relacionar siempre con situaciones reales y profesionales.

Ya tienes la unidad didáctica formalizada en el canvas, con RA, CE, contenidos, metodología y actividades, lista para integrar en una programación oficial o en el proyecto curricular (muy alineada con el enfoque que ya trabajas en otras unidades de cloud y AWS).

Siguiente paso propuesto (recomendado)

Puedo continuar de dos formas, ambas habituales en contexto docente:

Desarrollar los ejercicios prácticos paso a paso, con:

Capturas conceptuales (qué botón pulsar, qué opción elegir)

Advertencias de coste (Free Tier)

Resultados esperados

Preguntas de reflexión para el alumnado

Crear rúbricas de evaluación específicas para:

Prácticas técnicas

Caso práctico final

Evaluación competencial (RA ↔ CE)

Indícame cómo quieres continuar y, si lo deseas, el ciclo exacto (DAW o ASIR) para afinar aún más el enfoque técnico.