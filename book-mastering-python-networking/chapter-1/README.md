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

## ✅ Summary

This repository includes:

- ✅ Python fundamentals
- ✅ Data structures: Lists, Tuples, Dictionaries, Sets
- ✅ Built-in functions and methods

---

