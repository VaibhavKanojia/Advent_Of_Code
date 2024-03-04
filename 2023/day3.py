'''
Author: Vaibhav Kanojia
Purpose: In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
Created: 06.12.2023
Updated: 07.02.2024
'''
import re
import math
input_stream=r'C:\Vaibhav\Learnings\Playground\Python\2023\day3_input.txt'

#it's a game of indicies, keep a watch of prev and next row for any symbol +/- of the start/end number index for diagonal checks. For line checks, it will be +/-1 
#. is not a symbol


if __name__ == "__main__":
    #Task 2: Optimum approach
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    regex_gear='\*' #ignores all digits and periods
    regex_number='\d+'
    total=0

    gears={}#To keep the gear coordinates only when adjacent to a gear

    for row,line in enumerate(input_lines):
        for symbol in re.finditer(regex_gear,line):
            column=symbol.start()
            gears[(row,column)]=[]#record gear enteries co-ordinates

    for row,line in enumerate(input_lines):
        for number in re.finditer(regex_number,line):#iterate over all numbers
             for r in range(row-1,row+2):#row-1 to row+2 since right side of any range is non inclusive. Hence, we need to add 1 more
                 for c in range(number.start()-1,number.end()+1): #Cant use Span since we need to start before the 1st column and after the last column
                     if (r,c) in gears: #Found a gear
                         gears[(r,c)].append(int(number.group()))

    total=0
    for gear,number in gears.items():
        if len(number)==2:
            total+=math.prod(number)

    print(total)
'''#Task 1 Optimum approach
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    regex_symbol='[^\d\.]' #ignores all digits and periods
    regex_number='\d+'
    total=0

    symbol_adjacent=set()#Faster lookup times, better than lists

    for row,line in enumerate(input_lines):
        for symbol in re.finditer(regex_symbol,line):
            column=symbol.start()
            symbol_adjacent|=set((r,c) for r in range(row-1,row+2) for c in range(column-1,column+2)) #row-1 to row+2 since right side of any range is non inclusive. Hence, we need to add 1 more. Once we find the r,c we can add the sets using union

    for row,line in enumerate(input_lines):
        for number in re.finditer(regex_number,line):
            if any((row,col) in symbol_adjacent for col in range(*number.span())):#unpacking the number tuple
                total+=int(number.group())

    print(total)
'''

'''#Task 2: Approach 1
    #Dissecting string by string
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    temp=[]
    digit_index_list=[]
    special_char_index_list=[]
    digit_matcher=r'\d'
    remove_index_list=[]
    temp_list=[]
    digit_list=[]
    number_length=0
    final_score=[]

    #Task 2 - A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.This time, you need to find the gear ratio of every gear and add them all

    #Find the number in stream and then search for adjacent * available
    for list_idx in range(0,len(input_lines)):
        temp=re.findall(r'(\d+)',input_lines[list_idx])
        if list_idx==1: #1st line, hence avoid -ve line indexing
            print()
        elif list_idx==len(input_lines):#last line, hence avoid out of bound indexing
             for element in temp:
                start_idx=input_lines[list_idx].index(element)
                if (re.match(r'\*',input_lines[list_idx][start_idx+len(element)]) or re.match(r'\*',input_lines[list_idx][start_idx-1])):
                     print(element)
        else:#in between lines
            for element in temp:
                start_idx=input_lines[list_idx].index(element)
                if re.match(r'\*',input_lines[list_idx][start_idx+len(element)]):#Numbers which have * adjacent to the right
                    print("right: ",element)
                elif re.match(r'\*',input_lines[list_idx][start_idx-1]):#Numbers which have * adjacent to the left
                    print("left: ",element)
'''

