#!/usr/bin/python3.8

from sys import argv

conf = argv[1]
ignore = ["duplex", "alias", "Current configuration"]
f = open(conf, 'r')

for line in f:
    for ig in ignore:
        if ig in line:
            break
    else:
        print(line.rstrip())

