import nmap
import sys
def nmap_scanner(target):
    nm = nmap.PortScanner()
    print(f"Scanning target {target} using nmap...")
    nm.scan(target, '1-1024')
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                print(f"Port {port}: {state}")
if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        nmap_scanner(target)
    else:
        target_host = input("Enter Target IP/Hostname: ")
        nmap_scanner(target_host)