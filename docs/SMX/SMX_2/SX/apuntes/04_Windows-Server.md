---
ciclo: CFGM - Técnico en Sistemas Microinformáticos y Redes
title: Servicios en red
module number: 0227
lesson: UD. 4.0 - Windows Server
author: Javier Egea Blasco  
layout: default  
year: 26-27  
keywords: SMX, SMR, SX, SR
schedule: 233h - 7h/w
---

![Descripción de la imagen](./img_4/img_4_4.png){ .img2 .marginbottom40}

**Resultados de aprendizaje y criterios de evaluacion que se evaluarán en esta unidad.**  

| **Resultados de aprendizaje de la unidad didáctica:**|
||
| **RA. 1:** Instala servicios de configuración dinámica, describiendo sus características y aplicaciones.|

|**Criterios de evaluación de la unidad didáctica:**|
||
|**a)** Se ha reconocido el funcionamiento de los mecanismos automatizados de configuración de los parámetros de red.|
|**b)** Se han identificado las ventajas que proporcionan.|
|**c)** Se han ilustrado los procedimientos y pautas que intervienen en una solicitud de configuración de los parámetros de red.|
|**d)** Se ha instalado un servicio de configuración dinámica de los parámetros de red.|
|**e)** Se ha preparado el servicio para asignar la configuración básica a los sistemas de una red local.|
|**f)** Se han realizado asignaciones dinámicas y estáticas.|
|**g)** Se han integrado en el servicio opciones adicionales de configuración.|
|**h)** Se ha verificando la correcta asignación de los parámetros.|

## 1 - Introducción



### 1.8 gui ubuntu server

https://www.youtube.com/watch?v=aTtYuQ3YVOs

#### 1.8.1 Actualizar repositorios e instalar interfaz (ej. XFCE) y RDP

sudo apt update && sudo apt upgrade -y
<!-- sudo apt install xfce4 xfce4-goodies xrdp -y -->
sudo apt install ubuntu-desktop

#### 1.8.2 verificar si gnome se ha instalado correctamente

gnome-shell --version


<!-- sudo apt install --reinstall xrdp -y -->

<!-- #### 1.8.2 Iniciar y habilitar el servicio RDP

sudo systemctl enable xrdp
sudo systemctl start xrdp -->

3. Verificar los paquetes instalados (Ubuntu / Debian)

Si quieres confirmar que el metapaquete del escritorio completo o la sesión están en el sistema:
Bash

dpkg -l | grep -E "gnome-shell|ubuntu-desktop"

Si ves líneas que empiezan por ii, significa que los paquetes están instalados correctamente (ii = Installed/Ok).

reiniciar 
sudo reboot now
    

#### 1.8.3 Asignar contraseña al usuario

sudo passwd ubuntu

# instalar xRDP 
sudo apt install xrdp -y
sudo systemctl enable xrdp

Tip extra si usas RDP: Si instalaste GNOME para usarlo con xRDP, recuerda cambiar el comando de inicio en tu archivo ~/.xsession o /etc/xrdp/startwm.sh para que ejecute gnome-session en lugar de xfce4-session:

    Bash

    echo "gnome-session" > ~/.xsession

sudo systemctl restart xrdp 



<!-- #### 1.8.4 Definir XFCE para el usuario actual

echo "xfce4-session" > ~/.xsession

#### 1.8.5 Configurar xRDP para que siempre inicie XFCE a nivel global

sudo sed -i.bak '/^[[:space:]]*test -x \/etc\/X11\/Xsession/i xfce4-session' /etc/xrdp/startwm.sh -->


#### 1.8.6 Reiniciar el servicio xRDP

sudo systemctl restart xrdp

## 2 wireshark

wiresahrk

ip addr show eth0

y después detener el cliente DHCP:

killall udhcpc

Eliminar la dirección actual:

ip addr flush dev eth0
2. Volver a solicitar una IP por DHCP

Ejecuta:

udhcpc -i eth0

Si quieres que se vea claramente todo el proceso DHCP:

udhcpc -i eth0 -f -v

DHCP Discover
       ↓
DHCP Offer
       ↓
DHCP Request
       ↓
DHCP ACK

<!-- https://youtu.be/nc-ratzt1MU?si=yqgXB7f7zQNJvCCc&t=750 -->

https://learn.microsoft.com/es-es/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server?tabs=powershell

<!-- docker -->
<!-- https://www.youtube.com/watch?v=3UGWJ0rWzms&list=PLn5IkU1ZhgiZP8EewgFdxgnsIwN1q3Juo&index=1 -->

<!-- https://www.youtube.com/watch?v=uOk8vu2SEds -->
<!-- https://raul-profesor.github.io/SXI/section/P1/ -->
<!-- https://marcosruiz.github.io/categories/servicios-en-red/ -->
<!-- https://docs.google.com/presentation/d/1eJTYUdgqbQTfzIJDM4FhhvqMX3ICfIG85OaFwnReU3A/edit?slide=id.g1142a802_1_0#slide=id.g1142a802_1_0 -->
<!-- https://sergarb1.github.io/CursoIntroduccionADocker/ -->
<!-- https://github.com/kahun/awesome-sysadmin -->
<!-- https://acastan.gitbook.io/servicios -->


