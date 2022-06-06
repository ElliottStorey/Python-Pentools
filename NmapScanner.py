import nmap

scanner = nmap.PortScanner()

ip = input('Enter the ip to scan: ')

print(f'Scanning...{ip}')

res = input('Enter scan type:\n1 - SYN ACK\n2 - UDP\n3 - COMPREHENSIVE\n')

print(f'You selected: {res}')

def scan(s_methods, s_type):
    print(f'Nmap Version {scanner.nmap_version()}')
    scanner.scan(ip, '1-1024', s_methods)
    print(scanner.scaninfo())
    print(f'IP Status: {scanner[ip].state()}')
    print(f'Protocols: {scanner[ip].all_protocols()}')
    print(f'Open Ports: {scanner[ip][s_type].keys()}')

if res == '1':
    scan('-v sS', 'tcp')
elif res == '2':
    scan('-v sU', 'udp')
elif res == '3':
    scan('-v -sS -sV -sC -A -O', 'tcp')
else:
    print('Wrong selection!')