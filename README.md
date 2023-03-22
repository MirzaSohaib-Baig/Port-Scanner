#Port Scanner
This repository contains two Python scripts for port scanning, one using the socket library and the other using the nmap library.

##Socket Library Port Scanner
The Socket Library Port Scanner is a Python script that scans a range of ports on a given host using the socket library. The script prompts the user to input the target host's IP address, as well as the starting and ending port numbers to scan. It then iterates over the range of port numbers, creating a new socket object for each port and attempting to connect to it. If the connection is successful, the script prints "Port {port} is open".

To run the script, navigate to the directory containing the script and enter the following command in your terminal:

Copy code
python socket_port_scanner.py
Nmap Library Port Scanner
The Nmap Library Port Scanner is a Python script that scans a range of ports on a given host using the nmap library. The script prompts the user to input the target host's IP address, as well as the starting and ending port numbers to scan. It then uses the nmap library to scan the target host for open ports and prints the results to the console.

To run the script, navigate to the directory containing the script and enter the following command in your terminal:

Copy code
python nmap_port_scanner.py
Requirements
Both scripts require Python 3.x and the following Python libraries:

For the Socket Library Port Scanner:

socket
For the Nmap Library Port Scanner:

nmap
You can install the required libraries using pip:

perl
Copy code
pip install socket nmap
Disclaimer
These scripts are for educational purposes only and should not be used for any malicious activities. The author is not responsible for any harm caused by the use of these scripts. Use them at your own risk.
