#!/usr/bin/env python3

"""Alta3 Research || Author: RZFeeser@alta3.com"""

def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print('Handshaking......connecting with ' +coffeetime)
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' +mycmds)


def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    print("welcome to the network command pusher")

    print("\nData set found\n")

    commandpush(work2do)

main()
