#!/usr/bin/env python3

import paramiko, getpass, time

devices = {'R1': {'ip': '10.10.20.171'},
           'R2': {'ip': '10.10.20.172'}
}

commands = ['show version\n', 'show run\n']

username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535 

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


# Loop through devices
for device in devices.keys():
    outputFileName = device + '_show_run_output_txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(5)
    new_connection.send('enable\n')
    new_connection.send(f'{password}\n')
    new_connection.send('terminal length 0\n')
    with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(5)
            output = clear_buffer(new_connection)
            print(output.decode())
            f.write(output)

    new_connection.close()
