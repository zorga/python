#!/bin/python

def my_parse_int(string):
  string = string.strip()
  result = "NaN"
  if string.isdigit():
    result = int(string)
  return result
    

def main():
  assert (my_parse_int("1") == 1) 
  assert (my_parse_int("  1 ") == 1)
  assert (my_parse_int("08") == 8)
  assert (my_parse_int("5 friends") == "NaN")
  
if __name__ == '__main__':
  main()
