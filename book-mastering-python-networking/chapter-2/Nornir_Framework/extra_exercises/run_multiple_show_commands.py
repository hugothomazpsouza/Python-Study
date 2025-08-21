#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command, netmiko_send_config
import os
from datetime import datetime


nr = InitNornir()

commands = ["show ip int brief", "show version", "show arp"]

for command in commands:
    print(f'\n### Running {command} ###\n')
    result = nr.run(
        task=netmiko_send_command,
        command_string=command,
        enable=True
    )
    print_result(result)