Get-VMHost


https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/

<!-- Invoke-WebRequest -Uri "https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/x86_64/alpine-standard-3.20.3-x86_64.iso" -OutFile "C:\ISOs\alpine.iso" -->
Invoke-WebRequest -Uri "https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/x86_64/alpine-standard-3.24.1-x86_64.iso" -OutFile "C:\ISOs\alpine.iso"

https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/

https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-standard-3.24.1-x86_64.iso


Las buenas prácticas indican que el controlador de dominio no debe compartir ningun otro rol. 
En estructuras pequeñas es normal tener el DNS y el DHCP en el mismo controlador de dominio.

ambito: total de ip que el DHCP se encargará de repartir.
deberemos guardar una serie de ip (estaticas) para dispositivos criticos.

lease duration:
8-15 dias para sobremesa.
7-10 dias para protatiles
3-5 dia para telefonos móviles.
1 dia red de invitados.

despues de activar el ambito solo se asigna la ip pero no los ambitos.



# Práctica SMR: Servidor DHCP en Windows Server sobre AWS (con virtualización anidada)

## Objetivo pedagógico
Que el alumnado instale y configure el rol **DHCP Server** en Windows Server, y observe en tiempo real cómo varios equipos cliente obtienen su configuración IP (DHCPDISCOVER → OFFER → REQUEST → ACK), reservas, exclusiones, ámbitos (scopes), opciones de ámbito (DNS, puerta de enlace, etc.).

## Por qué no se puede hacer con instancias EC2 "sueltas"
Dentro de una VPC de AWS, **el tráfico broadcast/multicast no se propaga entre instancias**. DHCP depende de broadcasts (`255.255.255.255`), así que un cliente en una instancia EC2 nunca "verá" un DHCPOFFER de otra instancia EC2 en la misma subred, aunque el servidor esté bien configurado. Cada tarjeta de red (ENI) recibe su IP exclusivamente del DHCP interno de AWS, que no se puede sustituir.

**Solución:** montar todo el laboratorio *dentro* de una sola instancia EC2, usando un hipervisor anidado (Hyper-V) donde sí existe broadcast real entre las VMs virtuales que creéis dentro.

## Novedad clave (Feb 2026)
Hasta hace poco esto solo era posible en instancias `.metal` (caras). Desde el **16 de febrero de 2026**, AWS soporta oficialmente virtualización anidada en instancias EC2 **normales** (no metal), lo que abarata mucho la práctica. Familias soportadas actualmente: `C8i`, `M8i`, `R8i`, `C8id`, `R8id`, `M8id`, `C8i-flex`, `R8i-flex`, `M8i-flex`, `X8i`, `C7i`, `R7i`, `M7i`, `C7id`, `R7id`, `M7id`, `C7i-flex`, `R7i-flex`, `M7i-flex`, `I7i`. Solo procesadores Intel (no Graviton). Hipervisores L1 soportados: **Hyper-V** y **KVM**.

---

## Arquitectura del laboratorio (por alumno o por grupo)

```
Instancia EC2 (p. ej. m7i.2xlarge, Windows Server 2022, nested virt ON)
│
├── Hyper-V (L1, dentro de la instancia)
│   ├── Switch virtual "Interno" (Internal / Private) — SIN salida a la VPC
│   │
│   ├── VM1: Windows Server 2022 → Rol DHCP Server
│   ├── VM2: Windows 10/11 (cliente) → IP por DHCP
│   ├── VM3: Windows 10/11 (cliente) → IP por DHCP
│   └── (opcional) VM4: Linux ligero (cliente) → dhclient
```

Con el switch en modo **Interno/Privado** (no "Externo"), el broadcast DHCP se queda encerrado dentro del propio hipervisor Hyper-V — exactamente igual que en un laboratorio físico o en VirtualBox local.

---

## Paso 1 — Elegir tipo de instancia y región

- Recomendado para uso educativo con recursos amplios: **`m7i.xlarge`** o **`m7i.2xlarge`** (4/8 vCPU, 16/32 GB RAM) — suficiente para 1 servidor + 2-3 clientes ligeros.
- **Cuentas de estudiante (AWS Academy/Educate):** suelen restringir el catálogo a familias `t2`/`t3` por defecto. Comprueba si tu cuenta permite lanzar `m7i.large` (2 vCPU, **8 GiB RAM**) — validado en esta práctica y suficiente para 1 host + 1-2 clientes ligeros (Alpine). Si no aparece ninguna familia `7i`/`8i` al elegir tipo de instancia, el laboratorio de virtualización anidada no es viable en esa cuenta y toca plantear la alternativa en local (VirtualBox/VMware en los equipos del aula).
- Si el grupo va a correr VMs más pesadas o con GUI completa, sube a `m7i.4xlarge` (si la cuenta lo permite).
- Comprueba que la **región** que vais a usar ya tiene la característica activa (el despliegue empezó por `us-west-2` y se fue extendiendo; confirmadlo en la consola al configurar la instancia — si no aparece la opción, probad otra región o usad el CLI).
- **T3/T2 no sirven**: son familias *burstable* que no exponen VT-x al invitado, así que aunque tuvieran RAM de sobra, Hyper-V nunca arrancaría ninguna VM dentro.

