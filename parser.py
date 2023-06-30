import sys
import re
import subprocess

def checkOperatingSystem():
    proc = subprocess.Popen(["grep", "^NAME", "/etc/os-release"], stdout=subprocess.PIPE)
    output = proc.stdout.read()

    if "Debian" in output.decode():
        print("Debian")
    elif "RHEL" in output.decode():
        print("RHEL")

def hostSyntaxCheck(host):
    hostName = host.split("@")

    if len(hostName) == 2 and hostName[1] != "":
        return True
    else:
        return False

def parser():
    if len(sys.argv) == 2:
        print("Correct Argument Number")
    else:
        print("Incorrect Argument Number")

    hostSyntaxCheck(sys.argv[1])
    checkOperatingSystem()
    # Matching regular expression of username with given OS

parser()
