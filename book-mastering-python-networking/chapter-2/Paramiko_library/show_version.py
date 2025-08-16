#!/usr/bin/env python3

import paramiko
import time
import getpass

user = input('Username: ')
passw = getpass.getpass('Password: ')

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('10.10.20.171', username=user, password=passw, look_for_keys=False, allow_agent=False)


new_connection = connection.invoke_shell()
output = new_connection.recv(5000)
print(output.decode())

new_connection.send('enable\n')
new_connection.send(f'{passw}\n')
time.sleep(1)
output = new_connection.recv(5000)
print(output.decode())

new_connection.send('show version | i V\n')

time.sleep(3)
output = new_connection.recv(5000)
print(output.decode())

new_connection.close()
