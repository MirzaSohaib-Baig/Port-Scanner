import nmap
import termcolor

def scan(target, ports):
    print(termcolor.colored((f'\nStarting Scan For {target}\n'), 'cyan'))
    nm = nmap.PortScanner()
    nm.scan(target, f'1-{ports}')
    for host in nm.all_hosts():
        print(termcolor.colored(f'State : {nm[host].state()}', 'green'))
        for proto in nm[host].all_protocols():
            print(termcolor.colored(f'Protocol : {proto}', 'yellow'))
            lport = nm[host][proto].keys()
            for port in lport:
                print(termcolor.colored(f'Port : {port}\nState : {nm[host][proto][port]["state"]}', 'blue'))
                print(termcolor.colored(f'Service : {nm[host][proto][port]["name"]}', 'magenta'))
                print(termcolor.colored(f'Version : {nm[host][proto][port]["version"]}\n', 'red'))

target = input('[*] Enter Target or Targets To Scan: ')
ports = int(input('[*] Enter number of ports to be scanned: '))
if ',' in target:
    print(termcolor.colored(('[*] Scanning Multiple Targets'), 'blue'))
    for ip in target.split(','):
        scan(ip.strip(' '), ports)
else:
    scan(target, ports)
