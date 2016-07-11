# counts the number of files in a root directory and creates a 'pretty' list of the results
import os
import sys

def main():
    args = sys.argv

    if len(args) != 2:
        print("Invalid number of arguments. python filenum.py <rootDirectory>")
        sys.exit(0)
        
    path = args[1]
    
    if sys.platform == 'win32':
        fix_windows_directory(path)

    files = []
    directories = {}
    files, directories = get_directory_files(path)

    total_file_count = len(files)

    directories_numbers = {}

    for dir in directories:
        directories_numbers[dir] = len(directories[dir])

    for dir in directories_numbers:
        print(dir + " : " + str(directories_numbers[dir]))
        

# returns the paths in a list of all of the files in a directory
# and each of its subsequent sub directory
def get_directory_files(project_path, file_list=[], dir_dict={}):
    ignore_list = ['.git' , '.gitattributes', '.gitignore']

    main_dir = os.listdir(project_path)

    for node in main_dir:
        if node not in ignore_list:
            if is_file(node):
                file_list.append(project_path + "\\" +node)
                dir_dict[project_path] = file_list
            else:
                try:
                    file_list , dir_dict = get_directory_files(project_path + "\\" + node, [], dir_dict)
                except Exception as e:
                    print("Couldnt read " + project_path + "/" + node)
 

    return file_list, dir_dict


def fix_windows_directory(project_path):
    if '\\' in project_path:
        project_path = project_path.replace('\\', '/')

    return project_path

def is_file(file):
    if '.' in file:
        return True
    else:
        return False
        


if __name__ == '__main__':
    main()
