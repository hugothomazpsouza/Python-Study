# Netmiko Library Overview

## Introduction
While **Paramiko** is a great library for low-level SSH interactions with Cisco IOS and other vendors, it often requires repeating many steps (login, command execution, etc.).  

**Netmiko**, created and maintained by [Kirk Byers](https://github.com/ktbyers/netmiko), simplifies these processes by abstracting away much of the boilerplate code.

You can find additional examples and tutorials on Kirk’s blog:  
➡️ [https://pynet.twb-tech.com/blog/netmiko-python-library.html](https://pynet.twb-tech.com/blog/netmiko-python-library.html)

---

## Installation

First, activate your virtual environment and install Netmiko:

```bash
(venv) $ pip install netmiko
```

---

## Example 1: Running `show ip int brief`

Compare this with Paramiko — Netmiko reduces the number of lines required.

```python
from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type='cisco_ios',
    host='10.10.20.171',
    username='cisco',
    password='cisco'
)

print(net_connect.find_prompt())  # R1>

output = net_connect.send_command('show ip int brief')
print(output)
```

**Sample Output:**

```
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            10.10.10.100    YES TFTP   up                    up      
Ethernet0/1            1.1.1.1         YES TFTP   up                    up      
Ethernet0/2            10.10.20.171    YES TFTP   up                    up      
Ethernet0/3            unassigned      YES TFTP   administratively down down    
```

---

## Example 2: Configuring a New Interface

In this example, we configure a loopback interface on a Cisco router (DevNet CML sandbox).

```python
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "10.10.20.171",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",  # Enable password
}

net_connect = ConnectHandler(**device)
net_connect.enable()

print(net_connect.find_prompt())  # R1#

commands = [
    'interface loopback2',
    'ip address 2.2.2.2 255.255.255.255',
    'no shutdown'
]

output = net_connect.send_config_set(commands)
print(output)

# Save configuration
save_output = net_connect.save_config()
print(save_output)

net_connect.disconnect()
```

**Sample Output:**

```
R1#
R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#interface loopback2
R1(config-if)#ip address 2.2.2.2 255.255.255.255
R1(config-if)#no shutdown
R1(config-if)#end
R1#
write mem
Building configuration...
[OK]
R1#
```

---

## Summary
With **Netmiko** you can:
- Easily connect to network devices using SSH.  
- Run show commands with fewer lines of code.  
- Send configuration sets in bulk.  
- Save configurations directly from Python.  

Netmiko is highly recommended for network engineers automating repetitive CLI tasks.

