#!/usr/bin/python3.8

from sys import argv

conf = argv[1]
f = open(conf, 'r')

for line in f:
    print(line)