## Paso 2 — Lanzar la instancia con virtualización anidada activada

### Opción A: Consola (si ya está disponible en tu región)
1. EC2 → **Launch instance**.
2. AMI: **Windows Server 2022 Base** (o 2025 si está disponible).
3. Tipo de instancia: uno de los soportados (`m7i.xlarge`, etc.).
4. Despliega **Advanced details** → busca **Nested virtualization** → **Enable**.
5. Configura Security Group: permite **RDP (3389)** desde la IP del aula/alumno.
6. Lanza la instancia con un par de claves para poder recuperar la contraseña de administrador.

### Opción B: AWS CLI (recomendable, más fiable mientras el rollout en consola se completa)
```bash
aws ec2 run-instances \
  --image-id ami-xxxxxxxxxxxxxxxxx \
  --instance-type m7i.xlarge \
  --key-name mi-clave \
  --security-group-ids sg-xxxxxxxx \
  --subnet-id subnet-xxxxxxxx \
  --cpu-options NestedVirtualization=enabled \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=lab-dhcp-alumno1}]' \
  --region us-west-2
```
> Importante: usa una versión reciente del AWS CLI v2 (≥ 2.33.21). Versiones más antiguas no reconocen el parámetro `NestedVirtualization` dentro de `--cpu-options`.

Verifica que quedó activado:
```bash
aws ec2 describe-instances --instance-ids i-xxxxxxxxxxxxxxxxx \
  --query "Reservations[].Instances[].CpuOptions"
```

### Opción C: Activar nested virtualization en una instancia YA existente
Si ya tienes la instancia lanzada (p. ej. instalaste Windows Server con `t3.medium` y luego cambiaste a `m7i.large`), no hace falta relanzarla. El comando **no** es `modify-instance-attribute` sino un subcomando específico de CPU: `modify-instance-cpu-options`, con el flag `--nested-virtualization` (no `--cpu-options`):

```bash
# 1. Parar la instancia (debe estar Stopped para poder tocar CpuOptions)
aws ec2 stop-instances --instance-ids i-xxxxxxxxxxxxxxxxx
aws ec2 wait instance-stopped --instance-ids i-xxxxxxxxxxxxxxxxx

# 2. Cambiar el tipo de instancia si hace falta (ej. de t3.medium a m7i.large)
aws ec2 modify-instance-attribute --instance-id i-xxxxxxxxxxxxxxxxx --instance-type m7i.large

# 3. Activar nested virtualization
aws ec2 modify-instance-cpu-options \
  --instance-id i-xxxxxxxxxxxxxxxxx \
  --nested-virtualization enabled

# 4. Arrancar de nuevo
aws ec2 start-instances --instance-ids i-xxxxxxxxxxxxxxxxx
```
Si te da error de "Unknown options", tu AWS CLI es antiguo — actualízalo (`sudo ./aws/install --update`) hasta v2 ≥ 2.33.21.

## Paso 3 — Conectarse a la instancia y activar Hyper-V

1. Conéctate por **RDP** (obtén la contraseña con "Get Windows password" en la consola EC2).
2. Abre PowerShell como administrador e instala el rol Hyper-V:
```powershell
Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart
```
3. Tras el reinicio, abre **Hyper-V Manager** y verifica que el rol quedó operativo:
```powershell
Get-VMHost
```

### Si `Get-VMHost` da error "term not recognized"
- Comprueba que el rol instaló bien: `Get-WindowsFeature -Name Hyper-V*` (debe decir `Installed` en todas las líneas). Si dice `Available`, repite el `Install-WindowsFeature` — pide reinicio y a veces se corta con RDP.
- Comprueba que estás en PowerShell de **64 bits**: `[Environment]::Is64BitProcess` debe devolver `True`. El módulo de Hyper-V no existe en la consola x86.
- Si el rol está instalado pero el cmdlet no carga: `Import-Module Hyper-V`.

### Sobre `VirtualMachineMigrationEnabled = False`
Es normal y no afecta al laboratorio. Solo controla la Live Migration entre hosts Hyper-V distintos — aquí todo vive en un único host (la instancia EC2), así que no hace falta activarlo.

## Paso 4 — Crear el switch virtual interno

En Hyper-V Manager → **Virtual Switch Manager** → **New virtual network switch**:
- Tipo: **Internal** (o **Private**, si no quieres que ni siquiera la instancia anfitriona tenga IP en esa red).
- Nombre sugerido: `LAN-Laboratorio-DHCP`.

