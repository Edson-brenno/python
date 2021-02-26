#!/usr/bin/python3.9

import socket
import os
import sys

#e la vamos nos:
arg1 = str("{}".format(sys.argv[0]))
print(arg1)
#if e else para averiguacao de argumento:
if ( len(sys.argv) < 2):
    print("ETB INFORMATION \n")
    print("{} [ip] [how many hosts will be teste]\n".format(sys.argv[0]))
    print("{} 192.168.1.1 0-200 \n".format(sys.argv[0]))
elif (str("{}".format(sys.argv[1])) == "-h"):
    print("ETB INFORMATION \n")
    print("{} [ip] [how many hosts will be teste]\n".format(sys.argv[0]))
    print("{} 192.168.1.1 0-200 \n".format(sys.argv[0]))