import socket
import sys
def raw_port_scanner(target,start_port=1, end_port=1024):
    print(f"scanning target: {target}")
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
       print("Hostname could not be resolved.")
       sys.exit()
    for port in range(start_port, end_port + 1):
        try:
         print(f"scanning port: {port}...")
         s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.settimeout(0.5)
         result = s.connect_ex((target_ip, port))
         if result == 0:
            print(f"port {port} is open")
        except Exception:
            pass
        finally: 
            s.close()
if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_host = sys.argv[1]
    else:
        target_host = input("Enter Target IP/Hostname: ")
    raw_port_scanner(target_host) 