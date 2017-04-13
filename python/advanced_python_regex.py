#Q1)
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/andrewkruger/dsp/master/python/faculty.csv')
deg_dict = {}

for degs in df[' degree']:
    for deg in degs.lstrip(' ').replace('.','').split(' '):
        if deg != '0':
            deg_dict[deg] = deg_dict.get(deg, 0) + 1

print deg_dict

