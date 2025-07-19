# 🧠 Python Exercises with Networking Context

## 1. Variables and Strings
- Store a router hostname (e.g., "R1-SJC") and interface name ("GigabitEthernet0/1") as strings. Combine them to form a full interface description and print it.
- Given a description "Link to Switch SW1":
  - Convert it to uppercase.
  - Split the string to get the last word (the connected device).

## 2. Lists
- Create a list of VLAN IDs assigned to a switch: [10, 20, 30, 40]. Print the second and last VLAN.
- Add VLAN 50 to the list. Insert VLAN 15 at position 1. Remove VLAN 30.

## 3. Tuples
- Create a tuple of core router hostnames located in different cities: ("R1-NYC", "R2-LON", "R3-TYO"). Print the first two using slicing.
- Print the city code (last three letters) from each router name.

## 4. Built-in Functions
- Create a list of ping response times (in ms): [12, 20, 35, 5, 18].
- Print the number of samples.
- Find the minimum and maximum response times.

## 5. String Methods
- Given a device name "sw1-core":
  - Capitalize the name.
  - Convert it to uppercase.
  - Split the name using the `-` as a delimiter.

## 6. List Methods
- Create a list of firewall zones: ["inside", "outside", "dmz"].
- Add a new zone "guest".
- Insert "management" before "dmz".
- Remove "outside" using pop.

## 7. Dictionaries
- Create a dictionary to represent a router with interfaces:
```python
{
    "hostname": "R1",
    "interfaces": ["Gig0/0", "Gig0/1"],
    "location": "datacenter1"
}
```
- Add a "vendor" key with the value "Cisco".
- Print the router's location and all interface names.

## 8. Sets
- You receive a list of IPs scanned from the network: ["192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3"]
- Convert to a set to eliminate duplicates.
- Add a new IP "192.168.1.4".
- Add multiple IPs: "192.168.1.5", "192.168.1.6".

## 9. Operators
- Assume two devices support 5 and 8 VLANs respectively. Use arithmetic operators to:
  - Calculate the total VLANs.
  - Find the average.
  - Use modulo to check if the total VLANs is divisible by 4.

## 10. Comparison and Membership
- Given two bandwidth values (e.g., 1000 Mbps and 100 Mbps), compare them using relational operators.
- Check if "eth0" is part of a string "Device eth0 is active".

## 11. Conditional Statements
- Create a variable `interface_status = "down"` and print:
  - "Interface is operational" if up
  - "Interface is administratively down" if admin-down
  - "Interface is not operational" for anything else

## 12. While Loop
- You are pinging a server until it responds. Simulate this with:
```python
response = False
attempts = 0
```
- Use a while loop to simulate ping attempts until attempts reach 5.

## 13. For Loop
- Loop through a list of IP addresses: ["10.0.0.1", "10.0.0.2", "10.0.0.3"].
- Print: "Pinging <ip>" for each.
- Only print IPs ending in even numbers.

## 14. Functions
- Write a function `calculate_bandwidth(mbps, duration)` that returns the total data in MB transferred.
- Use this function for:
  - mbps = 100, duration = 60 seconds

## 15. Classes
- Create a class `Firewall` with attributes: hostname, interfaces, and rules.
- Initialize a firewall with 3 interfaces and 2 rules.
- Print the hostname and number of rules.

## 16. Modules and Packages
- Create a file `tools.py` with a function `is_private_ip(ip_address)` that returns True if the IP is from a private range.
- In another script, import this function and test with "10.0.0.1" and "8.8.8.8".
