'''
Python for Beginners 20776.059
Steve Heally
07/27/17

Homework #5 - homework_5_solution_program.py

Write another program that will import the module you created above so that it
can be used by this new program.
'''
import time
import homework_5_solution_module as hw5sm

'''
Open two files reading all lines into two separate variables.  Loop over elements
of first variable and compare to second variable looking for differences. Collect
any differences in a list 'diff_list'. Print the number of differences. If there
are no differences, A sleep is used to allow time to manually edit one of the files
and cause a difference.
'''
def DiffTwoFiles(file1,file2):

    diff_list = []
    counter = 0
    print '\nPausing for any manual file edits...\n'
    time.sleep(15)
    file_1 = open(file1, 'r')
    file_2 = open(file2, 'r')
    
    list_1 = file_1.readlines()
    list_2 = file_2.readlines()
    
    for item in list_1:
        if item == item in list_2:
            continue
        else:
            diff_list.append(item)
            counter = counter + 1
            
    file_1.close()
    file_2.close()
    if counter == 0:
        print '\nNo file changes.\n'
    if counter != 0:
        print '\nOne or both of the files has been changed.\n'
    if counter == 1:
        print 'The file',file1,'has been compared to',file2,'and there is',counter, \
              'difference.\n'
    else:
        print 'The file',file1,'has been compared to',file2,'and there are',counter, \
              'differences.\n'

'''
Call each function separately from the module 'homework_5_solution_module' that
was imported.
'''
def Run():
    file_name = hw5sm.AskForFileName()
    file_list = hw5sm.ReadFileContents(file_name)
    head_list = hw5sm.BuildHeadList(file_list)
    atom_list = hw5sm.BuildAtomList(file_list)
    tail_list = hw5sm.BuildTailList(file_list)
    hw5sm.WriteNewFile(head_list,atom_list,tail_list)
    DiffTwoFiles(file_name,'/Users/stvo/Desktop/Python/Lab9_10/output.txt')
    
Run()