Esto asegura que el tráfico DHCP nunca sale hacia la red de AWS ni a otras instancias.

## Paso 5 — Crear las máquinas virtuales cliente

Con RAM limitada (p. ej. `m7i.large` con 8 GiB), lo más eficiente es que **el propio host Windows Server actúe como servidor DHCP** (no hace falta una VM `SRV-DHCP` aparte) y usar Hyper-V solo para las VMs cliente. Como cliente, **Alpine Linux** es la opción más ligera (256–512 MB por VM) y perfectamente válida para ver el proceso DHCP completo.

### 5.1 Carpetas de trabajo
```powershell
New-Item -Path "C:\ISOs" -ItemType Directory -Force
New-Item -Path "C:\VMs" -ItemType Directory -Force
```

### 5.2 Descargar el ISO
```powershell
Invoke-WebRequest -Uri "https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/x86_64/alpine-standard-3.20.3-x86_64.iso" -OutFile "C:\ISOs\alpine.iso"
```
Comprueba que la descarga es correcta (debe rondar 190-250 MB, no unos pocos KB):
```powershell
Get-Item "C:\ISOs\alpine.iso" | Select-Object Name, Length
```

### 5.3 Crear la VM
```powershell
New-VM -Name "CLIENTE-1" `
  -MemoryStartupBytes 512MB `
  -Generation 2 `
  -NewVHDPath "C:\VMs\CLIENTE-1.vhdx" `
  -NewVHDSizeBytes 4GB `
  -SwitchName "LAN-Laboratorio-DHCP"

Set-VMFirmware -VMName "CLIENTE-1" -EnableSecureBoot Off   # Alpine no está firmado con la clave de MS
```

### 5.4 Añadir la unidad de DVD y montar el ISO
> **Importante:** las VMs Generation 2 **no traen unidad de DVD por defecto** (a diferencia de Generation 1). Hay que añadirla explícitamente con `Add-VMDvdDrive`, no basta con `Set-VMDvdDrive` sobre una unidad que no existe (falla en silencio y luego la VM intenta arrancar por red/PXE).
```powershell
Add-VMDvdDrive -VMName "CLIENTE-1" -Path "C:\ISOs\alpine.iso"
Get-VMDvdDrive -VMName "CLIENTE-1"   # debe mostrar el Path del ISO
```

### 5.5 Forzar el orden de arranque (DVD antes que red)
```powershell
Stop-VM -Name "CLIENTE-1" -TurnOff -Force
Set-VMFirmware -VMName "CLIENTE-1" -FirstBootDevice (Get-VMDvdDrive -VMName "CLIENTE-1")
Start-VM -Name "CLIENTE-1"
```

### 5.6 Conectar a la consola de la VM
Abre **Hyper-V Manager** → doble clic en `CLIENTE-1` (o clic derecho → Connect). Deberías ver arrancar el live system de Alpine. El candado rojo abierto que aparece arriba es solo el indicador de Secure Boot desactivado — no es un error.

En el prompt `localhost login:` entra con:
```
root
```
(sin contraseña).

Repite los pasos 5.1–5.6 con `CLIENTE-2` si quieres un segundo cliente.

**Alternativa Windows:** si prefieres un cliente Windows (más pesado, ~2 GB RAM) en vez de Alpine, usa el mismo procedimiento pero descargando un ISO de Windows Server/10/11 desde el Centro de evaluación de Microsoft.

## Paso 6 — Configurar el rol DHCP en el host (Windows Server anfitrión)

### 6.1 Instalar el rol
```powershell
Install-WindowsFeature -Name DHCP -IncludeManagementTools
```
No requiere reinicio.

### 6.2 Autorizar el servidor (solo aplica con Active Directory)
```powershell
Add-DhcpServerInDC -DnsName $env:COMPUTERNAME
```
`$env:COMPUTERNAME` es una variable de entorno que PowerShell resuelve automáticamente al nombre real del servidor — no hay que sustituirla a mano. En un servidor **standalone** (sin dominio, el caso típico de este laboratorio) este comando puede dar error; es esperable, ignóralo y continúa.

### 6.3 Asignar IP fija a la interfaz del switch interno
Al crear el switch interno, Windows crea automáticamente un adaptador virtual en el host (`vEthernet (LAN-Laboratorio-DHCP)`). Compruébalo:
```powershell
Get-NetIPAddress -InterfaceAlias "vEthernet (LAN-Laboratorio-DHCP)" -AddressFamily IPv4
```
Si ves una IP tipo `169.254.x.x` (APIPA), es normal — significa que aún no tiene IP fija. Asígnasela (será la puerta de enlace/DNS del ámbito):
```powershell
New-NetIPAddress -InterfaceAlias "vEthernet (LAN-Laboratorio-DHCP)" -IPAddress 192.168.10.1 -PrefixLength 24
```

### 6.4 Crear el ámbito (scope)
```powershell
Add-DhcpServerV4Scope -Name "Aula-SMR" `
  -StartRange 192.168.10.100 `
  -EndRange 192.168.10.200 `
  -SubnetMask 255.255.255.0 `
  -State Active
