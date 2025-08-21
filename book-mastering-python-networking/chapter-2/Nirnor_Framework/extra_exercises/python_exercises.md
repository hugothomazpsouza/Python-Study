# Nornir Exercises

This repository contains extra and intermediate Nornir exercises for network automation practice.

### 💡 I ran this exercises via Cisco DevNet Sandbox Lab (CML)

---

## Beginner Exercises

### Run multiple show commands
- Change your script so it collects:
  - `show ip int brief`
  - `show version`
  - `show arp`
- Print the outputs nicely per device.

---

## Intermediate Exercises

### 1. Check interface status across all devices
- Run `show ip int brief` on all devices.
- Parse the output (textfsm/jinja2) to find which interfaces are administratively down.

### 2. Ping test from devices
- Create a list of IPs to test.
- Use Nornir to send `ping <IP>` commands from all routers.
- Report which pings succeed/fail.

### 3. Config push
- Use `netmiko_send_config` to configure:
  ```
  interface loopback100
   description NORNIR_TEST
   ip address 10.10.10.1 255.255.255.255
  ```
- Verify afterwards with `show ip int brief`.
- If this `loopback100` already exists, don't recreate it.

### 4. Backup device configs
- Automate running `show running-config` on all devices.
- Save results to timestamped files (e.g., `backups/R1_running_{today}.txt`).

---

### Tips:
Each assumes your hosts.yaml contains something like:

````yaml
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


All scripts start with the same imports:
```python
#!/usr/bin/env python3
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command, netmiko_send_config
import os
from datetime import datetime
```

Happy Automating with Nornir
