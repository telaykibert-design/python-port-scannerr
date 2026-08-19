import sys
import ipaddress
def get_ip_class_and_gateway(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        first_octet = int(ip_str.split('.')[0])
        if 1 <= first_octet <= 127:
            ip_class = "class A"
        elif 128 <= first_octet <= 191:
            ip_class = "class B"
        elif 192 <= first_octet <= 223:
            ip_class = "class C"
        elif 224 <= first_octet <= 239:
            ip_class = "class D (Multicast)"
        else:
            ip_class = "class E (Experimental)"
        octets = ip_str.split('.')
        gateway = f"{octets[0]}.{octets[1]}.{octets[2]}.1"
        print(f"Target IP: {ip_str}")
        print(f"IP Class: {ip_class}")
        print(f"Default Gateway: {gateway}")
    except ValueError:
        print("Invalid IP address format.")
if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_ip = sys.argv [1]
    else:
        target_ip = input("Enter IP Address: ")
        get_ip_class_and_gateway(target_ip)