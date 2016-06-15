# arbitrarily counts the line numbers of files in a directory
# not entirely accurate but I use this to get a general idea
# of the number of lines a program that I have written is
# composed of.


import sys
import os

def main():

    args = sys.argv
    
    if len(args) != 2:
        print("Invalid number of arguments")
        
    else:
        
        path = args[1]

        if sys.platform == "win32":
            fix_windows_directory(path)

        # get a list of all the files in the project
        file_list = []
        file_list = get_directory_files(path, file_list)

        # accumulate the values

        count = 0
        countws = 0
        for f in file_list:
            try:
                count = count + get_lines(f)
                countws = countws + get_lines_ws(f)
            except Exception as e:
                print("Couldn't read file: " + f)


        print("Lines: " + str(count))
        print("Lines (with whitespace): " + str(countws))


# returns the paths in a list of all of the files in a directory
# and each of its subsequent sub directory
def get_directory_files(project_path, file_list):
    ignore_list = ['.git' , '.gitattributes', '.gitignore']

    main_dir = os.listdir(project_path)

    for node in main_dir:
        if node not in ignore_list:
            if is_file(node):
                file_list.append(project_path + "/" +node)
            else:
                try:
                    file_list = get_directory_files(project_path + "/" + node, file_list)
                except Exception as e:
                    print("Couldnt read " + project_path + "/" + node)
 

    return file_list

# hack
def is_file(name):
    if '.' in name:
        return True
    else:
        return False

# L . M . A . O
def fix_windows_directory(project_path):
    if '\\' in project_path:
        project_path = project_path.replace('\\', '/')

    return project_path



# return the number of lines.
def get_lines(fname):

    try:
        infile = open(fname, 'r')
        lines = infile.readlines()
        
        ln = len(lines)

        for line in lines: # we dont want to count whitespace
            if line == '\n':
                ln -= 1

        return int(ln)

    except Exception as e:
        print("Couldnt read file:" + fname + "|" + str(e))

# returns the number of lines.  whitespace inclusive.
def get_lines_ws(fname):

    try:
        infile = open(fname, 'r')
        lines = infile.readlines()

        return len(lines)

    except Exception as e:
        print("Couldnt read file:" + fname + "|" + str(e))

if __name__ == '__main__':
    main()
