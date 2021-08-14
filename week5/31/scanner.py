import sys, socket

#list of many common ports
PORT_LIST = [20,21,22,23,25,53,67,68,80,88,110,111,135,137,138,139,143,161,162,443,445,993,995,1433,1434,1723,3306,3389,5900,8080]

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid syntax... expecting \'python3 scanner.py <ip>\'')

open_list = []

try:
    for port in PORT_LIST:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.005)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'connected to {target} on port {port}')
            open_list.append(port)
        s.close()
    print(open_list)

except KeyboardInterrupt:
    print('\nExiting Program')
    print(open_list)
    sys.exit()
    
except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit()

except socket.error():
    print('Could not connect to server')
    sys.exit()