'''#Task 1: Approach 2
    #finding numbers and their indicies of all number combinations
    for list_iterator in range(0,len(input_lines)):
        temp=re.findall(r'(\d+)',input_lines[list_iterator])
        digit_list.append(temp)
        temp_list=[]
        start_index=0
        for inner_iterator in range(0,len(temp)):
            if len(temp[inner_iterator])==1  and inner_iterator!=0:#single digit, not at start, to avoid overlapping numbers
                start_index+=1
            elif len(temp[inner_iterator])==2  and inner_iterator!=0:#two digit, not at start, to avoid overlapping numbers
                start_index+=2
            start_index=input_lines[list_iterator].index(temp[inner_iterator],start_index)
            temp_list.append(start_index)
        digit_index_list.append(temp_list)
    print(digit_index_list[113])

    #finding special char location
    for element in input_lines:
        special_char_index_list.append([position for position, char in enumerate(element) if not (re.match(digit_matcher,char) or char=='.' or char=='\n')])

    #eval length of valid number and then scan whether if a special char lies in range
    for outer_iterator in range(0,len(input_lines)):
        for inner_iterator in range(0,len(digit_list[outer_iterator])):
            number_length=len(digit_list[outer_iterator][inner_iterator])
            if outer_iterator==0:#first line
                #print('1st line',digit_list[outer_iterator][inner_iterator])
                match number_length:
                    case 1:#single number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator]:
                            #print("1 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
                    case 2:#two digit number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator]:
                            #print("2 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
                    case 3:#three digit number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+3 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+3 in special_char_index_list[outer_iterator]:
                            #print("3 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
            elif outer_iterator==len(input_lines)-1:#last line
                #print("last line")
                match number_length:
                    case 1:#single number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator]:
                            #print("1 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
                    case 2:#two digit number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator]:
                            #print("2 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
                    case 3:#three digit number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+3 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+3 in special_char_index_list[outer_iterator]:
                            #print("3 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
            else:#inbetween lines
                match number_length:
                    case 1:#single number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator-1]:
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
                    case 2:#two digit number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator] or  digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator-1]:
                            #print("2 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
                    case 3:#three digit number
                        if digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]+3 in special_char_index_list[outer_iterator+1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator]+3 in special_char_index_list[outer_iterator] or digit_index_list[outer_iterator][inner_iterator] in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]-1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+1 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+2 in special_char_index_list[outer_iterator-1] or digit_index_list[outer_iterator][inner_iterator]+3 in special_char_index_list[outer_iterator-1]:
                            #print("3 digit:",digit_list[outer_iterator][inner_iterator])
                            final_score.append(int(digit_list[outer_iterator][inner_iterator]))
    #print(final_score)
    print(sum(final_score))
'''

