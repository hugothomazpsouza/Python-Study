# Nornir Framework

Nornir is an automation framework written in Python to be used with Python.  
It was not created to replace tools like **Netmiko** or **Napalm**, but rather designed to work with them.

---

## Installation

Install Nornir and required plugins:

```bash
pip install nornir nornir_utils nornir_netmiko
```

---

## Inventory Setup

Nornir expects an inventory file (`hosts.yaml`) in **YAML format**.

### Example `hosts.yaml`:

```yaml
R1:
    hostname: '10.10.20.171'
    port: 22
    username: 'cisco'
    password: 'cisco'
    platform: 'cisco_ios'

R2:
    hostname: '10.10.20.172'
    port: 22
    username: 'cisco'
    password: 'cisco'
    platform: 'cisco_ios'
```

---

## Example: Running a Command

### Script (`chapter2_5.py`):

```python
#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir()

result = nr.run(
    task=netmiko_send_command,
    command_string="show arp"
)

print_result(result)
```

### Output:

```
* R1 ** changed : False ********************************************************
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  1.1.1.1                 -   aabb.cc00.0310  ARPA   Ethernet0/1
Internet  1.1.1.2                27   aabb.cc00.0410  ARPA   Ethernet0/1
Internet  10.10.10.100            -   aabb.cc00.0300  ARPA   Ethernet0/0

* R2 ** changed : False ********************************************************
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  1.1.1.1                27   aabb.cc00.0310  ARPA   Ethernet0/1
Internet  1.1.1.2                 -   aabb.cc00.0410  ARPA   Ethernet0/1
Internet  20.20.20.100            -   aabb.cc00.0400  ARPA   Ethernet0/0
```

---

## Extra Exercise: Run Multiple Commands

Modify the script to collect **`show ip int brief`**, **`show version`**, and **`show arp`**.

### Extended Inventory with Logging:

```yaml
R1:
    hostname: '10.10.20.171'
    port: 22
    username: 'cisco'
    password: 'cisco'
    platform: 'cisco_ios'
    connection_options:
        netmiko:
          extras:
            secret: 'cisco'
            session_log: logs/R1.log

R2:
    hostname: '10.10.20.172'
    port: 22
    username: 'cisco'
    password: 'cisco'
    platform: 'cisco_ios'
    connection_options:
        netmiko:
          extras:
            secret: 'cisco'
            session_log: logs/R2.log
```

### Script (`run_multiple_show_commands.py`):

```python
#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

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

## Example Output (Truncated)

```
### Running show ip int brief ###
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            10.10.10.100    YES TFTP   up                    up
Ethernet0/1            1.1.1.1         YES TFTP   up                    up

### Running show version ###
Cisco IOS Software [Dublin], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.12.1

### Running show arp ###
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  1.1.1.1                 -   aabb.cc00.0310  ARPA   Ethernet0/1
Internet  1.1.1.2                45   aabb.cc00.0410  ARPA   Ethernet0/1
```

---

## Extra Information

For more information about the Nornir framework, check out this excellent post by **Syed Asif**:  
🔗 [Getting Started with Nornir for Python Network Automation](https://medium.com/@sydasif78/getting-started-with-nornir-for-python-network-automation-6c23de5744af)

📄 A PDF copy of this article is included in this project:  
**`Extra_information_Nornir_for_Python_Network_Automation_writed_by_Syed_Asif.pdf`**

