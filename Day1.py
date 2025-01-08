'''
Author: Vaibhav Kanojia
Purpose: Day 1
Created: 11.12.2024
Updated: 
'''
import re
input_stream=r'C:\AdventOfCode\2024\1_input.txt'
final_score=0


"""Part 1
if __name__ == "__main__":
    #Dissecting rows
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()

    left_row=[]
    right_row=[]
    diff_arr=[]

    for element in input_lines:
        left_row.append(int(element.split('   ')[0]))
        right_row.append(int(element.split('   ')[1].split('\n')[0]))

    #ascending sort
    left_row.sort()
    right_row.sort()

    print("-------Left Row----------")
    print(left_row)
    print("-------Right Row----------")
    print(right_row)

    for iterator in range(len(left_row)):
        diff_arr.append(abs(left_row[iterator]-right_row[iterator]))
    print(diff_arr)
    
    final_score=sum(diff_arr)

    print(final_score)
"""

#Part 2
if __name__ == "__main__":
    #Dissecting rows
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()

    left_row=[]
    right_row=[]
    simm_arr=[]
    mul_fac=0

    for element in input_lines:
        left_row.append(int(element.split('   ')[0]))
        right_row.append(int(element.split('   ')[1].split('\n')[0]))
    
    for element in left_row:
        for temp_element in right_row:
            if element == temp_element:
                mul_fac+=1
                continue
        print(mul_fac)
        simm_arr.append(element*mul_fac)
        mul_fac=0

    print(simm_arr)
    final_score=sum(simm_arr)

    print(final_score)