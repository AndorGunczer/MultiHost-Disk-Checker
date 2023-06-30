import sys
import subprocess
import parser

# Read All the Hosts from "hostFile" file


def getHostList(hostFile):
    f = open(hostFile, "r")

    hostList = f.read().split("\n")
    f.close
    return hostList


# Get a 3D Array in the following format diskInfo[host][partition][data] => Data is used for analytics
# The Data is ordered as follows: FileSystem / Size / Used / Avail / Use% / Mounted On

def obtainHostDiskInfo(hostFile):
    diskInfo = []
    hostList = getHostList(hostFile)
    i = 0
    k = 0
    
    while hostList[i] != "":
        if (parser.hostSyntaxCheck(hostList[i])):
            jArray = []
            proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
            output = proc.stdout.read()
            tmp = output.decode().split()

            del tmp[:7]
            kArray = []
            while k < len(tmp):
                #print(tmp[k])
                kArray.append(tmp[k])
                k += 1
                if k % 6 == 0:
                    jArray.append(kArray)
                    kArray = []
            diskInfo.append(jArray)
            k = 0
        else:
            print("Very Bad")
        i += 1

    return diskInfo


def main():
    diskInfo = obtainHostDiskInfo(sys.argv[1])
    print(type(diskInfo))
    print(diskInfo)
    print("\n\n\n\n\n")
    for i in diskInfo:
        print(i)


main()

