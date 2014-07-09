import sys
import codecs

def lempelziv (s, table):
    i = 256  #ASCII de 256 car comme dico de base 
    word = ''
    for char in s:
        if word + char in table:
            word = word + char
        else:
            table[word + char] = i 
            word = char
            i+=1

def main():
    print 49*'-'
    print '>>> Welcome in my Lempelziv implementation !! <<<'
    print 49*'-'
    table = {}
    f = codecs.open(sys.argv[1], 'r', 'utf-8')
    lempelziv(f.read(), table)
    results = table.items()
    sortedResults = sorted(results, key=lambda results: results[-1])
    for k, v in sortedResults:
        print k, '>', v

    sys.exit(0)

if __name__ == '__main__':
    main()

