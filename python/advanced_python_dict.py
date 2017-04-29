import pandas as pd
#df = pd.read_csv('https://raw.githubusercontent.com/andrewkruger/dsp/master/python/faculty.csv')

def cleanDeg( deg_str ):
    degrees = deg_str.split(' ')
    for i in range(len(degrees)):
        if (degrees[i] == '0'):
            degrees[i] = 'None'
        elif degrees[i][:2] == 'Ph':
            degrees[i] = 'Ph.D.'
        elif degrees[i][:2] == 'Sc':
            degrees[i] = 'Sc.D.'
        elif (degrees[i][0] == 'M'):
            if ('S' in degrees[i]):
                degrees[i] = 'M.S.'
            elif ('P' in degrees[i]):
                degrees[i] = 'M.P.H.'
            else:
                degrees[i] = 'M.D.'
        elif (degrees[i][0] == 'J'):
            degrees[i] = 'J.D.'
        elif (degrees[i][0] == 'B'):
            degrees[i] = 'B.S.Ed.'
    return " ".join(degrees)

    
faculty_dict = dict()
for i in range(len(df)):
    lastName = df['name'][i].split(' ')[-1]
    info = [cleanDeg(df[' degree'][i].strip()), df[' title'][i][:-17], df[' email'][i]]
    try:
        faculty_dict[lastName].append(info)
    except KeyError:
        faculty_dict[lastName] = [info]

print '\nQ6:'
fd_keys = faculty_dict.keys()
for key, val in faculty_dict.items()[:3]:
    print key, val
    

new_facDict = {}

for i in range(len(df)):
    name = df['name'][i].split(' ')
    lastName = name[-1]
    firstName = name[0]
    info = [cleanDeg(df[' degree'][i].strip()), df[' title'][i][:-17], df[' email'][i]]
    new_facDict[(firstName, lastName)] = [info]

print '\nQ7:'
for key, val in new_facDict.items()[:3]:
    print key, val

from collections import OrderedDict
sorted_dict = sorted(new_facDict.items(), key=lambda item: item[0][1])
sorted_facDict = OrderedDict((k, v) for k, v in sorted_dict )

print '\nQ8:'
for key, val in sorted_facDict.items()[:3]:
    print key, val
