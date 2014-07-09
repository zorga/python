import sys
import re

def findmail():
    match = re.search(r'[\w.-]+@[\w.-]+', sys.argv[1])
    if match:
        print match.group()
    else:
        print 'address not found !'

def main():
    findmail()

if __name__ == '__main__':
    main()
