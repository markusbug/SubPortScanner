import os
import socket
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def check(m,portnum):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        ipadd = socket.gethostbyname(m)
    except:
        print bcolors.FAIL+"DNS Resolving failed on: "+m+""+bcolors.ENDC
        return
    result = sock.connect_ex((ipadd, int(portnum)))
    if result == 0:
        print bcolors.OKGREEN+"[+] Got one!, "+m+";"+ipadd+""+bcolors.ENDC
    else:
        print bcolors.WARNING+"Port is not open on: "+m+""+bcolors.ENDC
    sock.close()
print "SubPortScanner.py\nAuthor: MarkusHaas2002(Github) | Markusbug(Twitter)"
try:
    domain = sys.argv[1]
    port = sys.argv[2]
except:
    print("No Parameter Provided.\nUse: python SubPortScanner.py [Domain] [Port]")
    exit()
if domain is None:
    print("No Parameter Provided.")
    exit()
if port is None:
    print("No Parameter Provided.")
    exit()
os.system("sublist3r -d "+ domain +" -o "+domain+".txt")
with open(domain+".txt") as f:
    content = f.read().splitlines()
i = 0
while i < len(content):
        check(content[i],port)
        i += 1
exit()
