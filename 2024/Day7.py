'''
Author: Vaibhav Kanojia
Purpose: Day 7
Created: 27.12.2024
Updated: 03.01.2025
'''
import re

input_stream=r'C:\AdventOfCode\2024\7_test_input.txt'

final_score = 0


def tree_evaluator(test_stream):
    isFound=False
    index=1
    result=0
    while index<len(test_stream):
        if (test_stream[index]*test_stream[index+1]) <=test_stream[0]: #Mul operator
            isFound=True
            result+=test_stream[index]*test_stream[index+1]
        elif (test_stream[index]+test_stream[index+1]) <=test_stream[0]: #Add operator
            result+=test_stream[index]+test_stream[index+1]
            isFound=True
        else: 
            isFound=False
        index+=1
    
        if isFound==True:
            print("Match found")
            print(result)
    return isFound

if __name__ == "__main__":
    # Dissecting rows
    input_content = open(input_stream, 'r')
    input_lines = input_content.readlines()

#backtracking algo -- find all perm/comb and then eliminate tree where result > expected
    for list_idx in range(0, len(input_lines)):
        print('-----------------------------')
        line = input_lines[list_idx]
        test_stream=re.findall(r'(\d+)', line)
        test_stream = [int(item) for item in test_stream]
        temp=test_stream[0]
        print("Line:",list_idx+1," with val:",temp)
        isFound=tree_evaluator(test_stream)
        if isFound:
            final_score+=test_stream[0]

print(final_score)
"""
for list_idx in range(0, len(input_lines)):
    print('-----------------------------')
    line = input_lines[list_idx]
    test_stream=re.findall(r'(\d+)', line)
    test_stream = [int(item) for item in test_stream]
    temp=test_stream[0]
    print("Line:",list_idx+1," with val:",temp)
    for stream_idx in range(len(test_stream)-1,0,-1):#reverse iterate to
        if temp%test_stream[stream_idx]==0:#find out whether last elem is mul or add operable
            temp=temp/test_stream[stream_idx]#divide since Mul operable
            print("Div with",test_stream[stream_idx]," to get:",temp)
            if temp==1.0 and stream_idx==1:#reached final element which satisfies the operations
                print("found match")
                final_score+=test_stream[0]
        else:#subtract if add operable
            temp=temp-test_stream[stream_idx]
            print("Sub with",test_stream[stream_idx],"to get:",temp)
"""
"""
    for list_idx in range(0, len(input_lines)):
        print('-----------------------------')
        line = input_lines[list_idx]
        test_stream=re.findall(r'(\d+)', line)
        print("Line:",list_idx+1)
        
        #Mul ALL test
        test_val=float(test_stream[1]) #init the test val before every next eval
        for stream_idx in range(2,len(test_stream)):
            test_val=test_val*float(test_stream[stream_idx])
        if int(test_val)==int(test_stream[0]):
            print("Mul ALL test success")
            final_score+=test_val
            continue

        #Add ALL test
        test_val=float(test_stream[1])
        for stream_idx in range(2,len(test_stream)):
            test_val=test_val+float(test_stream[stream_idx])
        if int(test_val)==int(test_stream[0]):
            print("Add ALL test success")
            final_score+=test_val
            continue

        #MulAdd test
        operator_toggle=False
        test_val=float(test_stream[1])
        for stream_idx in range(2,len(test_stream)):
            if operator_toggle==False:
                test_val=test_val*float(test_stream[stream_idx])
                operator_toggle=True
            else:
                test_val=test_val+float(test_stream[stream_idx])
                operator_toggle=False
        if int(test_val)==int(test_stream[0]):
            print("MulAdd test success")
            final_score+=test_val
            continue

        #AddMul test
        operator_toggle=False
        test_val=float(test_stream[1])
        for stream_idx in range(2,len(test_stream)):
            if operator_toggle==False:
                test_val=test_val+float(test_stream[stream_idx])
                operator_toggle=True
            else:
                test_val=test_val*float(test_stream[stream_idx])
                operator_toggle=False
        if int(test_val)==int(test_stream[0]):
            print("AddMul test success")
            final_score+=test_val
            continue

    print(final_score)
"""