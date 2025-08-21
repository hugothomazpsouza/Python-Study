# Python Networking Exercise Answers

This repository provides answers to practical Python networking exercises using the `With Nornir + Netmiko` library to automate interaction with Cisco IOS devices.

## Beginner Exercises

### Run multiple show commands (run_multiple_show_commands.py)

```python
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
```

---

## Intermediate Exercises

### 1. Check interface status across all devices(check_interface_status.py)
```python
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
```


### 2. Ping test from devices (ping_test.py)
```python
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
```



### 3. Config push (push_configuration.py)
```python
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
```


### 4. Backup device configs (backup_configs.py)
```python
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
```
