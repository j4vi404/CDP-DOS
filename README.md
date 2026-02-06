# 🔴CDP DoS 
# 🔧 Network Security Tool

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)

*Herramienta automatizada para configuración, auditoría y seguridad de infraestructura de red*

</div>

## ⚠️ ADVERTENCIA LEGAL
Este script es exclusivamente para **fines educativos y pruebas de penetración autorizadas**. El uso no autorizado es **ILEGAL**. Use bajo su propia responsabilidad.

---

## 📋 Tabla de Contenidos
- [Objetivo del Script](#objetivo-del-script)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Topología de Red](#topología-de-red)
- [Parámetros Utilizados](#parámetros-utilizados)
- [Medidas de Mitigación](#medidas-de-mitigación)
---
Enlace ataque CDP DOS
https://youtu.be/cN74mOLoX0M?si=GvqW0Xw_nMHO28l5
---
---

## 🎯 Objetivo del Script

Este script demuestra vulnerabilidades críticas en el protocolo CDP (Cisco 
Discovery Protocol) mediante un ataque de Denegación de Servicio (DoS). 
CDP es un protocolo propietario de Cisco que opera en la capa 2 del modelo 
OSI y se utiliza para descubrir dispositivos vecinos en la red. Sin embargo,
al ser un protocolo sin autenticación, es altamente susceptible a ataques
de saturación y envenenamiento de tabla.

El ataque funciona generando masivamente paquetes CDP falsificados que 
saturan la tabla de vecinos del switch/router objetivo, consumiendo recursos
críticos de memoria y CPU. Esto puede provocar degradación del rendimiento,
inestabilidad del sistema, e incluso reinicios inesperados del dispositivo.

### Propósito:
- Saturar la tabla CDP del switch/router objetivo con entradas falsas
- Consumir recursos de memoria y CPU del dispositivo
- Provocar inestabilidad (lentitud, reinicios, caídas)
- Validar configuraciones de seguridad en laboratorios

### Modo de USo:
El script genera paquetes CDP falsos de manera masiva hacia el switch objetivo, llenando su tabla de vecinos CDP hasta agotar recursos del sistema.

```
# Opción 1: HTTPS
git clone https://github.com/j4vi404/CDP-DOS.git

# Opción 2: SSH
git clone git@github.com:j4vi404/CDP-DOS.git

# Entrar al directorio
cd CDP-DOS
```
```
2. Verificar permisos
bash# Dar permisos de ejecución al script
chmod +x CDP.py

# Verificar que existe
ls -lh CDP.py
```
```
# Ejecutar con privilegios root (necesario para Scapy)
sudo python3 CDP.py
```
```
sudo python3 cdp_flood.py
# Ver paquetes CDP en tiempo real
sudo tcpdump -i eth0 -e -n 'ether dst 01:00:0c:cc:cc:cc'

```
```
# Ver vecinos CDP (se llenará de entradas falsas)
Switch# show cdp neighbors

# Ver estadísticas detalladas
Switch# show cdp traffic

```

## 📸 Capturas de Pantalla

### 1. Lab 

<img width="1319" height="863" alt="image" src="https://github.com/user-attachments/assets/637ffc89-67be-4c28-9db1-a57ba8fe49e7" />

---

### 2. Antes del Ataque - Tabla CDP Normal

<img width="1245" height="398" alt="image" src="https://github.com/user-attachments/assets/4b0edf2b-1772-46a0-a3c5-e3515ab74257" />

---
### 3. Durante el Ataque - Tabla CDP Saturada

<img width="1089" height="580" alt="image" src="https://github.com/user-attachments/assets/92525bf5-c752-4c2e-901a-0dd64d20b3b4" />

---

### 4. Ejecución del programa

<img width="849" height="190" alt="image" src="https://github.com/user-attachments/assets/fe24a64e-92ab-40a4-9ff8-953a5c6926d9" />

---

### 5. Consumo de Recursos del Switch

<img width="1248" height="595" alt="image" src="https://github.com/user-attachments/assets/4f7a2ab1-192e-4f34-8b78-431b428a7b2a" />

---

## 🌐 Topología de Red

### Diagrama de Topología

                                  (Cloud)
                                     |
                    +----------------+----------------+
                    |                                 |
                 e0/0                               e0/0
                  R-SD                              R-STG
           (15.0.7.0/24)      10.0.0.0/30           (15.0.8.0/24)
                 e0/2 -------------------------------- e0/2
                    |                                   |
                 e0/1              PNET              e0/1
                    |                                   |
                 e0/0                               e0/0
                  SW-SD                             SW-STG
                 /    \                             /    \
              e0/2    e0/1                       e0/1    e0/2
               |        |                         |        |
              e0       e0                       eth0     eth0
            Victima  Atacante                    TI       TI
```

### Direccionamiento IP

| Dispositivo | IP Address | Interface | Rol |
|-------------|------------|-----------|-----|
| Atacante | 192.168.1.100 | eth0 | Kali Linux |
| SW-CORE-01 | 192.168.1.1 | Vlan10 | Switch objetivo |
| PC-1 | 192.168.1.10 | eth0 | Usuario |
| PC-2 | 192.168.1.20 | eth0 | Usuario |

---

## ⚙️ Parámetros Utilizados

### Configuración del Script

```python
# Parámetros principales
INTERFACE = "eth0"                    # Interface de red
DELAY = 0.05                          # 50ms entre paquetes (20 pps)
DEVICE_PREFIX = "LAB-"                # Prefijo para nombres falsos
RANDOM_RANGE = (1000, 9999)           # Rango de números aleatorios

# Parámetros CDP
CDP_VERSION = 0x02                    # CDP versión 2
CDP_TTL = 0xb4                        # 180 segundos
CDP_MULTICAST_MAC = "01:00:0c:cc:cc:cc"  # MAC multicast CDP
```

### TLVs (Type-Length-Value) Incluidos

| Type | Nombre | Descripción | Valor |
|------|--------|-------------|-------|
| 0x0001 | Device ID | Nombre del dispositivo | LAB-XXXX (aleatorio) |
| 0x0003 | Port ID | Puerto de origen | GigabitEthernet0/1 |
| 0x0004 | Capabilities | Capacidades | 0x00000001 (Router) |

---
### Software Requerido

```bash
# Python 3.8+
python3 --version

# Instalar Scapy
pip3 install scapy

# O desde repositorios
sudo apt-get install python3-scapy
```


### 🛡️ Medidas de Mitigación

## 1. Desactivar CDP Globalmente 

```cisco
! Desactivar CDP en todo el dispositivo
Switch(config)# no cdp run

! Verificar
Switch# show cdp
CDP is not enabled
```

**Justificación:** CDP NO es necesario para el funcionamiento normal de la red.

### 2. Desactivar CDP por Interface

```cisco
! Desactivar en interfaces específicas
Switch(config)# interface range GigabitEthernet0/1-24
Switch(config-if-range)# no cdp enable
Switch(config-if-range)# exit
```

### 3. Port Security

```cisco
Switch(config)# interface GigabitEthernet0/24
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security violation shutdown
```

### 4. Storm Control

```cisco
! Limitar tráfico multicast
Switch(config)# interface range GigabitEthernet0/1-24
Switch(config-if-range)# storm-control multicast level 10.00
Switch(config-if-range)# storm-control action shutdown
```

### 5. CPU Rate Limiting

```cisco
Switch(config)# mls qos
Switch(config)# mls rate-limit all cdp 50 10
```

### 6. VACLs (Filtrado de CDP)

```cisco
! Crear ACL para bloquear CDP
Switch(config)# mac access-list extended BLOCK-CDP
Switch(config-ext-macl)# deny any host 0100.0ccc.cccc
Switch(config-ext-macl)# permit any any
Switch(config-ext-macl)# exit

! Aplicar a VLAN
Switch(config)# vlan access-map CDP-FILTER 10
Switch(config-access-map)# match mac address BLOCK-CDP
Switch(config-access-map)# action drop
Switch(config-access-map)# exit
Switch(config)# vlan filter CDP-FILTER vlan-list 10
```

### 7. Configuración de Baseline Completa

```cisco
 === MITIGACIÓN COMPLETA ===

 1. Desactivar CDP
no cdp run

 2. Port Security
interface range GigabitEthernet0/1-24
  switchport port-security
  switchport port-security maximum 2
  switchport port-security violation restrict
  storm-control multicast level 5.00
  no cdp enable
exit

 3. Rate Limiting
mls qos
mls rate-limit all cdp 50 10

 4. Logging
logging buffered 64000
snmp-server enable traps cdp

 5. Guardar
write memory
```

### 8. Checklist de Seguridad

```
☐ Desactivar CDP globalmente (no cdp run)
☐ Si CDP es necesario, solo en interfaces trunk de gestión
☐ Port-security en puertos de acceso
☐ Storm-control en todas las interfaces
☐ CPU rate limiting para CDP
☐ VACLs para filtrar CDP en VLANs de usuario
☐ Logging y SNMP traps habilitados
☐ IDS/IPS con reglas CDP
☐ Auditorías periódicas (show cdp)
☐ IOS actualizado con parches de seguridad
```

---

```

### Monitoreo Durante el Ataque

```bash
# Terminal 1: Ejecutar script
sudo python3 CDP.py

# Terminal 2: Monitorear tráfico CDP
sudo tcpdump -i eth0 -e -n 'ether dst 01:00:0c:cc:cc:cc'

# Terminal 3: Ver tabla CDP del switch (si tienes acceso)
# Switch# show cdp neighbors
```

### Análisis con Wireshark

```bash
# Capturar tráfico
sudo tcpdump -i eth0 -w cdp_attack.pcap

# Abrir en Wireshark
wireshark cdp_attack.pcap

# Filtro en Wireshark: cdp
```

### Herramientas
- **Scapy**: https://scapy.net/
- **Wireshark**: https://www.wireshark.org/
- **Yersinia**: Framework para ataques layer 2

---

## ⚖️ Descargo de Responsabilidad

**USO EXCLUSIVAMENTE EDUCATIVO**

✅ **Permitido:**
- Laboratorios controlados
- Pruebas de penetración autorizadas
- Educación en ciberseguridad

❌ **PROHIBIDO:**
- Uso sin autorización
- Atacar sistemas de terceros
- Redes de producción
- Actividades ilegales

El autor NO se hace responsable del mal uso de esta herramienta.

---

**Autor:** Sr.J4VI MINYETE  
