'''
Author: Vaibhav Kanojia
Purpose: Day 2
Created: 12.12.2024
Updated: 13.12.2024
'''
input_stream=r'C:\AdventOfCode\2024\2_input.txt'

safe_range=[1,2,3]

def asc_eval(sample_element,already_attempted_flag):
    is_not_safe=0
    for iterator in range(len(sample_element)-1):
        check_var=int(sample_element[iterator+1])-int(sample_element[iterator])
        if not (check_var in safe_range) and already_attempted_flag==0:
            print("not safe:",check_var," try one more time!")
            if ((iterator+1) == len(sample_element)-1): # if we reach 2nd last element, then
                is_not_safe=0#since dropping last element at the list will make report safe
                already_attempted_flag=1
                print("safe after dropping:",sample_element[iterator+1],":already:",already_attempted_flag)
            elif int(sample_element[iterator+2])-int(sample_element[iterator]) in safe_range:
                #Trying with next to next elem
                is_not_safe=0
                already_attempted_flag=1
                print("safe after dropping:",sample_element[iterator+1],":already:",already_attempted_flag)
            else:
                print("fail to recover")
                is_not_safe=1
                break
        elif not (check_var in safe_range) and already_attempted_flag==1:
            print("fail to recover")
            is_not_safe=1
            break

    return is_not_safe

def desc_eval(sample_element,already_attempted_flag):
    is_not_safe=0
    for iterator in range(len(sample_element)-1):
        check_var=int(sample_element[iterator+1])-int(sample_element[iterator])
        if not (-1*check_var in safe_range) and already_attempted_flag==0:#-1* to remove negative for valid desc cases
            print("not safe:",check_var," try one more time!")
            if ((iterator+1) == len(sample_element)-1): # if we reach 2nd last element, then
                is_not_safe=0#since dropping last element at the list will make report safe
                print("safe after dropping:",sample_element[iterator+1])
                already_attempted_flag=1
            elif -1*(int(sample_element[iterator+2])-int(sample_element[iterator])) in safe_range:
                #Trying with next to next elem
                is_not_safe=0
                print("safe after dropping:",sample_element[iterator+1])
                already_attempted_flag=1
            else:
                print("fail to recover")
                is_not_safe=1
                break
        elif not (check_var in safe_range) and already_attempted_flag==1:
            print("fail to recover")
            is_not_safe=1
            break
    return is_not_safe

def check(sample_element):#check fn to decide whether asc or desc
    already_attempted_flag=0#to avoid redropping for list where dupl values were at start of list
    is_not_safe=0
    check_var=int(sample_element[1])-int(sample_element[0])
    if check_var>0: # ascending order to be checked
        print("asc")
        is_not_safe=asc_eval(sample_element,already_attempted_flag)
    elif check_var<0:#descending order
        print("desc")
        is_not_safe=desc_eval(sample_element,already_attempted_flag)
    else: #not asc/desc order
        print("not safe at 1st position",check_var," try one more time!")
        already_attempted_flag=1
        sample_element.pop(1)
        print("sample list after popping:",sample_element)
        check_var=int(sample_element[1])-int(sample_element[0])
        print("new check_var:",check_var)
        if check_var>0 and check_var in safe_range: # ascending order to be checked
            print("asc after dropping 2nd ele")
            is_not_safe=asc_eval(sample_element,already_attempted_flag)
        elif check_var<0 and -1*check_var in safe_range:#descending order
            print("desc after dropping 2nd ele")
            is_not_safe=desc_eval(sample_element,already_attempted_flag)
        else:
            print("fail to recover")
            is_not_safe=1

    return is_not_safe

if __name__ == "__main__":
    #Dissecting rows
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    samples=[]
    is_not_safe=0
    iterator =0
    
    for element in input_lines:
        samples.append(element.split('\n')[0].split(' '))
        is_not_safe+=check(samples[iterator])
        print("sample:",samples[iterator],"is_not_safe:",is_not_safe)
        print('==============================')
        iterator+=1
        
    print("safe reports:",len(input_lines)-is_not_safe)


"""

def check(sample_element):
    safe_range=[1,2,3]
    check_var=int(sample_element[1])-int(sample_element[0])
    is_not_safe=0
    if check_var>0: # ascending order to be checked
        print("asc")
        for iterator in range(len(sample_element)-1):
            check_var=int(sample_element[iterator+1])-int(sample_element[iterator])
            if not (check_var in safe_range):
                print("not safe:",check_var)
                is_not_safe=1
                break
"""