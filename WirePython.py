from scapy.all import *


def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src 
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        length = len(packet)

        print(f"Packet captured:")
        print(f" - Source: {src_ip}")
        print(f" - Destination: {dst_ip}")
        print(f" - Protocol: {protocol}")
        print(f" - Length: {length} bytes")
        print("=" * 50)
        
print("Tool made by: https://github.com/GabrielConforto")
print("-------------------------------------------------")

sniff(prn=packet_callback, filter="ip", count=10)  # Captures 10 packets, adjust however you please