```

### 6.5 Configurar opciones del ámbito (DNS, puerta de enlace)
```powershell
Set-DhcpServerV4OptionValue -ScopeId 192.168.10.0 `
  -DnsServer 8.8.8.8 `
  -Router 192.168.10.1
```

### 6.6 Comprobar
```powershell
Get-DhcpServerV4Scope
Get-DhcpServerV4OptionValue -ScopeId 192.168.10.0
```
También puedes activarlo y revisarlo desde la consola gráfica (**DHCP → clic derecho al ámbito → Activate**) para que los alumnos vean el proceso completo por GUI además de por PowerShell.

## Paso 7 — Verificar desde los clientes

### En un cliente Alpine
Dentro de la consola de la VM (root, sin contraseña):
```sh
ip link show          # confirma el nombre real de la interfaz (eth0, enp0s3...)
ip link set eth0 up    # si aparece "state DOWN", súbela manualmente antes de pedir IP
udhcpc -i eth0
```
Si da `network is down`, es que la interfaz está apagada a nivel de enlace — el `ip link set eth0 up` lo soluciona. Si persiste, revisa en el host que el adaptador de la VM está conectado al switch correcto:
```powershell
Get-VMNetworkAdapter -VMName "CLIENTE-1" | Select-Object Name, SwitchName, Status
```

### En un cliente Windows
```cmd
ipconfig /release
ipconfig /renew
ipconfig /all
```

En ambos casos, los alumnos deberían ver la IP asignada dentro del rango del ámbito, la puerta de enlace y el DNS entregados por el servidor.

## Paso 8 — Ver el proceso de broadcast y asignación (DORA) en detalle

Esta es la parte más didáctica: ver el intercambio DHCPDISCOVER → DHCPOFFER → DHCPREQUEST → DHCPACK, no solo el resultado final.

### 8.1 Ver los leases concedidos (resultado, no proceso)
```powershell
Get-DhcpServerV4Lease -ScopeId 192.168.10.0
```
Muestra IP, MAC del cliente, nombre de host y expiración del lease.

### 8.2 Log de auditoría del propio DHCP (sin instalar nada extra)
Windows Server DHCP registra cada fase del proceso en un log diario:
```powershell
Get-Content "C:\Windows\System32\dhcp\DhcpSrvLog-$(Get-Date -Format 'ddd').log" -Tail 30
```
Contiene códigos de evento (10 = nuevo lease, 11 = renovación, etc.) con timestamps — buen ejercicio para que el alumnado interprete el log como evidencia textual del DORA.

### 8.3 Captura con tcpdump en el cliente Alpine (ver el DORA en vivo, lado cliente)
```sh
apk add tcpdump
tcpdump -i eth0 -n port 67 or port 68 -v
```
Con la captura corriendo, repite `udhcpc -i eth0` en otra sesión (o tras liberar la IP) para ver los 4 paquetes en tiempo real con IPs y puertos 67/68.

### 8.4 Captura con Wireshark en el host (lado servidor, análisis de campos BOOTP/DHCP)
```powershell
Invoke-WebRequest -Uri "https://2.na.dl.wireshark.org/win64/Wireshark-latest-x64.exe" -OutFile "C:\Wireshark-installer.exe"
Start-Process "C:\Wireshark-installer.exe"
```
Instala con opciones por defecto (incluye Npcap). Captura en el adaptador **`vEthernet (LAN-Laboratorio-DHCP)`** con el filtro:
```
bootp
```
Permite inspeccionar campo a campo (Option 53 - Message Type, Option 51 - Lease Time, Client MAC...), justo el nivel de detalle que suele pedirse en el currículo de SMR.

> Si el host no ve tráfico este-oeste de las VMs en Wireshark, activa port mirroring en el adaptador de la VM:
> ```powershell
> Set-VMNetworkAdapter -VMName "CLIENTE-1" -PortMirroring Source
> ```

### 8.5 Ejercicios adicionales con valor curricular
- **Reservas** por MAC: `Add-DhcpServerV4Reservation`.
- **Exclusiones** dentro del ámbito: `Add-DhcpServerV4ExclusionRange`.
- **Liberar y renovar** (contraste DISCOVER completo de 4 paquetes vs. renovación de 2 paquetes): en Alpine, `udhcpc -R` para liberar y volver a pedir.
- **Agotamiento del ámbito**: crear un ámbito de prueba muy pequeño (p. ej. solo 2-3 IPs) para que los alumnos vean qué ocurre cuando un cliente no puede recibir oferta.
- **Dos clientes simultáneos**: añadir `CLIENTE-2` y comparar cómo el servidor evita duplicados de IP.

---

## Escalar la práctica a varios alumnos/grupos

Opciones, de más simple a más automatizada:

1. **Una instancia por alumno**, lanzada manualmente siguiendo la guía — válido para grupos pequeños.
2. **AMI personalizada**: una vez que tengas una instancia con Windows Server + Hyper-V + switch interno + VMs base ya creadas (apagadas), crea una **AMI** a partir de ella. Cada alumno lanza su propia instancia desde esa AMI y ya tiene el entorno listo, solo falta que configuren el DHCP (que es justo la parte que queréis que hagan ellos).
3. **CloudFormation / Launch Template** para lanzar N instancias idénticas de golpe (una por alumno), reutilizando la AMI del punto 2. Esto os interesa si repetís la práctica cada curso.

¿Quieres que te prepare la plantilla de **CloudFormation** para lanzar automáticamente una instancia por alumno (con nested virtualization activado, AMI personalizada y tags por nombre de alumno), o prefieres primero montar y probar tú una instancia "maestra" de forma manual antes de automatizar?

---

## Notas de coste
- `m7i.xlarge` en On-Demand: revisa el precio actual en la [calculadora de AWS](https://calculator.aws) para tu región, ya que varía.
- Recuerda **detener (no solo cerrar RDP)** las instancias fuera del horario de clase — el hipervisor anidado no reduce el coste de la instancia base.
- Considera usar **Spot Instances** si la práctica no requiere disponibilidad garantizada, para abaratar costes en un aula.






# Práctica SMR: Servidor DHCP en Ubuntu Server 22.04 sobre AWS (con virtualización anidada)

Versión equivalente a la práctica de Windows Server, pero con **Ubuntu Server 22.04** como anfitrión, **KVM/QEMU + libvirt** como hipervisor anidado (en vez de Hyper-V), e **isc-dhcp-server** como servicio DHCP (en vez del rol DHCP de Windows).

## Objetivo pedagógico
Que el alumnado instale y configure **isc-dhcp-server** en Ubuntu, y observe el proceso DHCPDISCOVER → OFFER → REQUEST → ACK entre el servidor y varios clientes virtuales, con ámbitos, reservas y exclusiones.

## Por qué sigue haciendo falta virtualización anidada
El motivo es exactamente el mismo que en la práctica Windows: dentro de una VPC de AWS **el broadcast no se propaga entre instancias EC2**, así que un DHCP en una instancia nunca vería peticiones de otra instancia distinta. La solución sigue siendo montar todo (servidor + clientes) **dentro de una única instancia EC2**, usando un hipervisor anidado con una red aislada donde el broadcast sí circula libremente.

## Novedad de fondo (recordatorio)
Desde el 16 de febrero de 2026, AWS soporta virtualización anidada en instancias EC2 no-metal (familias `C7i`/`M7i`/`R7i`, `C8i`/`M8i`/`R8i` y variantes). Esto aplica igual con Linux: los hipervisores L1 soportados son **Hyper-V y KVM** — en Ubuntu usaremos KVM.

---

## Arquitectura del laboratorio

```
Instancia EC2 (m7i.large, Ubuntu Server 22.04, nested virt ON)
│
├── KVM / libvirt (L1, dentro de la instancia)
│   ├── Red virtual "aislada" (isolated) — SIN salida a la VPC ni NAT
│   │
│   ├── isc-dhcp-server → corriendo en el propio host (Ubuntu), escuchando en la interfaz puente de la red aislada
│   ├── VM "cliente1": Alpine Linux → IP por DHCP
│   └── VM "cliente2" (opcional): Alpine Linux → IP por DHCP
```

Igual que con el switch "Internal" de Hyper-V, aquí usamos una red libvirt en modo **isolated**: sin forwarding hacia la interfaz física ni NAT, así el tráfico DHCP no sale de la instancia.

---

## Paso 1 — Elegir tipo de instancia y región

- Mismas condiciones que en la práctica de Windows: necesitas una familia `7i`/`8i` (`m7i.large` con 8 GiB RAM es suficiente para host + 1-2 clientes Alpine).
- En cuentas de estudiante, confirma que puedes lanzar esa familia antes de nada; si solo tienes `t2`/`t3` disponibles, esta práctica no es viable en AWS (T3 no expone VT-x al invitado).

## Paso 2 — Lanzar la instancia con virtualización anidada activada

### Opción A: Consola
1. EC2 → **Launch instance**.
2. AMI: **Ubuntu Server 22.04 LTS**.
3. Tipo de instancia: `m7i.large` (o superior).
4. **Advanced details** → **Nested virtualization** → **Enable**.
5. Security Group: permite **SSH (22)** desde la IP del aula/alumno.

### Opción B: AWS CLI
```bash
aws ec2 run-instances \
  --image-id ami-xxxxxxxxxxxxxxxxx \
  --instance-type m7i.large \
  --key-name mi-clave \
  --security-group-ids sg-xxxxxxxx \
  --subnet-id subnet-xxxxxxxx \
  --cpu-options NestedVirtualization=enabled \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=lab-dhcp-ubuntu-alumno1}]' \
  --region us-west-2
