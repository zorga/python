import sys
from scapy.all import *
import string

def main():
    path = '/home/nico/file.pcap'
    packets = rdpcap(path)
    f = open('packets.txt', 'w')
    for p in packets:
        f.write(str(p.payload))
    f.close()

if __name__ == '__main__':
    main()
