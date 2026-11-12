
# Condiciones de lanzamiento de las instancias `alumnos` y `profesor`

Lanzar 2 instancias con las siguiente condiciones.

1. AMI: **Windows Server 2025 Base**.
1. Tipo de instancia: `m7i.xlarge` o `t3.large`.
1. Almacenamiento: 30GB.
1. Zona de despliegue  **Configuración de red** → pulsar el botón de **editar** y en **subred** buscar la subred **172.32.31.0/20**.
1. Configurar **grupo de seguridad** de la instancia. 
    - **Reglas de entrada**: Permitir todo el tráfico.
    - **Reglas de salida**: Permitir todo el tráfico.

Cambiar nombre de las instancias a `alumnos` y `profesor`

