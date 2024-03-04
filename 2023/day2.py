'''
Author: Vaibhav Kanojia
Purpose: Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?
what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
Created: 02.12.2023
Updated: 06.12.2023
'''
import re
input_stream=r'C:\AdventOfCode\2023\day2_input.txt'
final_score=0

if __name__ == "__main__":
    #Dissecting string by string
    input_content=open(input_stream,'r')
    input_lines=input_content.readlines()
    game_dict={}
    selected_game=''
    max_red_cubes=12
    max_green_cubes=13
    max_blue_cubes=14
    red_cube=0
    green_cube=0
    blue_cube=0
    impossible_game_ids=[]
    all_game_id_list=[]

    min_rgb_list=[]
    for line in input_lines:#creating dict with game id's as Key
        game_dict[line.split('Game ')[-1].split(':')[0]]=line.split(':')[-1].split(';')
    #print(game_dict)
    for key,value in game_dict.items():
        print(value)
        min_red_req=0
        min_green_req=0
        min_blue_req=0
        for element in value:
            if re.search(r'red',element)!=None:
                red_cube=int(element.split('red')[0].split(' ')[-2])
            else:
                red_cube=0
            if re.search(r'green',element)!=None:
                green_cube=int(element.split('green')[0].split(' ')[-2])
            else:
                green_cube=0
            if re.search(r'blue',element)!=None:
                blue_cube=int(element.split('blue')[0].split(' ')[-2])
            else:
                blue_cube=0
            #print('red:',red_cube,' green:',green_cube,' blue:',blue_cube)
            if min_red_req<red_cube:
                min_red_req=red_cube
            if min_green_req<green_cube:
                min_green_req=green_cube
            if min_blue_req<blue_cube:
                min_blue_req=blue_cube
        print('min red:',min_red_req,' green:',min_green_req,' blue:',min_blue_req)
        min_rgb_list.append(min_red_req*min_green_req*min_blue_req)
    print(min_rgb_list)
    print(sum(min_rgb_list))

'''
#part1
    for line in input_lines:#creating dict with game id's as Key
        game_dict[line.split('Game ')[-1].split(':')[0]]=line.split(':')[-1].split(';')
    print(game_dict)
    for key,value in game_dict.items():
        print(value)
        for element in value:
            red_cube=int(element.split('red')[0].split(' ')[-2])
            green_cube=int(element.split('green')[0].split(' ')[-2])
            blue_cube=int(element.split('blue')[0].split(' ')[-2])
            if red_cube>max_red_cubes or green_cube>max_green_cubes or blue_cube > max_blue_cubes:
                print("Impossible Game:",key)
                print(element)
                if key not in impossible_game_ids:
                    impossible_game_ids.append(int(key))

    impossible_game_ids=list(dict.fromkeys(impossible_game_ids))#remove dupl

    for iterator in range(1,len(game_dict.keys())+1):#sum of all Game id's
        all_game_id_list.append(iterator)
    
    print(impossible_game_ids)
    print(all_game_id_list)
    
    for element in impossible_game_ids:
        print(element)
        all_game_id_list.remove(element)
        print(all_game_id_list)
    final_score=sum(all_game_id_list)
    print(final_score)
'''

