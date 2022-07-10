# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:25:42 2022

@author: Ravindranath Nemani
"""


def update_tracker(tracker, current, current_length, current_cell_update_rule, direction_set, current_direction_value):
    
    tracker[current][current_direction_value] += 1
    
    for j in range(current_length):
        for direction in direction_set:
            if direction == current_direction_value:
                current = (current[0] + current_cell_update_rule[direction][0], current[1] + current_cell_update_rule[direction][1])
            else:
                pass
        if current not in tracker:
            temp_dict = {}
            for direction in direction_set:
                if direction == current_direction_value:
                    temp_dict[direction] = 1
                else:
                    temp_dict[direction] = 0
            tracker[current] = temp_dict
        else:
            tracker[current][current_direction_value] += 1
            
    return tracker, current


def getPlusSignCount(N, L, D):

    D = D.replace('', ' ').strip().split(' ')

    direction_set = ['L', 'R', 'U', 'D']
    
    origin = (0,0)
    
    tracker = {origin: {'L': 0, 'R': 0, 'U': 0, 'D': 0}}

    current_cell_update_rule = {'L' : [-1, 0], 'R' : [1, 0], 'U' : [0, 1], 'D' : [0, -1]}

    current = origin

    for i in range(len(L)):
        
        if D[i] == 'L':
            tracker, current = update_tracker(tracker, current, L[i], current_cell_update_rule, direction_set, 'L')
        elif D[i] == 'R':
            tracker, current = update_tracker(tracker, current, L[i], current_cell_update_rule, direction_set, 'R')
        elif D[i] == 'U':
            tracker, current = update_tracker(tracker, current, L[i], current_cell_update_rule, direction_set, 'U')
        elif D[i] == 'D':
            tracker, current = update_tracker(tracker, current, L[i], current_cell_update_rule, direction_set, 'D')      

        if i+1 <= len(L)-1:
            if D[i+1] == 'L':
                tracker[current]['L'] += 1
            elif D[i+1] == 'R':
                tracker[current]['R'] += 1
            elif D[i+1] == 'U':
                tracker[current]['U'] += 1
            elif D[i+1] == 'D':
                tracker[current]['D'] += 1

    plus_sign_tracker = {}
    
    for k, v in tracker.items():
        left = (k[0] - 1, k[1])
        right = (k[0] + 1, k[1])
        up = (k[0], k[1] + 1)
        down = (k[0], k[1] - 1)
        if (left in tracker) and (right in tracker) and (up in tracker) and (down in tracker):
               plus_sign_tracker[k] = v
    plus_sign_positions = list(plus_sign_tracker.keys())
    return {'PlusPositions' : plus_sign_positions, 'PlusCount' : len(plus_sign_tracker)}

N = 9
L = [6, 3, 4, 5, 1, 6, 3, 3, 4]
D = 'ULDRULURD'
print(getPlusSignCount(N, L, D))

N = 8
L = [1, 1, 1, 1, 1, 1, 1, 1]
D = 'RDLUULDR'
print(getPlusSignCount(N, L, D))

N = 8
L = [1, 2, 2, 1, 1, 2, 2, 1]
D = 'UDUDLRLR'
print(getPlusSignCount(N, L, D))
