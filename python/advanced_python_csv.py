#### Q5) Write to File

#!/bin/python3

import sys
import os

def write_to_csv(list_of_emails):
    with open('emails.csv', 'w') as f:
        f.write('list_of_emails\n')
        for email in list_of_emails:
            f.write(email+'\n')

emails = list(map(str.strip, sys.stdin.readlines()))
write_to_csv(emails)
assert os.path.exists('emails.csv'), 'did you write to "emails.csv"?'
with open('emails.csv', 'r') as f:
    header = f.readline()
    emails2 = []
    for line in f.readlines():
        emails2.append(line.strip())
os.remove('emails.csv')
assert all(i == j for i, j in zip(emails, emails2)), 'this list of emails is different'
assert len(emails) == len(emails2), 'this list of emails is different'
print(1)

''' With pandas
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/andrewkruger/dsp/master/python/faculty.csv')
df[' email'].to_csv('emails.csv', header=False, index = False)
'''
