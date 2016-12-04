a = 0 
t = [1, 2, 3, 5, 8, 10, 15, 20, 40, 45, 47]

# init

i = 0
j = len(t) 
m = 0

# iter
while (i != j and t[m] != a) :
    m = j + (i - j) / 2 
    print t[m], m, i, j
    if t[m] >= a :
        j = m
    else :
        i = m + 1
print i, j
print i!=j 
