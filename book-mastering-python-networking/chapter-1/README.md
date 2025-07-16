# 🐍 Python Basics for Networking and DevOps

This repository contains beginner-friendly Python examples focused on networking, DevOps, and general programming fundamentals. These notes include string manipulation, lists, tuples, dictionaries, sets, and built-in functions.

---

## 📌 Variables and Strings

```python
a = "networking is fun"
b = 'DevOps is fun too'
c = """what about coding? 
super fun!"""  # Triple quotes allow multi-line strings

for n in a, b, c:
    print(n)
```

---

## 📋 Lists

```python
vendors = ["Cisco", "Arista", "Juniper"]

print(vendors[0][2])    # s
print(vendors[1][0:2])  # Ar
print(vendors[2])       # Juniper
print(vendors[0:2])     # ['Cisco', 'Arista']
```

---

## 📦 Tuples

```python
datacenters = ("SJC1", "LAX1", "SF01", "CA01")

print(datacenters[0])       # SJC1
print(datacenters[1])       # LAX1
print(datacenters[2])       # SF01
print(datacenters[0:3])     # ('SJC1', 'LAX1', 'SF01')
print(datacenters[0][0:2])  # SJ
```

---

## 🔧 Common Built-in Functions

```python
print(len(a))           # 17
print(len(vendors))     # 3

b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(min(b))           # 1
print(max(b))           # 10
```

---

## 🔤 String Methods

```python
print(a.capitalize())   # Networking is fun
print(a.upper())        # NETWORKING IS FUN

b = a.upper()
print(b)                # NETWORKING IS FUN

print(a.split())        # ['networking', 'is', 'fun']

b = a.split()
print(b)                # ['networking', 'is', 'fun']
```

---

## 📑 List Methods

```python
routers = ['r1', 'r2', 'r3', 'r4', 'r5']

print(routers)          # ['r1', 'r2', 'r3', 'r4', 'r5']

routers.append('r6')
print(routers)          # ['r1', 'r2', 'r3', 'r4', 'r5', 'r6']

routers.insert(2, 'r100')
print(routers)          # ['r1', 'r2', 'r100', 'r3', 'r4', 'r5', 'r6']

routers.pop(1)
print(routers)          # ['r1', 'r100', 'r3', 'r4', 'r5', 'r6']
```

---

## 🗺️ Dictionaries (Mappings)

```python
datacenter1 = {'spines': ['r1', 'r2', 'r3', 'r4']}   
print(datacenter1)  # {'spines': ['r1', 'r2', 'r3', 'r4']}

# Appending a 'leafs' key and its values into the existing datacenter1 dictionary
datacenter1['leafs'] = ['l1', 'l2', 'l3', 'l4']
print(datacenter1)  # {'spines': ['r1', 'r2', 'r3', 'r4'], 'leafs': ['l1', 'l2', 'l3', 'l4']}

print(datacenter1['spines'])    # ['r1', 'r2', 'r3', 'r4']
print(datacenter1['leafs'])     # ['l1', 'l2', 'l3', 'l4']
```

---

## 🔁 Sets (Remove Duplicates)

> ⚠️ Sets are unordered and do not support indexing.

```python
a = 'hello'
# Use the built-in function set() to convert the string to a set
print(set(a))   # {'e', 'o', 'h', 'l'} - order may vary each time

b = set([1, 1, 2, 2, 3, 3, 4, 4])
print(b)        # {1, 2, 3, 4}

b.add(5)
print(b)        # {1, 2, 3, 4, 5}

b.update(['a', 'a', 'b', 'b'])
print(b)        # {1, 2, 3, 4, 5, 'b', 'a'}
```


---

## ➕ Python Operators

```python
print(1 + 3)    # 4
print(2 - 1)    # 1
print(1 * 5)    # 5

# Floor division and modulo
print(5 / 1)    # 5.0
print(5 // 2)   # 2
print(5 % 2)    # 1
```

> 📝 Note: 
> - `//` (floor division) truncates the result to an integer.
> - `%` (modulo) returns the remainder.

> Example:
> - examples:
> - 5 // 2 the result is 2 because the result of the division is 2.5
> - 5 % 2 the result is 1 because 5 divided by 2 is 2 with remainder(restante) 1
---

## 🔍 Comparison and Membership Operators

```python
a = 1
b = 2

print(a == b)   # False
print(a > b)    # False
print(a < b)    # True
print(a <= b)   # True

a = 'hello world'

print('h' in a)     # True
print('z' in a)     # False
print('h' not in a) # False
print('z' not in a) # True
```

---

## 🔁 Conditional Statements

```python
a = 10

if a > 1:
    print(str(a) + ' is larger than 1')
elif a < 1:
    print(str(a) + ' is smaller than 1')
else:
    print(str(a) + ' is equal to 1')
```

---

## 🔄 While Loop

```python
a = 10 
b = 1

while b < 10:
    print(b)
    b += 1
```

---

## 🔂 For Loop

```python
a = [100, 200, 300, 400, 500]

for numbers in a:
    print(numbers)
```

---

## 🧩 Python Functions

```python
def subtract(a, b):
    c = a - b
    return c

result = subtract(10, 5)
print(result)   # 5
```

---

## 🧱 Python Classes

```python
class router(object):
    def __init__(self, name, interface_number, vendor):
        self.name = name
        self.interface_number = interface_number
        self.vendor = vendor

r1 = router('CSR100V', 64, 'Cisco')
print(r1.name)              # CSR100V
print(r1.interface_number)  # 64
print(r1.vendor)            # Cisco
```

---

## 📦 Modules and Packages

```python
# File: subtract.py
def subtract(a, b):
    return a - b
```

To import and use in another script in the same directory:

```python
import subtract
result = subtract.subtract(10, 5)
print(result)   # 5
```

To create a package:

```bash
mkdir math_stuff
touch math_stuff/__init__.py
```

Place `subtract.py` inside `math_stuff`, then use:

```python
from math_stuff.subtract import subtract
result = subtract(10, 5)
print(result)   # 5
```
