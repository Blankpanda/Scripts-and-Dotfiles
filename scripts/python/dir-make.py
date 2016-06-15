# targets a file that has a listing for directories and creates them
# takes only a text file as a target for now
# arguments:
#           python dir-make.py file-list.txt
import os
import sys

def main():
    args = sys.argv

    if len(args) != 2:
        print('Invalid arguments\n\rpython dir-make.py file-list.txt')
        sys.exit(0)

    file_name = args[1]
    f = open(file_name,'r')
    file_content = f.read()
    lines = file_content.split('\n')

    # strip new line at the end if the test file has it
    if '' in lines or '\n'in lines:
        lines = lines[:len(lines)-1]

    for name in lines:
        os.makedirs(name)

    
    
if __name__ == '__main__':
    main()
