#!/usr/bin/python3.8

from sys import argv

conf = argv[1]
f = open(conf, 'r')

#print(f.read())
for line in f:
    if '!' in line:
        continue
    else:
        print(line.rstrip())

