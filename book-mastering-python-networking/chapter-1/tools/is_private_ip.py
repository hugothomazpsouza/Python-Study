import ipaddress

def is_private_ip(ip_address):
    """ 
    Returns True if the IP address is from a private range, else False. 

    Example of private ranges: - 10.0.0.0/8 - 172.16.0.0/12 - 192.168.0.0/16 
    """
    try:
        ip = ipaddress.ip_address(ip_address)
        return ip.is_private
    except ValueError:
        return False
