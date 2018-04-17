'''
Python for Beginners 20776.059
Steve Heally
07/27/17

Homework #5 - homework_5_solution_module.py

This module will perform file parsing and writing on an exisiting file named '1JKB.pdb'
located in the same directory as this module.  The file will be split into three sections,
then the sections output to a new file in the same order.
'''

def AskForFileName():
    ''' Ask user for the name of an existing file named '1JKB.pdb' located in same directory
as this module. This is the file that will be parsed. '''
    
    while True:
        user_input = raw_input('\nEnter the name of the input file:')
        try:
            file = open(user_input)
        except IOError:
            print 'File not found!'
        else:
            file.close()
            return user_input

def ReadFileContents(file_name):
    ''' Read the contents of the file into memory as a variable. '''
    
    file = open(file_name, 'r')
    all_file_contents = file.readlines()
    file.close()
    
    return all_file_contents

def BuildHeadList(all_file_contents):
    ''' Search the file for lines that are *above* the *first* line that starts with 'ATOM'
in the file and save them into memory as a list called 'head_list'.  The '\\n' characters
will be removed from each line as they are saved. '''
    
    head_list = []
    
    for line in all_file_contents:
        if line.startswith('ATOM'):
            continue
        else:
            head_list.append(line.strip('\n'))
            
    return head_list[0:290]

def BuildAtomList(all_file_contents):
    ''' Search the file for lines that start with 'ATOM', representing the middle of the file,
and save them into memory as a list called 'atom_list'.  The '\\n' characters will be removed
from each line as they are saved. '''
    
    atom_list = []

    for line in all_file_contents:
        if line.startswith('ATOM'):
            atom_list.append(line.strip('\n'))

    return atom_list

def BuildTailList(all_file_contents):
    ''' Search the file for lines that are *below* the *last* line that starts with 'ATOM' in
the file and save them into memory as a list called 'tail_list'.  The '\\n' characters
will be removed from each line as they are saved. '''
    
    tail_list = []

    for line in all_file_contents:
        if line.startswith('ATOM'):
            continue
        else:
            tail_list.append(line.strip('\n'))

    return tail_list[290:]

def WriteNewFile(list1,list2,list3):
    ''' Output the three lists extracted from the file to a new file in the same order as the
original file creating a duplicate copy named 'output.txt' in the same directory as
this module. '''
    
    new_list = list1 + list2 + list3
    new_file = open('output.txt', 'w')
    for item in new_list:
        new_file.write(item + '\n')
    new_file.close()
    print '\nFile has been created, or modified if already exists.\n'

def Run():
    ''' The Run() Function will run all functions within this module. '''
    
    file_name = AskForFileName()
    file_list = ReadFileContents(file_name)
    head_list = BuildHeadList(file_list)
    atom_list = BuildAtomList(file_list)
    tail_list = BuildTailList(file_list)
    WriteNewFile(head_list,atom_list,tail_list)

''' Make this file a module '''
if __name__ == '__main__':
    Run()


    


