
# Python for Networking – Practice Notes

## 1. Variables and Strings

```python
rt_hostname = "R1-SJC"
rt_interface = "GigabitEthernet0/1"
print(f'{rt_hostname} - Interface: {rt_interface}')  # Output: R1-SJC - Interface: GigabitEthernet0/1

description = 'Link to Switch SW1'
print(description.upper())      # Output: LINK TO SWITCH SW1
words = description.split()
print(words[-1])                # Output: SW1

# Extra examples
print(description.lower())          # Output: link to switch sw1
print(description.capitalize())     # Output: Link to switch sw1
print(description.split())          # Output: ['Link', 'to', 'Switch', 'SW1']
```

## 2. Lists

```python
vlan_id = [10, 20, 30, 40]
print(vlan_id)

vlan_id.append(50)
vlan_id.insert(1, 15)
print(vlan_id)

vlan_id.pop(3)
print(vlan_id)
```

## 3. Tuples

```python
core_routers = ('R1-NYC', 'R2-LON', 'R3-TYO')
print(core_routers)
print(core_routers[0:2])

for router in core_routers:
    print(router[3:])
```

## 4. Built-in Functions

```python
ping_ms = [12, 20, 35, 5, 18]
print(ping_ms)
print(min(ping_ms))
print(max(ping_ms))
```

## 5. String Methods

```python
sw_name = 'sw1-core'
print(sw_name.capitalize())
print(sw_name.upper())
print(sw_name.split('-'))
```

## 6. List Methods

```python
fw_zones = ['inside', 'outside', 'dmz']
print(fw_zones)

fw_zones.append('guest')
print(fw_zones)

fw_zones.insert(2, 'management')
print(fw_zones)

fw_zones.pop(1)
print(fw_zones)
```

## 7. Dictionaries

```python
router = {"hostname": "R1", "interfaces": ["Gig0/0", "Gig0/1"], "location": "datacenter1"}
print(router)

router["vendor"] = "Cisco"
print(router)

print(router['location'])
```

## 8. Sets

```python
ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3"]
print(ip_addresses)

ip_addresses = set(ip_addresses)
print(ip_addresses)

ip_addresses.add("192.168.1.4")
print(ip_addresses)

ip_addresses.update(["192.168.1.5", "192.168.1.6"])
print(ip_addresses)
```

## 9. Operators

```python
a = 5
b = 8

total_vlans = a + b
print(total_vlans)

d = total_vlans / 2
print(d)

is_divisible_by_4 = total_vlans % 4 == 0
print(is_divisible_by_4)
```

## 10. Comparison and Membership

```python
bandwidth_1 = 100
bandwidth_2 = 1000

print(bandwidth_1 > bandwidth_2)

description = "Device eth0 is active"
print("eth0" in description)
print("eth0" not in description)
```

## 11. Conditional Statements

```python
interface_status = "down"

if interface_status == "up":
    print('The interface is operational')
elif interface_status == "admin-down":
    print('Interface is administratively down')
else:
    print('Interface is not operational')
```

## 12. While Loop

```python
reponse = False
attempts = 0

while not reponse and attempts < 5:
    print("Pinging server... attempt", attempts + 1)
    attempts += 1
```

## 13. For Loop

```python
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

for ip in ip_addresses:
    last_octet = int(ip.split('.')[-1])
    if last_octet % 2 == 0:
        print(f'Pinging {ip}')
```

## 14. Functions

```python
def bandwidth(mbps, duration):
    mbps_to_mbytes_per_sec = mbps / 8
    total_data_mb = mbps_to_mbytes_per_sec * duration
    return total_data_mb

mbps = 100
duration = 120

total_data = bandwidth(mbps, duration)
print(f'Total data transferred in megabytes (MB): {total_data} with a transfer rate of {mbps}mbps in {duration}s.')
```
