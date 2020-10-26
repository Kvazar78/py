#!/usr/bin/python3.8

from sys import argv

conf = argv[1]
exit_conf = argv[2]

ignore = ["duplex", "alias", "Current configuration"]
f = open(conf, 'r')
ext = open(exit_conf, 'w')

for line in f:
    for ig in ignore:
        if ig in line:
            break
    else:
        ext.writelines(line)
ext.close()


