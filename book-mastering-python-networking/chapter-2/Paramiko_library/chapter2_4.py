#!/usr/bin/env python3

import paramiko, getpass, time, json

with open('devices.json', 'r') as f:
    devices = json.load(f)

with open('commands.txt', 'r') as f:
    commands = f.readlines()


username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


# Loop through devices
for device in devices.keys():
    outputFileName = f'{device}_configuration_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    time.sleep(1)
    new_connection.send('enable\n')
    new_connection.send(f'{password}\n')
    output = clear_buffer(new_connection)
    time.sleep(2)
    with open(outputFileName, 'wb') as f:
        for command in commands:
            if command == 'copy run start\n':
                new_connection.send('copy run start\n')
                new_connection.send(' \n')
                time.sleep(3)
            else:
                new_connection.send(command)
                time.sleep(1)
                output = clear_buffer(new_connection)
                print(output.decode())
                f.write(output)

    new_connection.close()
