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
