import sys
import re

def main():
    n = int(raw_input().strip())
    B = raw_input().strip()
    
    assert 1 <= n <= 100
    for c in B:
        assert c in ["0", "1"]
    
    occ = substringIndices(B)
    if len(occ) <= 0:
        print("0")
        return
    
    else:
        count = 0
        l = []
        for i in occ:
            for j in range(3):
                new_B = beautify(B, i, j)
                l.append(len(substringIndices(new_B)))
            #print("choices : " + str(l))
            right = min(l) 
            #print("best choice : " + str(right))
            B = beautify(B, i, right)
            l = []
            count = count + 1

    print(count)

def substringIndices(s):
    occ = [m.start() for m in re.finditer("010", s)] 
    return occ
         
def beautify(s, pos, shift):
    count = 0
    new_s = ""

    for c in s:
        if count == pos + shift:
            new_s += "0"
        else:
            new_s += s[count] 
        count = count + 1

    return new_s

if __name__ == '__main__':
    main()
