# 1. Variables and Strings

rt_hostname = "R1-SJC"
rt_interface = "GigabitEthernet0/1"

print(f'{rt_hostname} - Interface: {rt_interface}')     #output: R1-SJC - Interface: GigabitEthernet0/1


description = 'Link to Switch SW1'

print(description.upper())      #output: LINK TO SWITCH SW1
words = description.split()     
print(words[-1])                #output: SW1

#extra examples
print(description.lower())          #output: link to switch sw1
print(description.capitalize())     #output: Link to switch sw1
print(description.split())          #output: ['Link', 'to', 'Switch', 'SW1']


###########################

# 2. Lists

vlan_id = [10, 20, 30, 40]
print(vlan_id)          #output: [10, 20, 30, 40]

vlan_id.append(50)      
vlan_id.insert(1, 15)
print(vlan_id)          #output: [10, 15, 20, 30, 40, 50]

vlan_id.pop(3)
print(vlan_id)          #output: [10, 15, 20, 40, 50]


###########################

# 3. Tuples

core_routers = ('R1-NYC', 'R2-LON', 'R3-TYO')

print(core_routers)         #output: ('R1-NYC', 'R2-LON', 'R3-TYO')
print(core_routers[0:2])    #output: ('R1-NYC', 'R2-LON')

for router in core_routers:
    print(router[3:])       #output:    NYC
                            #           LON
                            #           TYO
                            
                            
###########################

# 4. Built-in Functions

ping_ms = [12, 20, 35, 5, 18]

print(ping_ms)          #output: [12, 20, 35, 5, 18]
print(min(ping_ms))     #output: 5
print(max(ping_ms))     #output: 35


###########################

# 5. String Methods

sw_name = 'sw1-core'

print(sw_name.capitalize())     #output: Sw1-core
print(sw_name.upper())          #output: SW1-CORE
print(sw_name.split('-'))       #output: ['sw1', 'core']


###########################

# 6. List Methods

fw_zones = ['inside', 'outside', 'dmz']

print(fw_zones)                     #output: ['inside', 'outside', 'dmz']
fw_zones.append('guest')
print(fw_zones)                     #output: ['inside', 'outside', 'dmz', 'guest']
fw_zones.insert(2, 'management') 
print(fw_zones)                     #output: ['inside', 'outside', 'management', 'dmz', 'guest']    
fw_zones.pop(1) 
print(fw_zones)                     #output: ['inside', 'management', 'dmz', 'guest']


###########################

# 7. Dictionaries

router = {"hostname" : "R1", "interfaces" : ["Gig0/0", "Gig0/1"], "location" : "datacenter1"}

print(router)   #output: {'hostname': 'R1', 'interfaces': ['Gig0/0', 'Gig0/1'], 'location': 'datacenter1'}
router["vendor"] = "Cisco"
print(router)   #output: {'hostname': 'R1', 'interfaces': ['Gig0/0', 'Gig0/1'], 'location': 'datacenter1', 'vendor': 'Cisco'}

print(router['location'])   #output: datacenter1

###########################

# 8. Sets

ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3"]

print(ip_addresses) #output: ['192.168.1.1', '192.168.1.2', '192.168.1.1', '192.168.1.3']
ip_addresses = set(ip_addresses)
print(ip_addresses) #output: {'192.168.1.3', '192.168.1.2', '192.168.1.1'}
ip_addresses.add("192.168.1.4")
print(ip_addresses) #output: {'192.168.1.3', '192.168.1.2', '192.168.1.4', '192.168.1.1'}
ip_addresses.update(["192.168.1.5", "192.168.1.6"])
print(ip_addresses) #output: {'192.168.1.2', '192.168.1.6', '192.168.1.5', '192.168.1.4', '192.168.1.1', '192.168.1.3'}


###########################

# 9. Operators

a = 5
b = 8

total_vlans = a + b
print(total_vlans)      #output: 13

d = total_vlans / 2
print(d)                #output: 6.5

is_divisible_by_4 = total_vlans % 4 == 0
print(is_divisible_by_4)                    #output: False

    

###########################

# 10. Comparison and Membership

bandwidth_1 = 100
bandwidth_2 = 1000

print(bandwidth_1 > bandwidth_2)        #output: False

description = "Device eth0 is active"

print("eth0" in description)            #output: True

#extra test
print("eth0" not in description)        #output: False


###########################

# 11. Conditional Statements

interface_status = "down"

if interface_status == "up":
    print(f'The interface is operational')
elif interface_status == "admin-down":
    print(f'Interface is administratively down')
else:
    print(f'Interface is not operational')
    

###########################

# 12. While Loop

reponse = False
attempts = 0

while not reponse and attempts < 5:
    print("Pinging server... attempt", attempts + 1)
    attempts += 1


###########################

# 13. For Loop

ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

# First option
for ip in ip_addresses:
    last_octet = int(ip.split('.')[-1]) # OR "print(int(ip[-1]))" will GET THE LAST octet
    if last_octet % 2 == 0:
        print(f'Pinging {ip}')

#Second option
for ip in ip_addresses:
    if int(ip[-1]) % 2 == 0:
        print(f'Pinging {ip}')
        


###########################

#14. Functions

def bandwidth(mbps, duration):
    """
    Calculates the total data transferred in MB given bandwidth in Mbps and duration in seconds.

    Args:
        mbps: Bandwidth in megabits per second.
        duration: Duration in seconds.

    Returns:
        Total data transferred in megabytes (MB).
    """
    # Convert Mbps to MBps (Megabytes per second)
    mbps_to_mbytes_per_sec = mbps / 8
    # Calculate total data in MB
    total_data_mb = mbps_to_mbytes_per_sec * duration
    return total_data_mb

mbps = 100
duration = 120

total_data = bandwidth(mbps, duration)

print(f'Total data transferred in megabytes (MB): {total_data} with a tranfer rate of the {mbps}mbps in {duration}s.')
