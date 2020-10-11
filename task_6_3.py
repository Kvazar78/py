#!/usr/bin/python3.7

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, command_end in trunk.items():
    print("interface FastEthernet" + intf)
    vlans = ' '.join(command_end)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            print(f" {command} {vlans}")
        else:
            print(f" {command}")
