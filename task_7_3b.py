#!/usr/bin/python3.6

f = open('CAM_table.txt', 'r')
list1 = f.read().split('\n')

for i in range(6):
    list1.pop(0)

a = input('Введи номер VLAN:')

for el in list1:
    if len(el) != 0:
        str = el.split()
        if str[0] == a:
            print(el)