'''##Task 1: Approach 1
    for element in input_lines:
        digit_index_list.append([position for position, char in enumerate(element) if re.match(digit_matcher,char)])
    #print(digit_index_list[0])
    for element in input_lines:
        special_char_index_list.append([position for position, char in enumerate(element) if not (re.match(digit_matcher,char) or char=='.' or char=='\n')])
    #print(special_char_index_list[0])

    for list_iterator in range(0,len(digit_index_list)):
        if list_iterator==0 :#1st row 
            for element_iterator in range(0,len(digit_index_list[list_iterator])):
                if (digit_index_list[list_iterator][element_iterator] in special_char_index_list[list_iterator+1]) or ((digit_index_list[list_iterator][element_iterator]+1) in special_char_index_list[list_iterator+1]) or ((digit_index_list[list_iterator][element_iterator]-1) in special_char_index_list[list_iterator+1]) or  (digit_index_list[list_iterator][element_iterator]+1 in special_char_index_list[list_iterator]) or (digit_index_list[list_iterator][element_iterator]-1 in special_char_index_list[list_iterator]):
                    continue
                else:
                    temp_list.append(digit_index_list[list_iterator][element_iterator])

        if list_iterator==len(digit_index_list)-1:#last row
            for element_iterator in range(0,len(digit_index_list[list_iterator])):
                if (digit_index_list[list_iterator][element_iterator] in special_char_index_list[list_iterator-1]) or (digit_index_list[list_iterator][element_iterator]+1 in special_char_index_list[list_iterator-1]) or ((digit_index_list[list_iterator][element_iterator]-1) in special_char_index_list[list_iterator-1]) or  (digit_index_list[list_iterator][element_iterator]+1 in special_char_index_list[list_iterator]) or (digit_index_list[list_iterator][element_iterator]-1 in special_char_index_list[list_iterator]):
                    continue
                else:
                    temp_list.append(digit_index_list[list_iterator][element_iterator])
        else:
            for element_iterator in range(0,len(digit_index_list[list_iterator])):
                if (digit_index_list[list_iterator][element_iterator] in special_char_index_list[list_iterator+1]) or (digit_index_list[list_iterator][element_iterator]+1 in special_char_index_list[list_iterator+1]) or ((digit_index_list[list_iterator][element_iterator]-1) in special_char_index_list[list_iterator+1]) or  (digit_index_list[list_iterator][element_iterator]+1 in special_char_index_list[list_iterator]) or (digit_index_list[list_iterator][element_iterator]-1 in special_char_index_list[list_iterator]) or (digit_index_list[list_iterator][element_iterator] in special_char_index_list[list_iterator-1]) or (digit_index_list[list_iterator][element_iterator]+1 in special_char_index_list[list_iterator-1]) or ((digit_index_list[list_iterator][element_iterator]-1) in special_char_index_list[list_iterator-1]):
                    continue
                else:
                    temp_list.append(digit_index_list[list_iterator][element_iterator])
        remove_index_list.append(temp_list)
        temp_list=[]

    for list_iterator in range(0,len(remove_index_list)):#remove unnecessary indicies 
            for element_iterator in range(0,len(remove_index_list[list_iterator])):
                if remove_index_list[list_iterator][element_iterator] in digit_index_list[list_iterator]:
                    digit_index_list[list_iterator].remove(remove_index_list[list_iterator][element_iterator])
    
    for list_iterator in range(0,len(digit_index_list)):#remove adjacent indicies
            for element_iterator in range(0,len(digit_index_list[list_iterator])):
                if element_iterator==len(digit_index_list[list_iterator]):
                    break
                if digit_index_list[list_iterator][element_iterator]+1 in digit_index_list[list_iterator]:
                    digit_index_list[list_iterator].remove(digit_index_list[list_iterator][element_iterator]+1)
                
                if digit_index_list[list_iterator][element_iterator]+2 in digit_index_list[list_iterator]:
                    digit_index_list[list_iterator].remove(digit_index_list[list_iterator][element_iterator]+2)

    for list_iterator in range(0,len(digit_index_list)):#fetch the numbers where we found symbols and add them
            temp=re.findall(r'(\d+)',input_lines[list_iterator])
            print(temp)
            print(digit_index_list[0])
            if temp:
                for element in temp:
                    print("index:",input_lines[0].index(element))
                    if input_lines[list_iterator].index(element) in digit_index_list[list_iterator]:
                        print("element at index:",element)
                        digit_list.append(int(element))
            print('------')

            for element_iterator in range(0,len(digit_index_list[list_iterator])):
                for iterator in range(0,len(input_lines[list_iterator])):
                if re.match(r'(\d+)',input_lines[list_iterator][iterator]):
                    iterate_inside=1
                    while re.search(r'(\d+)',input_lines[list_iterator][iterato+iterate_inside])!=None:
                        print(iterator+iterate_inside)
                        print(input_lines[list_iterator][iterator])
                        print("---")
                        iterate_inside+=1
                    print('----------------------')
    print(sum(digit_list))


#1st approach
    for element in input_lines:
        temp=list(element)
        if '\n' in temp:
            temp.remove('\n')
        preproc_list.append(temp)
    #print(preproc_list)
    for list in preproc_list:
        for iterator in range(0,len(list)):
            if (ord(list[iterator])>47 and ord(list[iterator])<58):
                if preproc_list.index(list)==0:
                    #1st list
                    if not ((ord(preproc_list[preproc_list.index(list)+1][iterator-1])>47 and ord(preproc_list[preproc_list.index(list)+1][iterator-1])<58) or (preproc_list[preproc_list.index(list)+1][iterator-1]== ".")) or not((ord(preproc_list[preproc_list.index(list)+1][iterator])>47 and ord(preproc_list[preproc_list.index(list)+1][iterator])<58) or (preproc_list[preproc_list.index(list)+1][iterator]== ".")) or not((ord(preproc_list[preproc_list.index(list)+1][iterator+1])>47 and ord(preproc_list[preproc_list.index(list)+1][iterator+1])<58) or (preproc_list[preproc_list.index(list)+1][iterator+1]== ".")) or not((ord(list[iterator-1])>47 and ord(list[iterator-1])<58) or list[iterator-1]=='.') or not((ord(list[iterator+1])>47 and ord(list[iterator+1])<58) or list[iterator+1]=='.'):
                        index_collector.append(iterator)
                if preproc_list.index(list)==len(preproc_list)-1:
                    #last list
                    if not ((ord(preproc_list[preproc_list.index(list)-1][iterator-1])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator-1])<58) or (preproc_list[preproc_list.index(list)-1][iterator-1]== ".")) or not((ord(preproc_list[preproc_list.index(list)-1][iterator])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator])<58) or (preproc_list[preproc_list.index(list)-1][iterator]== ".")) or not((ord(preproc_list[preproc_list.index(list)-1][iterator+1])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator+1])<58) or (preproc_list[preproc_list.index(list)-1][iterator+1]== ".")) or not((ord(list[iterator-1])>47 and ord(list[iterator-1])<58) or list[iterator-1]=='.') or not((ord(list[iterator+1])>47 and ord(list[iterator+1])<58) or list[iterator+1]=='.'):
                        index_collector.append(iterator)
                else:
                    #in between but last element number is failing
                    if iterator==0:
                        if not ((ord(preproc_list[preproc_list.index(list)+1][iterator])>47 and ord(preproc_list[preproc_list.index(list)+1][iterator])<58) or (preproc_list[preproc_list.index(list)+1][iterator]== ".")) or not((ord(preproc_list[preproc_list.index(list)+1][iterator+1])>47 and ord(preproc_list[preproc_list.index(list)+1][iterator+1])<58) or (preproc_list[preproc_list.index(list)+1][iterator+1]== ".")) or not((ord(preproc_list[preproc_list.index(list)-1][iterator])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator])<58) or (preproc_list[preproc_list.index(list)-1][iterator]== ".")) or not((ord(preproc_list[preproc_list.index(list)-1][iterator+1])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator+1])<58) or (preproc_list[preproc_list.index(list)-1][iterator+1]== ".")) or not((ord(list[iterator+1])>47 and ord(list[iterator+1])<58) or list[iterator+1]=='.'):
                            index_collector.append(iterator)
                    if iterator==len(list)-1:
                        if not ((ord(preproc_list[preproc_list.index(list)+1][iterator])>47 and ord(preproc_list[preproc_list.index(list)+1][iterator])<58) or (preproc_list[preproc_list.index(list)+1][iterator]== ".")) or not((ord(preproc_list[preproc_list.index(list)+1][iterator-1])>47 and ord(preproc_list[preproc_list.index(list)+1][iterator-1])<58) or (preproc_list[preproc_list.index(list)+1][iterator-1]== ".")) or not((ord(preproc_list[preproc_list.index(list)-1][iterator])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator])<58) or (preproc_list[preproc_list.index(list)-1][iterator]== ".")) or not((ord(preproc_list[preproc_list.index(list)-1][iterator-1])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator-1])<58) or (preproc_list[preproc_list.index(list)-1][iterator-1]== ".")) or not((ord(list[iterator-1])>47 and ord(list[iterator-1])<58) or list[iterator-1]=='.'):
                            index_collector.append(iterator)
                    else:
                        if not ((ord(preproc_list[preproc_list.index(list)+1][iterator-1])>47 and ord(preproc_list[preproc_list.    index(list)+1][iterator-1])<58) or (preproc_list[preproc_list.index(list)+1][iterator-1]== ".")) or not ((ord(preproc_list[preproc_list.index(list)+1][iterator])>47 and ord(preproc_list[preproc_list.index (list)+1][iterator])<58) or (preproc_list[preproc_list.index(list)+1][iterator]== ".")) or not((ord  (preproc_list[preproc_list.index(list)+1][iterator+1])>47 and ord(preproc_list[preproc_list.index(list)   +1][iterator+1])<58) or (preproc_list[preproc_list.index(list)+1][iterator+1]== ".")) or not((ord(list [iterator-1])>47 and ord(list[iterator-1])<58) or list[iterator-1]=='.') or not ((ord(preproc_list   [preproc_list.index(list)-1][iterator-1])>47 and ord(preproc_list[preproc_list.index(list)-1]  [iterator-1])<58) or (preproc_list[preproc_list.index(list)-1][iterator-1]== ".")) or not((ord    (preproc_list[preproc_list.index(list)-1][iterator])>47 and ord(preproc_list[preproc_list.index(list)-1]    [iterator])<58) or (preproc_list[preproc_list.index(list)-1][iterator]== ".")) or not((ord(preproc_list [preproc_list.index(list)-1][iterator+1])>47 and ord(preproc_list[preproc_list.index(list)-1][iterator   +1])<58) or (preproc_list[preproc_list.index(list)-1][iterator+1]== ".")) or not((ord(list[iterator-1])    >47 and ord(list[iterator-1])<58) or list[iterator-1]=='.') or not((ord(list[iterator+1])>47 and ord(list   [iterator+1])<58) or list[iterator+1]=='.'):
                            index_collector.append(iterator)
        index_collector.append('\n')
    print(index_collector)
'''
