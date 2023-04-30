import sys
import socket 
from datetime import datetime

#define our target 

if len (sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #transalte hostname to IPv4
else:
    print("invalid amount of arguments.")
    print("syntax: python3 scanner.py <ip>")

#add a pretty banner 
print("_" * 50)
print("scanning target: "+target)
print("time started: "+str(datetime.now()))
print("_" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"port {port} is open")

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved")
    sys.exit()
except socket.error:
    print("could n ot connect to server")
    sys.exit()
