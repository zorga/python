#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

# function used as key to sort the dico in alphabetical order
def getValue(dicoEntry):
  return dicoEntry[0]

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename)
  matchYear = re.search('\d+', filename)
  if matchYear:
    year = matchYear.group()
  lines = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f.read())
  dico = {}
  for line in lines:
      dico[line[1]] = line[0]
      dico[line[2]] = line[0]
  sorted_names = sorted(dico.items(), key = getValue)
  sorted_names.insert(0, year)
  return sorted_names

def display_names(names):
    print names[0]
    for entry in names[1:]:
        print entry[0], entry[1]

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  for filename in args:
    #for each file we extract the names-rank list : l
    l = extract_names(filename)
    if summary == True:
        f = open('summaryfile', 'a')
        #we first write the year which is at the indice 0 in the list
        f.write(l[0])
        f.write('\n')
        #then we write all the entry of the list, beginning at the indice 1 because 0 is the year
        for entry in l[1:]:
            f.write(entry[0])
            f.write(' ')
            f.write(entry[1])
            f.write('\n')
        #don't forget to close the file once we have finished the writing operation
        f.close()
    else:
        display_names(l)
      
      

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
