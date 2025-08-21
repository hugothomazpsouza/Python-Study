#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command, netmiko_send_config
import os
from datetime import datetime


nr = InitNornir()


def check_interfaces(task):
    result = task.run(task=netmiko_send_command, command_string="show ip int brief", enable=True)
    lines = result.result.splitlines()
    #print(lines)
    down_ints = [line for line in lines if "administratively down" in line]
    if down_ints:
        print(f'{task.host}: Interface admin down -> {down_ints}')


result = nr.run(task=check_interfaces)
print_result(result)
