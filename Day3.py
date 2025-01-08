'''
Author: Vaibhav Kanojia
Purpose: Day 3
Created: 18.12.2024
Updated: 19.12.2024
'''
import re

input_stream = r'C:\AdventOfCode\2024\3_input.txt'
pattern = r'mul\((\d+),(\d+)\)'

final_score = 0

if __name__ == "__main__":
    # Dissecting rows
    input_content = open(input_stream, 'r')
    input_lines = input_content.readlines()

    for list_idx in range(0, len(input_lines)):
        line = input_lines[list_idx]
        capturing = True
        matches = []
        
        while line:
            if re.search(r"don\'t\(\)", line):
                line = re.split(r"don\'t\(\)", line, 1)[1]
                capturing = False
            elif re.search(r"do\(\)", line):
                line = re.split(r"do\(\)", line, 1)[1]
                capturing = True
            elif capturing:
                match = re.search(pattern, line)
                if match:
                    matches.append(match.groups())
                    line = line[match.end():]
                else:
                    break
            else:
                break

        print(matches)
        for match in matches:
            final_score += int(match[0]) * int(match[1])

    print(final_score)
'''
import re

input_stream=r'C:\AdventOfCode\2024\3_input.txt'
mul_regex_pattern=r'mul\((\d+),(\d+)\)'
do_pattern='do()'
dont_pattern="don't()"
pattern = r'do\((?:[^d]|d(?!on\'t\(\)))*?mul\((\d+),(\d+)\)'

final_score=0

if __name__ == "__main__":
    #Dissecting rows
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()

    for list_idx in range(0,len(input_lines)):
        matches = re.findall(pattern, input_lines[list_idx])
        print(matches)
        """
        do_called=input_lines[list_idx].split(do_pattern)#fetch all the do() before finding don't()
        for element in do_called:
            relevant_mul=element.split(dont_pattern)
            print(relevant_mul[0])#Utilize only 0th since the remaining comes from don't()
            temp=re.findall(mul_regex_pattern,relevant_mul[0])#findall which matches mul()
            print(temp)
            for element in temp:
                final_score+=int(element[0])*int(element[1])#sum of mul()
        
        """
    print(final_score)
'''

'''
if __name__ == "__main__":
    #Dissecting rows
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()

    for list_idx in range(0,len(input_lines)):
        temp=re.findall(mul_regex_pattern,input_lines[list_idx])
        print(temp)
        for element in temp:
            final_score+=int(element[0])*int(element[1])
    print(final_score)
'''