```

### Opción C: Activar nested virtualization en una instancia ya existente
```bash
aws ec2 stop-instances --instance-ids i-xxxxxxxxxxxxxxxxx
aws ec2 wait instance-stopped --instance-ids i-xxxxxxxxxxxxxxxxx
aws ec2 modify-instance-cpu-options --instance-id i-xxxxxxxxxxxxxxxxx --nested-virtualization enabled
aws ec2 start-instances --instance-ids i-xxxxxxxxxxxxxxxxx
```
> Requiere AWS CLI v2 ≥ 2.33.21. Si da "Unknown options", actualiza el CLI.

Verifica:
```bash
aws ec2 describe-instances --instance-ids i-xxxxxxxxxxxxxxxxx \
  --query "Reservations[].Instances[].CpuOptions"
```

## Paso 3 — Conectarse por SSH e instalar KVM/libvirt

```bash
ssh -i mi-clave.pem ubuntu@<IP-publica-de-la-instancia>
```

Verifica que la CPU expone las extensiones de virtualización (debe devolver un número > 0):
```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

Instala el comprobador oficial y confirma que KVM es utilizable:
```bash
sudo apt update
sudo apt install -y cpu-checker
kvm-ok
```
Debería responder:
```
INFO: /dev/kvm exists
KVM acceleration can be used
```
Si dice que no puede usarse, revisa el Paso 2 (nested virtualization no quedó activado, o el tipo de instancia no lo soporta).

