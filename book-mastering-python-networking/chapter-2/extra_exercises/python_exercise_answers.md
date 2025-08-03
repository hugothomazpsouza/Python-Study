# Python Networking Exercise Answers

This repository provides answers to practical Python networking exercises using the `pexpect` library to automate interaction with Cisco IOS devices over Telnet.

## Exercises

- [Exercise 1: Telnet to multiple Cisco IOS devices and collect administratively down interfaces](#exercise-1-telnet-to-multiple-cisco-ios-devices-and-collect-administratively-down-interfaces)

---

```python
import getpass
import pexpect
import sys

devices = {
    'rt-p001': {'prompt': 'R1', 'ip': '10.10.20.171'},
    'rt-p002': {'prompt': 'R2', 'ip': '10.10.20.172'}
}

username = input('Username: ')
password = getpass.getpass('Password: ')

commands = ['show ip int brief | in administratively down']

for device in devices:
    output_file = f'{device}_down_interfaces.txt'
    prompt = devices[device]['prompt']
    ip = devices[device]['ip']

    child = pexpect.spawn(f'telnet {ip}')

    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(f'{prompt}>')

    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)
    child.expect(f'{prompt}#')

    with open(output_file, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(f'{prompt}#')
            f.write(child.before)

    child.sendline('exit')


```
