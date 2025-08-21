#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command, netmiko_send_config
import os
from datetime import datetime


def push_config(task):
    cfg = [
        "interface loopback100",
        "description NORNIR_TEST",
        "ip address 100.100.100.100 255.255.255.255"
    ]
    check = task.run(task=netmiko_send_command, command_string="show ip int brief", enable=True)
    lines = check.result.splitlines()
    
    # Check if the interface already exists
    check_loopback100 = [line for line in lines if "Loopback100" in line]
    if check_loopback100:
        print(f"The Loopback100 interface already exists")
    else:
        task.run(task=netmiko_send_config, config_commands=cfg, enable=True)

    #verify = task.run(task=netmiko_send_command, command_string="show ip int brief", enable=True)   
    #print(f'\n{task.host} verification:\n{verify.result}')


nr = InitNornir()
result = nr.run(task=push_config)
print_result(result)
