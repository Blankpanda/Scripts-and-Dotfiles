#!/usr/bin/env python
import sys

from datetime import datetime
#TODO: output what the script needs as args
def main():
    args = sys.argv

    if len(args) > 3:
        print("Incorrect arguments")
        sys.exit(0)
        
    pattern = "%H:%M:%S.%f"
    d1 = datetime.strptime(args[1],pattern)
    d2 = datetime.strptime(args[2], pattern)

    print(d1 - d2)

if __name__ == '__main__':
    main()
    
