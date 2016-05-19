import os
import sys

def main():
    if len(sys.argv) > 3:
        print("Incorrect number of arguments")
        sys.exit(1)
    
    directory = sys.argv[1]
    custom_name = ""
    if len(sys.argv) == 2:
        custom_name = "items"
    else:
        custom_name = sys.argv[2]
    
    items = os.listdir(directory)

    if len(items) == 1:
        custom_name = custom_name[:-1]
    
    print("{0} has {1} {2}.".format(directory, len(items),custom_name))
    

if __name__ == '__main__':
    main()
