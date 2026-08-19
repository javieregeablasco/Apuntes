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

sudo apt install ubuntu-desktop

#### 1.8.2 verificar si gnome se ha instalado correctamente

gnome-shell --version




3. Verificar los paquetes instalados (Ubuntu / Debian)

Si quieres confirmar que el metapaquete del escritorio completo o la sesión están en el sistema:
Bash

dpkg -l | grep -E "gnome-shell|ubuntu-desktop"

Si ves líneas que empiezan por ii, significa que los paquetes están instalados correctamente (ii = Installed/Ok).

reiniciar 
sudo reboot now
    

#### 1.8.3 Asignar contraseña al usuario

sudo passwd ubuntu

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