Instala el stack de virtualización:
```bash
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virtinst
sudo usermod -aG libvirt,kvm $USER
newgrp libvirt
```

Comprueba que el servicio está activo:
```bash
sudo systemctl status libvirtd
virsh list --all
```

## Paso 4 — Crear la red virtual aislada

Este es el equivalente al switch "Internal" de Hyper-V: define una red libvirt **sin** `<forward>`, para que no tenga NAT ni salida hacia la interfaz física.

```bash
cat <<EOF > /tmp/lab-net.xml
<network>
  <name>lab-dhcp</name>
  <bridge name='virbr-lab' stp='on' delay='0'/>
</network>
EOF

sudo virsh net-define /tmp/lab-net.xml
sudo virsh net-start lab-dhcp
sudo virsh net-autostart lab-dhcp
```

> Importante: al **no** incluir ningún bloque `<forward>` ni `<ip>`, esta red queda en modo *isolated* — libvirt no le asigna su propio DHCP interno (que interferiría con el vuestro) ni la conecta a internet. Es justo lo que queremos: un segmento aislado donde el único DHCP sea el vuestro.

Verifica que se creó el puente:
```bash
ip link show virbr-lab
virsh net-list --all
```

## Paso 5 — Crear las máquinas virtuales cliente

Usaremos **Alpine Linux** por ligereza (256–512 MB por VM), igual que en la versión Windows.

### 5.1 Descargar el ISO
```bash
mkdir -p ~/isos ~/vms
wget -O ~/isos/alpine.iso https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/x86_64/alpine-standard-3.20.3-x86_64.iso
ls -lh ~/isos/alpine.iso   # debe rondar 190-250 MB
```

### 5.2 Crear la VM con virt-install (consola de texto, sin necesidad de GUI)
```bash
sudo virt-install \
  --name cliente1 \
  --memory 512 \
  --vcpus 1 \
  --disk path=/var/lib/libvirt/images/cliente1.qcow2,size=4 \
  --cdrom ~/isos/alpine.iso \
  --network network=lab-dhcp \
  --graphics none \
  --console pty,target_type=serial \
  --os-variant alpinelinux3.19
```
Esto te conecta automáticamente a la **consola serie** de la VM en la misma terminal SSH — no necesitas RDP ni VNC. Verás arrancar el live system de Alpine ahí mismo.

> Si `--os-variant alpinelinux3.19` da error porque `osinfo-db` no lo reconoce, quítalo o usa `--os-variant generic` — no afecta a la funcionalidad, solo son optimizaciones de la plantilla.

En el prompt `localhost login:` entra con:
```
root
```
(sin contraseña).

Para salir de la consola serie sin apagar la VM: `Ctrl + ]`.

### 5.3 Reconectar a la consola más tarde
```bash
virsh console cliente1
```

### 5.4 Segundo cliente (opcional)
Repite 5.2 cambiando `--name cliente2` y la ruta del disco.

## Paso 6 — Instalar y configurar isc-dhcp-server en el host

### 6.1 Averiguar la interfaz del host en la red aislada
Al crear la red `lab-dhcp`, libvirt creó el puente `virbr-lab` en el host — es el equivalente al `vEthernet (LAN-Laboratorio-DHCP)` de Windows:
```bash
ip addr show virbr-lab
```

### 6.2 Asignar IP fija al puente (será la puerta de enlace)
```bash
sudo ip addr add 192.168.10.1/24 dev virbr-lab
```
> Para que sobreviva a un reinicio, añádelo también a Netplan (`/etc/netplan/`) o vía `nmcli`, según cómo gestione red tu instancia — para la práctica en clase basta con el comando anterior en cada sesión.

