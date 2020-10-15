#!/usr/bin/python3.7

f = open('./ospf.txt', 'r')
for line in f:
	ospf = line.split()
	print("Prefix             " + ospf[1])
	print("AD/Metric          " + ospf[2].strip('[]'))
	print("Next-Hop           " + ospf[4].strip(','))
	print("Last update        " + ospf[5].strip(','))
	print("Outbound Interface " + ospf[6])
	print('\n' + '-' * 30)
	
