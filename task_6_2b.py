#!/usr/bin/python3.7

addr = 0

while addr == 0:
    addr = 1
    ip = input('Введи IP-адрес :').split('.')
    if len(ip) == 4:
        for num in ip:
            try:
                num = int(num)
            except ValueError:
                addr = 0
                break
            else:
                if num < 0 or num > 255:
                    addr = 0
                    break
    else:
        addr = 0

if addr == 1:
    if 1 <= int(ip[0]) <= 223:
        print('unicast')
    elif 224 <= int(ip[0]) <= 239:
        print('multicast')
    elif int(ip[0]) == 0 and int(ip[1]) == 0 and int(ip[2]) == 0 and int(ip[3]) == 0:
        print('unassigned')
    elif int(ip[0]) == 255 and int(ip[1]) == 255 and int(ip[2]) == 255 and int(ip[3]) == 255:
        print('local broadcast')
    else:
        print('unused')
