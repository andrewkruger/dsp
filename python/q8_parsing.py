# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/andrewkruger/dsp/master/python/football.csv')
indexof_MinDiff = abs(df['Goals']-df['Goals Allowed']).idxmin()
print df['Team'][indexof_MinDiff]
