#!/bin/python3

import sys
import os


facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""

with open('faculty.csv', 'w') as f:
    f.write(facultycsv)

#### Q6) Create dictionary from csv

def get_dict():
    facDict = {}
    with open('faculty.csv') as f:
        f.readline()
        for line in f:
            data = line.strip('\n').split(',')
            lastName = data[0].split(' ')[-1]
            if lastName not in facDict:
                facDict[lastName] = [data[1:]]
            else:
                facDict[lastName].extend([data[1:]])
        return facDict

answer = get_dict()
n = 0
for key, vals in answer.items():
    assert all('{key},{val}'.format(key=key, val=','.join(val)) in facultycsv
               for val in vals)
    n += len(vals)
assert n == facultycsv.count('\n')
print(1)

#### Q7) Create dictionary from csv Part 2

def get_dict():
    facDict = {}
    with open('faculty.csv') as f:
        f.readline()
        for line in f:
            data = line.strip('\n').split(',')
            name = tuple(data[0].split(' '))
            facDict[name] = data[1:]
        return facDict  

answer = get_dict()
for key, val in answer.items():
    assert '{key},{val}'.format(key=' '.join(key), val=','.join(val)) in facultycsv
assert len(answer) == facultycsv.count('\n')
print(1)

''' Using pandas (before seeing format in hackerrank)
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
'''
