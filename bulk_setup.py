from netmiko import ConnectHandler

#Identify the list of ip address informed in the file "ip_address.txt" and add it to the list "lista_ip_final".
list_ip_final = []
with open("ip_address.txt", "r") as address:
    ip_address = address.readlines()
    for ip in ip_address:
        list_ip_final.append(ip.strip())

#Open the file "configuration.txt" to read the settings to be applied and each equipment.
with open("configuration.txt", "r") as file:
    conf_line = file.read().splitlines()

#Loop to establish a connection on each router and apply desired settings.
for address in list_ip_final:
    ip = address
    address = { 
        'device_type': 'cisco_ios', 
        'host': address, 
        'username': 'cisco', 
        'password': 'cisco123', 
    }
    print("\n### Configuration in progress on the host {} ... ###\n".format(ip))
    connect = ConnectHandler(**address)
    configuration = connect.send_config_set(conf_line)
    print(configuration)
    connect.disconnect()

print("\nSettings completed!")