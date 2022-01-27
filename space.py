import argparse

def show(file_path):
    given_file = open(file_path, 'r')
    count=0
    for line in given_file.readlines():
        count +=1
        if(line[0]=="\t"):
            print("Line{}: {}".format(count, line.strip()))
    given_file.close()


def fix(file_path):
    given_file = open(file_path, 'r')
    count=0
    print("Before Replacing")
    
    for line in given_file.readlines():
        count +=1
        print("Line{}: {}".format(count,line))
    given_file.close()
    
    given_file = open(file_path, 'r')
    print("After Replacing")
    count=0
    for line in given_file.readlines():
        count +=1
        if(line[0]=="\t"):
            line="  "+line.lstrip()
        print("Line{}: {}".format(count, line))
    given_file.close()


parser=argparse.ArgumentParser(description='Performs following file processing function')
parser.add_argument("--show", type=str, help='shows the indented lines with line number from the given file')
parser.add_argument("--fix", type=str, help='replaces the leading tabs with two spaces')
if parser.parse_args().show:
    show(parser.parse_args().show)
elif parser.parse_args().fix:
    fix(parser.parse_args().fix)
