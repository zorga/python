import sys
import codecs

def main():
    f = codecs.open(sys.argv[1], 'r', 'utf-8')
    for line in f:
        print line
    f.close()

if __name__ == '__main__':
    main()
