####Q1)
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/andrewkruger/dsp/master/python/faculty.csv')
df[' email'].to_csv('emails.csv', header=False, index = False)