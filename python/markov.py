#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.


# Note: This program starts with the start of a sentence it identified in the text.


import argparse
import string
import random


#Get parameters:
    
parser = argparse.ArgumentParser(description='Markov text generator.')
parser.add_argument('filename', nargs=1, help='filename of source text')
parser.add_argument('nwords', metavar='N', nargs=1, type=int,
                   help='integer number of words to be used in text')
args = parser.parse_args()

fn = args.filename[0]
nwords = args.nwords[0]


#Read in text:
    
#If I want to exclude punctuation
#exclude = list(string.punctuation)

word_list = []

with open(fn) as tm:
    for line in tm:
        words = line.strip('\n').split(' ') #separate words
        for word in words:
            if len(word) > 0:
                word_list.append(word)
'''If certain characters or punctuation needs to be removed:
            w = ''
            for c in word:
                if c not in exclude:
                    w+=c
            if len(w) > 0:
                word_list.append(w)
'''   


# Create dictionaries to be used in markov chains:
        
markov = {}
mark_start = {}
startSentence = True
for i in range(len(word_list)-2):
    if startSentence:
        try:
            mark_start[(word_list[i],word_list[i+1])].append(word_list[i+2])
        except KeyError:
            mark_start[(word_list[i],word_list[i+1])] = [word_list[i+2]]
        startSentence = False

    try:
        markov[(word_list[i],word_list[i+1])].append(word_list[i+2])
    except KeyError:
        markov[(word_list[i],word_list[i+1])] = [word_list[i+2]]
    if word_list[i][-1] in ['.','?','!']:
        startSentence = True
      
   
# Create text, and start with beginning of a sentence:
                
seed = random.randint(0, len(mark_start))
keys = mark_start.keys()[seed]

out_string = keys[0] +' ' +keys[1]

for i in range(nwords - 2):
    l = len(markov[keys])
    if l > 1:
        seed = random.randint(0,l-1)
    else:
        seed = 0
    newWord = markov[keys][seed]
    keys = (keys[1],newWord)
    out_string += ' ' + newWord


#Print text:
    
print out_string
