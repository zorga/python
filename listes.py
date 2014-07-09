import sys

fibo = [1, 2, 3, 4]
b = fibo # make b point to the list pointed by fibo
i=0
while i<len(fibo):
    fibo[i]=fibo[i]+1
    i+=1

for var in b:
    print var
# fibo and b point to the same list so, if I modify fibo, b will me modified too, of course
