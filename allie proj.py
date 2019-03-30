import csv
import pandas as pd
import requests
import json
import unicodecsv as csv

df = pd.read_csv(r'/Users/michelleglewis/Downloads/ira_tweets_csv_hashed.csv', low_memory = False, usecols = ["tweet_text"])

dictionary = {}

for i in df['tweet_text']:
    words = i.split()
    count = count + 1
    for x in words:
        if x not in dictionary:
            dictionary[x] = 1
        else:
            dictionary[x] = dictionary[x] + 1
            
listofwords = [(list(dictionary.keys())[i], list(dictionary.values())[i]) for i in range(len(dictionary.keys()))]

sortedlist = sorted(listofwords, key=lambda tup: tup[1], reverse=True)
word1 = sortedlist[0]
word2 = sortedlist[1]
word3 = sortedlist[2]
word4 = sortedlist[3]
word5 = sortedlist[4]

print(word1[0] + ":" + str(word1[1]))
print(word2[0] + ":" + str(word2[1]))
print(word3[0] + ":" + str(word3[1]))
print(word4[0] + ":" + str(word4[1]))
print(word5[0] + ":" + str(word5[1]))






        
