#!/bin/python

def add_binary(a, b):
  tmp = bin(a + b)
  return tmp[2:]
  
def main():
  assert(add_binary(1, 1) == "10")
  assert(add_binary(51, 12) == "111111")
  print(add_binary(51, 12))
  

if __name__ == '__main__':
  main()
