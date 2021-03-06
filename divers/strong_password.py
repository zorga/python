#!/usr/bin/python2.7
"""
A python script to generate strong passwords
Generate a random strong string of size 300
Then select a random part of that string of user specified size, as password
"""

import random
import argparse

special_chars = [">", "<", "#", "(", ")", "-", "_", "|", "&", "@", "$", "]", "[", "%"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="Desired password size (between 4 and 20)")
    args = parser.parse_args()

    if not args.size:
        psize = 12
        print 'No size submitted : using ' + str(psize) + ' as default.'

    else:
        psize = int(args.size)

    assert 4 <= psize <= 20
    passwd = ""

    for i in range(100):
        c = random.randint(97, 122)
        cUpper = random.randint(65, 90)
        passwd += chr(c)
        passwd += special_chars[random.randint(0, len(special_chars) - 1)]
        passwd += chr(cUpper)

    rand_i = random.randint(0, len(passwd) - psize)
    rand_j = rand_i + psize
    passwd = passwd[rand_i:rand_j]
    # shuffle password characters
    passwd = ''.join(random.sample(passwd, len(passwd)))

    print passwd

if __name__ == "__main__":
    main()
