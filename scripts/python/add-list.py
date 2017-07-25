#!/usr/bin/env python
import sys
from subprocess import call

def main():
    script_name, fname = sys.argv

    contents = []
    with open(fname,'r') as f:
        contents = f.readlines()
    contents = [x.strip() for x in contents]

    full_command = ""
    for i in range(0,len(contents)):
        full_command += contents[i] + " "
               
    print("git add " + full_command)

if __name__ == '__main__':
    main()
        
