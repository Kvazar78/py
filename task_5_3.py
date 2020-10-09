#!/usr/bin/python3.7

int = input('Введите режим работы интерфейса (access/trunk): ')
type_int = input('Введите тип и номер интерфейса: ')
vlans = input('Введите номер влан(ов): ')

template_int = {
	'0': {
	   "switchport mode access",
	   "switchport access vlan {}",
	   "switchport nonegotiate",
	   "spanning-tree portfast",
	   "spanning-tree bpduguard enable"},
	'1': {
	   "switchport trunk encapsulation dot1q",
	   "switchport mode trunk",
	   "switchport trunk allowed vlan {}"}
	   }

num = str(len(int) % 2)
print('interface ' + type_int)
print('\n'.join(template_int[num]).format(vlans))
