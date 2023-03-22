import socket, termcolor

def scan(target, ports):
	print(termcolor.colored((f'\nStarting Scan For {target}\n'), 'cyan'))
	for port in range(1, ports):
		scan_port(target,port)

def scan_port(ip_address, port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.1)
		result = sock.connect_ex((ip_address, port))
		if result == 0:
			service = socket.getservbyport(port)
			print('[+] Port Opened:', str(port))
			print(termcolor.colored((f'[+] Service: {service}'), 'magenta'))
			try:
				sock.send(b'Hello\r\n')
				version = sock.recv(1024)
				print(termcolor.colored((f'[+] Version: {version.decode().strip()}'), 'red'))
			except:
				pass
		sock.close()
	except:
		pass

targets = input('[*] Enter Target or Targets To Scan: ')
ports = int(input('[*] Enter number of ports to be scanned: '))
if ',' in targets:
	print(termcolor.colored(('[*] Scanning Multiple Targets'), 'blue'))
	for ip in targets.split(','):
		scan(ip.strip(' '), ports)
else:
	scan(targets,ports)

