#!/usr/bin/env python3

import sys
import io

cfg = open("config.txt", "r")
bitOrder = open("bit_order.txt", "r")
bitFile = open("bits.txt", "w")

cfgData = {}
for line in cfg:
    parts = line.split("=")
    cfgData[parts[0][5:].strip()] = parts[1].strip()
cfg.close()

bits = io.StringIO()
for line in bitOrder:
    line = line.strip()
    if line not in cfgData:
        print("Error: field "+line+" is missing from config")
        exit(1)
    bits.write(cfgData.pop(line))
bitOrder.close()

if len(cfgData) > 0:
    print("Error: the following config fields are missing from bit order")
    for k,v in cfgData.pairs():
        print(k)
    exit(1)

bitFile.write(bits.getvalue()[::-1])
bitFile.close()

print("Generated bits.txt")
