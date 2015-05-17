#!/bin/bash
touch plaintext
python hackPacket.py file.pcap
for file in dir ./packets/*
do
    openssl rsautl -in $file -decrypt -inkey ~/ssl_key/ooghe.key >> plaintext
done
cd packets
rm *
cd ..
cat plaintext
rm plaintext

