import sys
from scapy.all import *
import string
import dpkt

def main():
    path = './file.pcap'
    f = open(path)
    pcap = dpkt.pcap.Reader(f)
    udp_n = 0
    tcp_n = 0
    total_packet = 0
    i = 0

    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        total_packet += 1
        if eth.type == 2048:
            ip = eth.data
            if ip.p == 17:
                udp_n += 1
                udp = ip.data
                payload = udp.data
                res = open('./packets/packets' + str(i) + '.txt', 'w')
                res.write(str(payload))
                res.close()
            if ip.p == 6:
                tcp_n += 1
        i += 1
    print('> total : ' + str(total_packet))
    print('> number of udp packets : ' + str(udp_n))
    print('> number of tcp packets : ' + str(tcp_n))

if __name__ == '__main__':
    main()
