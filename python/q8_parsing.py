# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Don't use pandas.

# Following functions will be called like this:
#   footballTable = read_data('football.csv')
#   minRow = get_index_with_min_abs_score_difference(footballTable)
#   print str(get_team(minRow, footballTable))


#!/bin/python3

import sys
import os
import csv

text = '''Team,Games,Wins,Losses,Draws,Goals,Goals Allowed,Points
Arsenal,38,26,9,3,79,36,87
Liverpool,38,24,8,6,67,30,80
Manchester United,38,24,5,9,87,45,77
Newcastle,38,21,8,9,74,52,71
Leeds,38,18,12,8,53,37,66
Chelsea,38,17,13,8,66,38,64
West_Ham,38,15,8,15,48,57,53
Aston_Villa,38,12,14,12,46,47,50
Tottenham,38,14,8,16,49,53,50
Blackburn,38,12,10,16,55,51,46
Southampton,38,12,9,17,46,54,45
Middlesbrough,38,12,9,17,35,47,45
Fulham,38,10,14,14,36,44,44
Charlton,38,10,14,14,38,49,44
Everton,38,11,10,17,45,57,43
Bolton,38,9,13,16,44,62,40
Sunderland,38,10,10,18,29,51,40
Ipswich,38,9,9,20,41,64,36
Derby,38,8,6,24,33,63,30
Leicester,38,5,13,20,30,64,28'''

with open('football.csv', 'w') as f:
    f.write(text)


def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    table = []
    with open(filename) as f:
        f.readline()
        for line in f:
            data = line.strip('\n').split(',')
            table.append([data[0]]+list(map(int,data[1:])))
    return table

def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    goal_diff = [abs(g[5]-g[6]) for g in goals]
    return goal_diff.index(min(goal_diff))
    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    return parsed_data[index_value][0]
   
footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))

    
# Using pandas
'''import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/andrewkruger/dsp/master/python/football.csv')
indexof_MinDiff = abs(df['Goals']-df['Goals Allowed']).idxmin()
print df['Team'][indexof_MinDiff]
'''


