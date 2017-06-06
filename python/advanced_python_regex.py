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

#### Q1) Count Degrees

# Complete the function below.

def count_degrees(csv_file_name):
    with open(csv_file_name) as f:
        degrees = {}
        f.readline()
        for line in f:
          dat = line.strip('\n').split(',')
          deg = dat[1].replace('.','').upper()
          degs = deg.lstrip(' ').split(' ')
          for d in degs:
              degrees[d] = degrees.get(d,0) + 1
        return degrees

try:
    degreecounts = count_degrees('faculty.csv')
    os.remove('faculty.csv')
except Exception as e:
    os.remove('faculty.csv')
    raise(e)
    
degreecounts = {
    str(key).replace(' ', '').replace('.', '').upper(): val
    for key, val in degreecounts.items()
}

degrees = ['MD', 'MA', 'SCD', 'BSED', 'PHD', '0', 'MPH', 'MS', 'JD']
assert len(degrees) >= len(degreecounts), 'did you get all the different degrees?'
assert len(degrees) == len(degreecounts), 'your output has too many degrees'
for degree in degrees:
    count = degreecounts.get(degree, -1)
    print(count)
    

#### Q2) Count Titles

# Complete the function below.

def count_titles(csv_file_name):
    with open(csv_file_name) as f:
        titles = {}
        f.readline()
        for line in f:
          dat = line.strip('\n').split(',')
          t = dat[2][:9].lower()
          titles[t] = titles.get(t,0) + 1
        return titles  

try:
    titlecounts = count_titles('faculty.csv')
    os.remove('faculty.csv')
except Exception as e:
    os.remove('faculty.csv')
    raise(e)
    
degreecounts = {
    str(key).replace(' ', '').replace('.', '').lower()[:9]: val
    for key, val in titlecounts.items()
}

titles = ['professor', 'associate', 'assistant']
assert len(titles) >= len(titlecounts), 'did you get all the different titles?'
assert len(titles) == len(titlecounts), 'your output has too many titles'
for title in titles:
    count = titlecounts.get(title, -1)
    print(count)
    
    
#### Q3) Emails

# Complete the function below.

def emails(csv_file_name):
    emails = []
    with open(csv_file_name) as f:
        f.readline()
        for line in f:
            data = line.strip('\n').split(',')
            emails.append(data[3])
        return emails
    
try:
    email_list = emails('faculty.csv')
    os.remove('faculty.csv')
except Exception as e:
    os.remove('faculty.csv')
    raise(e)
    
for email in sorted(email_list):
    print(email.lower())
    

#### Q4) Email Domains

def unique_domains(emails):
    domains = []
    for email in emails:
        domain = email.split('@')[1]
        if domain not in domains:
            domains.append(domain)
    return domains

emails = sys.stdin.readlines()
emails = [email.strip() for email in emails]
domains = unique_domains(emails)
for domain in sorted(domains):
    print(domain)



''' USING PANDAS
####Q1)
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/andrewkruger/dsp/master/python/faculty.csv')
deg_dict = {}

for degs in df[' degree']:
    for deg in degs.lstrip(' ').replace('.','').split(' '):
        if deg != '0':
            deg_dict[deg] = deg_dict.get(deg, 0) + 1

print '\nQ1. Find how many different degrees there are, and their frequencies:\n' 
print 'Number of degrees: ',len(deg_dict), '\n'
print sorted(sorted(deg_dict.items(), key=lambda item: item[0]), key=lambda item: item[1])


####Q2)
title_dict = {}
for title in df[' title']:
    title = title.replace(' is ',' of ') #One degree has 'is' instead of 'of'
    title_dict[title] = title_dict.get(title, 0) + 1

print '\n\nQ2. Find how many different titles there are, and their frequencies:\n'
print 'Number of titles: ', len(title_dict), '\n'
print sorted(sorted(title_dict.items(), key=lambda item: item[0]), key=lambda item: item[1])


####Q3)
print '\n\nQ3. Search for email addresses and put them in a list:\n'
print list(df[' email'])


####Q4)
domain_dict = {}

for email in df[' email']:
    domain = email.split('@')[1]
    domain_dict[domain] = domain_dict.get(domain, 0) + 1

print '\n\nQ4. Find how many different email domains there \
are and print the list of unique email domains:\n'
print 'Number of email domains: ',len(domain_dict), '\n'
print sorted(sorted(domain_dict.items(), key=lambda item: item[0]), key=lambda item: item[1])
'''
 
