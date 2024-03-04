'''
Author: Vaibhav Kanojia
Purpose: The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number
Created: 02.12.2023
Updated: 05.12.2023
'''
import re
input_stream=r'C:\AdventOfCode\2023\day1_input.txt'
final_score=0

'''
#Part 1
if __name__ == "__main__":
    #Dissecting string by string
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    two_digit_list=[]
    for line in input_lines:
        #Skip if no digits present
        if line.isalpha()==True:
            print("Line doesnt have digits",line)
            continue
        else:
        #Scan for 1st and last digit to generate a two digit number representation
            number_list_from_line=[]
            int_version_of_number_list_from_line=[]
            for character in line:
                if ord(character)>47 and ord(character)<58:
                    number_list_from_line.append(character)
            int_version_of_number_list_from_line = [eval(i) for i in number_list_from_line]
            if len(number_list_from_line)>1:
                two_digit_list.append(int_version_of_number_list_from_line[0]*10+int_version_of_number_list_from_line[-1])
            else:#If single digit then use the same to make a 2 digit number
                two_digit_list.append(int_version_of_number_list_from_line[0]*10+int_version_of_number_list_from_line[0])
    final_score=sum(two_digit_list)
    print(final_score)
'''

'''
if __name__ == "__main__":
    #Dissecting string by string
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    two_digit_list=[]
    number_in_word_list=['one','two','three','four','five','six','seven','eight','nine']
    number_list=['1','2','3','4','5','6','7','8','9']
    temp_list=[]
    for line in input_lines:
        temp=line
        result=""
        for index in range(0,len(number_list)):
            result=re.sub(number_in_word_list[index],number_list[index],temp)
            temp=result
            #print(result)
        temp_list.append(result)
        #Skip if no digits present
        if result.isalpha()==True:
            print("Line doesnt have digits",result)
            continue
        else:
        #Scan for 1st and last digit to generate a two digit number representation
            number_list_from_line=[]
            int_version_of_number_list_from_line=[]
            for character in result:
                if ord(character)>47 and ord(character)<58:
                    number_list_from_line.append(character)
            int_version_of_number_list_from_line = [eval(i) for i in number_list_from_line]
            if len(number_list_from_line)>1:
                two_digit_list.append(int_version_of_number_list_from_line[0]*10+int_version_of_number_list_from_line[-1])
            else:#If single digit then use the same to make a 2 digit number
                two_digit_list.append(int_version_of_number_list_from_line[0]*10+int_version_of_number_list_from_line[0])
    print(two_digit_list)
    print(len(two_digit_list))
    final_score=sum(two_digit_list)
    print(final_score)
    f = open("myfile.txt", "w")
    for element in temp_list:
        f.write(element)
    f.close()
'''

def word_conv(element):
    for word in number_in_word_list:
        if element==word:
            element=str(int(number_in_word_list.index(word))+1)
    return element

if __name__ == "__main__":
    #Dissecting string by string
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    two_digit_list=[]
    number_in_word_list=['one','two','three','four','five','six','seven','eight','nine']
    temp_list=[]
    scan_regex=r'[1-9]|oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight|one|two|three|four|five|six|seven|eight|nine'
    capture_regex=[]
    joined_word=['oneight','twone','threeight','fiveight','sevenine','eightwo','eighthree','nineight']
    joined_number=['1,8','2,1','3,8','5,8','7,9','8,2','8,3','9,8']
    for line in input_lines:
        capture_regex=re.findall(scan_regex,line)
        for element in capture_regex:
            if len(element)>=5 and element in joined_word:
                for jw in joined_word:
                    if element==jw:
                        capture_regex[capture_regex.index(element)]=joined_number[joined_word.index(jw)]
        temp_list.append(capture_regex)
    for element_list in temp_list:
        if len(element_list)==1:
            if not (ord(element_list[0])>48 and ord(element_list[0])<58):
                element_list[0]=word_conv(element_list[0])
            two_digit_list.append(int(element_list[0])*10+int(element_list[0]))
        else:
            if re.search(r',',element_list[0]) != None :#joined number at start
                element_list[0]=element_list[0].split(',')[0]
            if re.search(r',',element_list[-1]) != None :#joined number at end
                element_list[-1]=element_list[-1].split(',')[-1]
            if len(element_list[0])>1:
                element_list[0]=word_conv(element_list[0])
            if len(element_list[-1])>1:
                element_list[-1]=word_conv(element_list[-1])
            two_digit_list.append(int(element_list[0])*10+int(element_list[-1]))
        print(element_list)
                
    #print(temp_list)
    print("two digit:",two_digit_list)
    final_score=sum(two_digit_list)
    print(final_score)

