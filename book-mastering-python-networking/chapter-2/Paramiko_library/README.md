# Paramiko Library

Paramiko is a Python implementation of the SSHv2 protocol. It focuses only on SSHv2 with no Telnet support.

## Installation of Paramiko

It’s pretty straightforward with Python pip. Due to the encryption used for the SSH protocol, there is a hard dependency on the `cryptography` library.

**Cryptography library installation instructions:**  
[https://cryptography.io/en/latest/installation/](https://cryptography.io/en/latest/installation/)

**Paramiko installation steps:**
```bash
pip install cryptography
pip install paramiko
```

---

## Paramiko Overview

### Example Script
```python
import paramiko, time

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect(
    '192.168.2.51',
    username='cisco',
    password='cisco',
    look_for_keys=False,
    allow_agent=False
)
new_connection = connection.invoke_shell()
output = new_connection.recv(5000)
print(output)

stdin, stdout, stderr = connection.exec_command('show version | i V\n')

time.sleep(3)
output = new_connection.recv(5000)
print(output)

new_connection.close()
```

**Example Output:**
```
*************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and     *
* education. IOSv is provided as-is and is not supported by Cisco's     *
* Technical Advisory Center. Any use or disclosure, in whole or in      *
* part, of the IOSv Software or Documentation to any third party for    *
* any purposes is expressly prohibited except as otherwise authorized   *
* by Cisco in writing.                                                  *
*************************************************************************
lax-edg-r1#
show version | i V
Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.8(3)M2, RELEASE SOFTWARE (fc2)
Processor board ID 98U40DKV403INHIULHYHB
lax-edg-r1#
```

---

## Code Breakdown

### 1. `import paramiko`
Imports the Paramiko library, used to make SSH connections to remote devices (Linux servers, Cisco routers, etc.).

### 2. `connection = paramiko.SSHClient()`
Creates an SSH client object called `connection`. It will be used to open the connection, run commands, and manage the session.

### 3. `connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())`
By default, Paramiko won’t connect to unknown hosts (not found in `$HOME/.ssh/known_hosts`).  
This tells Paramiko to automatically accept the host key for unknown devices instead of throwing an error.

### 4. `connection.connect(...)`
Opens an SSH connection to the remote device.

**Arguments:**
- `'192.168.2.51'` → IP address of the remote device
- `username='cisco'` → SSH username
- `password='cisco'` → SSH password
- `look_for_keys=False` → Don’t use local SSH keys
- `allow_agent=False` → Don’t use the SSH agent

These last two ensure only the provided username/password are used.

### 5. `new_connection = connection.invoke_shell()`
Starts an **interactive shell session** with the remote device (like when you SSH manually).

### 6. `output = new_connection.recv(5000)`
Receives data from the shell (up to 5000 bytes).  
This **reads and clears** the buffer to avoid mixing outputs between commands.

### 7. `print(output)`
Prints the received data (usually as a byte string `b'...'`).

### 8. `new_connection.send("show version | i V\n")`
Sends the CLI command `show version | include V`.  
The `\n` simulates pressing **Enter**.

### 9. `time.sleep(3)`
Waits 3 seconds to allow the device to respond.

### 10. `output = new_connection.recv(5000)`
Reads the command output from the buffer.

### 11. `print(output)`
Displays the captured output.

### 12. `new_connection.close()`
Closes the interactive shell session.

---

**Summary:**  
This example demonstrates how to connect to a Cisco router using Paramiko, send commands, receive outputs, and handle session management in Python.


---

## Another Example: `exec_command()` Success Case

### Code:
```python
connection.connect('192.168.2.51', username='cisco', password='cisco',
                   look_for_keys=False, allow_agent=False)
stdin, stdout, stderr = connection.exec_command('show version | i V\n')
stdout.read()
```

### Explanation:
1. **connection.connect(...)** → Connects to a Cisco router using SSH.
2. **exec_command('show version | i V\n')** → Sends the command to the router in a new SSH session channel.
3. **stdout.read()** → Reads the output of that command.

**Sample Output:**
```
Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.8(3)M2, ...
```

---

## Error When Running a New Command After `exec_command()`

### Example Error:
```python
stdin, stdout, stderr = connection.exec_command('show version | i V\n')
Traceback (most recent call last):
...
paramiko.ssh_exception.SSHException: SSH session not active
```

**Why This Happens:**
- Cisco routers often auto-close idle SSH sessions when using `exec_command()`.
- `exec_command()` creates a **temporary** session/channel.
- After it finishes, the channel closes, leaving the connection without an active channel.

**Fixes:**
1. **Reconnect Before Each Command** *(not efficient)*
```python
connection.connect(...)
stdin, stdout, stderr = connection.exec_command(...)
```
2. **Use `invoke_shell()` For Persistent Sessions** *(recommended)*
```python
shell = connection.invoke_shell()
shell.send('show version | i V\n')
time.sleep(2)
output = shell.recv(5000).decode()
print(output)
```

**Comparison Table:**
| Method         | Pros                   | Cons                                     |
|----------------|------------------------|------------------------------------------|
| `exec_command()`| Simple, 1-shot command | Session often closes after 1 use         |
| `invoke_shell()`| Persistent session     | Requires manual handling of I/O          |

---

## Understanding `stdin`, `stdout`, and `stderr` in Paramiko

When you run:
```python
stdin, stdout, stderr = ssh.exec_command('command')
```

### Streams:
- **stdin** → Standard Input (send data to the command)
- **stdout** → Standard Output (command results)
- **stderr** → Standard Error (error messages)

### Example:
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.10.1', username='admin', password='admin')

stdin, stdout, stderr = ssh.exec_command('show version')

output = stdout.read().decode()
error = stderr.read().decode()

if error:
    print("Error found:", error)
else:
    print("Command output:\n", output)

ssh.close()
```

---

## First Paramiko Program Example (from book)

```python
#!/usr/bin/env python

import paramiko, getpass, time

devices = {'lax-edg-r1': {'ip': '192.168.2.51'},
           'lax-edg-r2': {'ip': '192.168.2.52'}}
commands = ['show version\n', 'show run\n']

username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

# Loop through devices
for device in devices.keys():
    outputFileName = device + '_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(5)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(5)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output)

    new_connection.close()
```

---

## About `clear_buffer()` Function

```python
def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)
```

**Purpose:**  
Clears any pending output from the SSH buffer to keep the session in sync.

**Why Important:**  
When automating with `.invoke_shell()`, leftover outputs (e.g., from `enable`, `terminal length 0`, etc.) can interfere with the next command’s output.

**How It Works:**
- `connection.recv_ready()` → Checks if data is available
- `connection.recv(max_buffer)` → Reads and clears the buffer

**Example Usage:**
```python
new_connection.send("terminal length 0\n")
output = clear_buffer(new_connection)
```

**`max_buffer` Definition:**
```python
max_buffer = 65535
```

✅ Summary: Keeps automation clean by ensuring no old output is mixed with new command results.

