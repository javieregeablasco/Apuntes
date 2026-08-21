https://claude.ai/chat/9855204e-6faa-475b-a785-1bd358009530


1. Revisa si Sysprep falló en la instancia original

Si todavía tienes la instancia origen (o puedes lanzar otra desde el mismo punto), revisa este log:

C:\Windows\System32\Sysprep\Panther\setupact.log

Busca líneas con SYSPRP seguidas de Error o Fatal. Las causas más típicas de que Sysprep falle silenciosamente en Windows Server son:

Apps de Microsoft Store / AppX instaladas para el usuario actual que no se pueden generalizar (muy común incluso en Server con apps preinstaladas).
Software de terceros que deja el sistema en un estado no compatible con Sysprep (agentes antivirus, ciertos drivers).
Sysprep ya se había ejecutado antes y el contador de ejecuciones se agotó (Windows solo permite un número limitado de sysprep antes de forzar reinstalación).

Si ves errores ahí, hay que resolverlos (normalmente desinstalando o eliminando esas apps AppX con PowerShell Get-AppxPackage | Remove-AppxPackage) y repetir el sysprep.

2. Verifica si EC2Launch v2 realmente ejecutó setAdminAccount

En la instancia nueva (la que da el error), si puedes acceder por SSM Session Manager (no necesita contraseña, solo necesita el rol IAM con AmazonSSMManagedInstanceCore y el agente SSM activo), revisa:

C:\ProgramData\Amazon\EC2Launch\Log\agent.log

Busca la tarea setAdminAccount y si terminó con error.

3. Mientras tanto, para entrar YA a esta instancia nueva

No esperes a resolver la causa raíz — puedes acceder ahora mismo de dos formas:

Opción A — SSM Session Manager (si el agente SSM está en tu AMI y la instancia tiene el rol IAM adecuado):
Conéctate directamente sin contraseña desde la consola EC2 → botón "Connect" → pestaña "Session Manager".

Opción B — Forzar contraseña vía SSM Run Command:
Si tienes SSM funcionando, ejecuta el documento AWS-RunPowerShellScript con:

powershell
net user Administrator "TuNuevaPassword123!"

¿Tienes el agente SSM instalado y el rol IAM asociado a estas instancias? Si me confirmas eso, te guío por el camino más rápido para entrar ahora mismo y luego revisamos el log de Sysprep para arreglarlo de raíz.