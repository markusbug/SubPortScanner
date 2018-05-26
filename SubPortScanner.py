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
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def check(m,portnum):
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
print "SubPortScanner.py\nAuthor: MarkusHaas2002(Github) | Markusbug(Twitter)"
try:
    domain = sys.argv[1]
    port = sys.argv[2]
except:
    print("No Parameter Provided.\nUse: python SMTPVuln.py [Domain] [Port]")
    exit()
if domain is None:
    print("No Parameter Provided.")
    exit()
if port is None:
    print("No Parameter Provided.")
    exit()
os.system("python Sublist3r/sublist3r.py -d "+ domain +" -o Sublist3r/sublistresult/m.txt")
with open("Sublist3r/sublistresult/m.txt") as f:
    content = f.read().splitlines()
i = 0
if port is "smtp":
    matching = [s for s in content if "mail" in s]
    print bcolors.OKBLUE+"[+] Port 25 selected."
    while i < len(matching):
        check(matching[i],"25")
        i += 1
    sock.close()
    exit()
else:
    while i < len(content):
        check(content[i],port)
        i += 1
    sock.close()
    exit()
