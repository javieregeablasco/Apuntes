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

- Recomendado para uso educativo: **`m7i.xlarge`** o **`m7i.2xlarge`** (4/8 vCPU, 16/32 GB RAM) — suficiente para 1 servidor + 2-3 clientes ligeros (2 GB RAM cada VM cliente, 4 GB el servidor).
- Si el grupo va a correr VMs más pesadas o con GUI completa, sube a `m7i.4xlarge`.
- Comprueba que la **región** que vais a usar ya tiene la característica activa (el despliegue empezó por `us-west-2` y se fue extendiendo; confirmadlo en la consola al configurar la instancia — si no aparece la opción, probad otra región o usad el CLI).

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

## Paso 3 — Conectarse a la instancia y activar Hyper-V

1. Conéctate por **RDP** (obtén la contraseña con "Get Windows password" en la consola EC2).
2. Abre PowerShell como administrador e instala el rol Hyper-V:
```powershell
Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart
```
3. Tras el reinicio, abre **Hyper-V Manager**.

## Paso 4 — Crear el switch virtual interno

En Hyper-V Manager → **Virtual Switch Manager** → **New virtual network switch**:
- Tipo: **Internal** (o **Private**, si no quieres que ni siquiera la instancia anfitriona tenga IP en esa red).
- Nombre sugerido: `LAN-Laboratorio-DHCP`.

Esto asegura que el tráfico DHCP nunca sale hacia la red de AWS ni a otras instancias.

## Paso 5 — Crear las máquinas virtuales

Dentro de Hyper-V, crea:
- **1 VM "SRV-DHCP"**: Windows Server 2022, adaptador de red conectado a `LAN-Laboratorio-DHCP`. Aquí instalarás el rol DHCP.
- **2-3 VMs "CLIENTE-X"**: Windows 10/11 (o Server con GUI si prefieres uniformidad), mismo switch interno, configuradas para obtener IP automáticamente (comportamiento por defecto).

Tip de recursos: usa **discos diferenciales (differencing disks)** a partir de una VHDX "maestra" ya generalizada (sysprep) para no tener que instalar el SO 4 veces y ahorrar espacio/tiempo.

## Paso 6 — Configurar el rol DHCP en SRV-DHCP

Dentro de la VM `SRV-DHCP`:
```powershell
Install-WindowsFeature -Name DHCP -IncludeManagementTools
```
Luego, en la consola DHCP (o vía PowerShell):
```powershell
Add-DhcpServerV4Scope -Name "Aula-SMR" -StartRange 192.168.10.100 -EndRange 192.168.10.200 -SubnetMask 255.255.255.0
Set-DhcpServerV4OptionValue -ScopeId 192.168.10.0 -DnsServer 8.8.8.8 -Router 192.168.10.1
Add-DhcpServerInDC   # autorización en AD si hay dominio; si es standalone, autorizar no aplica igual
```
Actívalo desde la consola gráfica (**DHCP → clic derecho al ámbito → Activate**) para que los alumnos vean el proceso completo también por GUI, no solo por PowerShell — es lo que evaluaréis normalmente en el ciclo.

## Paso 7 — Verificar desde los clientes

En cada `CLIENTE-X`:
```cmd
ipconfig /release
ipconfig /renew
ipconfig /all
```
Los alumnos deberían ver la IP asignada dentro del rango del ámbito, la puerta de enlace y DNS entregados por el servidor. En `SRV-DHCP`, la consola DHCP mostrará los **leases activos** (Address Leases), y se puede capturar el intercambio DORA con Wireshark instalado dentro de las VMs para verlo a nivel de trama.

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