### 6.3 Instalar el servicio
```bash
sudo apt install -y isc-dhcp-server
```

### 6.4 Decirle en qué interfaz debe escuchar
Edita `/etc/default/isc-dhcp-server`:
```bash
sudo nano /etc/default/isc-dhcp-server
```
Y ajusta la línea:
```
INTERFACESv4="virbr-lab"
```

### 6.5 Configurar el ámbito
Edita `/etc/dhcp/dhcpd.conf`:
```bash
sudo nano /etc/dhcp/dhcpd.conf
```
Añade al final:
```
subnet 192.168.10.0 netmask 255.255.255.0 {
  range 192.168.10.100 192.168.10.200;
  option routers 192.168.10.1;
  option domain-name-servers 8.8.8.8;
  option subnet-mask 255.255.255.0;
  default-lease-time 600;
  max-lease-time 7200;
}
```

### 6.6 Arrancar el servicio
```bash
sudo systemctl restart isc-dhcp-server
sudo systemctl status isc-dhcp-server
```
Si falla al arrancar, casi siempre es porque `INTERFACESv4` apunta a una interfaz que no existe todavía o el archivo `dhcpd.conf` tiene un error de sintaxis — revisa con:
```bash
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
```

## Paso 7 — Verificar desde los clientes

En la consola serie de `cliente1` (Alpine):
```sh
ip link show                # confirma el nombre de la interfaz (normalmente eth0)
ip link set eth0 up         # si aparece "state DOWN"
udhcpc -i eth0
```

Deberías ver:
```
udhcpc: sending discover
udhcpc: sending select for 192.168.10.10x
udhcpc: lease of 192.168.10.10x obtained
```

## Paso 8 — Ver el proceso de broadcast y asignación (DORA) en detalle

### 8.1 Leases concedidos (resultado)
```bash
cat /var/lib/dhcp/dhcpd.leases
```

### 8.2 Log del propio servicio en vivo (equivalente al DhcpSrvLog de Windows)
```bash
sudo journalctl -u isc-dhcp-server -f
```
Déjalo corriendo en una terminal SSH y repite `udhcpc -i eth0` en la consola de la VM en otra — verás las líneas DHCPDISCOVER/DHCPOFFER/DHCPREQUEST/DHCPACK en tiempo real, con IP y MAC del cliente.

### 8.3 Captura con tcpdump en el cliente (lado cliente)
```sh
apk add tcpdump
tcpdump -i eth0 -n port 67 or port 68 -v
```

### 8.4 Captura con tcpdump en el host, sobre el puente (lado servidor)
Como no hay GUI en Ubuntu Server, usamos `tcpdump`/`tshark` y, si se quiere inspección visual campo a campo, se exporta el `.pcap` y se abre con Wireshark en el portátil del alumno:
```bash
sudo tcpdump -i virbr-lab -n port 67 or port 68 -w /tmp/dhcp-capture.pcap
```
Detén la captura con `Ctrl+C` tras generar tráfico, y descárgala a tu equipo local para abrirla con Wireshark:
```bash
scp -i mi-clave.pem ubuntu@<IP-instancia>:/tmp/dhcp-capture.pcap .
```
También puedes instalar `tshark` en el propio host si prefieres inspeccionar sin salir de la terminal:
```bash
sudo apt install -y tshark
sudo tshark -i virbr-lab -Y bootp
```

### 8.5 Ejercicios adicionales con valor curricular
- **Reservas por MAC** en `dhcpd.conf`:
```
host cliente1-fijo {
  hardware ethernet 52:54:00:xx:xx:xx;
  fixed-address 192.168.10.50;
}
```
(obtén la MAC con `ip link show eth0` dentro de la VM, o con `virsh domiflist cliente1` desde el host)
- **Exclusiones**: en isc-dhcp-server se hacen dejando fuera del `range` las IPs que no quieres repartir, o usando `deny` con clases.
- **Liberar y renovar**: `udhcpc -R` para liberar y forzar un DISCOVER nuevo; comparar con una simple renovación.
- **Agotamiento del ámbito**: reduce el `range` a 2-3 IPs y lanza 2 clientes a la vez.

---

## Escalar la práctica a varios alumnos/grupos

Igual que en la versión Windows:
1. Una instancia Ubuntu por alumno, siguiendo esta guía manualmente.
2. Crear una **AMI personalizada** una vez tengas el host con KVM/libvirt, la red `lab-dhcp` y las VMs base ya creadas (apagadas) — cada alumno lanza desde esa AMI y solo le queda configurar `isc-dhcp-server`.
3. **CloudFormation/Launch Template** para desplegar N instancias de golpe reutilizando esa AMI.

---

## Notas de coste
- Mismas consideraciones que en la práctica Windows: revisa el precio de `m7i.large` en la [calculadora de AWS](https://calculator.aws), detén las instancias fuera de horario de clase, y valora Spot Instances si la disponibilidad garantizada no es crítica.