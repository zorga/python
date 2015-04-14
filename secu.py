import string
import sys

def generatePasswdList():
    mdp = "QNKruN"
    charList = "abcdefghijklmnopqrstuvwxyz"
    slen = len(charList)
    result = []
    for i in range(0, slen):
        for d in range(0, 10):
            concat = charList[i] + str(d)
            result.append(concat)
    return result


def main():
    passwdList = generatePasswdList()

    sys.exit(0)

if __name__ == '__main__':
    main()
