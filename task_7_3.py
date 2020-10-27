#!/usr/bin/python3.8

f = open('CAM_table.txt', 'r')
list = f.read().split('\n')

for i in range(6):
    list.pop(0)

for el in list:
    print(el.replace('DYNAMIC', ''))
