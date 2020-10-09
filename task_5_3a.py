#!/usr/bin/python3.7

int = input('Введите режим работы интерфейса (access/trunk): ')
template_qst = {
	'access': 'Введите номер VLAN: ',
	'trunk': 'Введите разрешенные VLANы: '}
print(template_qst[int])
vlans = input()
type_int = input('Введите тип и номер интерфейса: ')
##vlans = input('Введите номер влан(ов): ')

print('\n' + '-' * 30)

template_int = {
	'access': {
	   "switchport mode access",
	   "switchport access vlan {}",
	   "switchport nonegotiate",
	   "spanning-tree portfast",
	   "spanning-tree bpduguard enable"},
	'trunk': {
	   "switchport trunk encapsulation dot1q",
	   "switchport mode trunk",
	   "switchport trunk allowed vlan {}"}
	   }

print('interface ' + type_int)
print('\n'.join(template_int[int]).format(vlans))
