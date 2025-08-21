#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command, netmiko_send_config
import os
from datetime import datetime


def backup_config(task):
    os.makedirs('backups', exist_ok=True)
    timestap = datetime.now().strftime("%Y%m%d_%H%M")
    task.run(task=netmiko_send_command, command_string="terminal length 0", enable=True)
    backup = task.run(task=netmiko_send_command, command_string="show run", enable=True)

    with open(f'backups/{task.host}_running_config_{timestap}.txt', 'w') as f:
        f.write(backup.result) 


nr = InitNornir()
result = nr.run(task=backup_config)
print_result(result)
