import pcapy
from struct import unpack

def packet_handler(header, data):
    # Extract Ethernet header
    eth_header = data[:14]
    eth = unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])

    if eth_protocol == 8:  # IPv4
        # Parse IP header (20 bytes)
        ip_header = data[14:34]
        iph = unpack('!BBHHHBBH4s4s', ip_header)
        source_ip = socket.inet_ntoa(iph[8])
        dest_ip = socket.inet_ntoa(iph[9])

        print(f'Source IP: {source_ip}, Destination IP: {dest_ip}')

# Open network interface for packet capture
cap = pcapy.open_live('eth0', 65536, 1, 0)

# Start capturing packets
cap.loop(0, packet_handler)

#xxxxx
