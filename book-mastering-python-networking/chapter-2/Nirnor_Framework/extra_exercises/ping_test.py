#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command, netmiko_send_config
import os
from datetime import datetime


nr = InitNornir()
ips_to_test = ["10.10.20.171", "1.1.1.1"]

def ping_task(task):
    for ip in ips_to_test:
        result = task.run(task=netmiko_send_command, command_string=f"ping {ip} repeat 4", enable=True)
        print(f"\n{task.host} ping {ip}:\n{result.result}")

result = nr.run(task=ping_task)
#print_result(result)
