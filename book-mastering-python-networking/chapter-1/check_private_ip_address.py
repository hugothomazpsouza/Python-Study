
from tools.is_private_ip import is_private_ip

ip_list = [
    "10.0.0.1",         # Private
    "172.16.5.4",       # Private
    "192.168.1.100",    # Private
    "8.8.8.8",          # Public (Google DNS)
    "1.1.1.1",          # Public (Cloudflare DNS)
    "172.32.0.1",       # Public (outside private 172.16.0.0/12)
    "192.0.2.1",        # Public (TEST-NET-1)
    "169.254.1.1",      # Link-local (not private)
    "127.0.0.1",        # Loopback (not considered private)
    "100.64.0.1"        # Carrier-grade NAT (special-use, not private)
]

for ip in ip_list:
    result = is_private_ip(ip)
    if result == 1:
        print(f'The {ip} is a Private IP address.')
    else:
        print(f'The {ip} is NOT a Private IP address.')
