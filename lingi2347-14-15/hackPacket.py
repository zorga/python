import sys
import dpkt

def checkArgs(func):
    def wrapper():
        if not (len(sys.argv) > 1):
            print("This program takes a pcap file in argument !")
        else:
            func()
    return wrapper

@checkArgs
def readPayloads():
    f = open(sys.argv[1])
    i = 0
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        if eth.type == 2048: # type 2048 -> IPv4
            ip = eth.data
            if ip.p == 17: # 17 -> UDP
                udp = ip.data
                payload = udp.data
                res = open('./packets/packets' + str(i) + '.txt', 'w')
                res.write(str(payload))
                res.close()
        i += 1
    print("payloads retrieved successfully ! :) ")

def main():
    readPayloads()

if __name__ == '__main__':
    main()
