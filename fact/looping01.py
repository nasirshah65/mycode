#!/usr/bin/env python3

dnsfile = open("dnsservers.tx", "r")
dnslist = dnsfile.readlines()

for svr in dnslist:
    print(svr, end="")

#close your file
dnsfile.close()
