import csv
import pandas as pd
import requests
import json

df = pd.read_csv(r'/Users/michelleglewis/Downloads/ira_tweets_csv_hashed.csv', low_memory = False)

dictionary = {}

for i in df:
    tweet = df[13][i]
    data = tweet.json()
    words = tweet.split()
    for x in words:
        if x not in dictionary:
            dictionary[x] = 1
        else:
            dictionary[x] = dictionary[x] + 1    

listofwords = list((dictionary.keys(), dictionary.values()))
sortedlist = sorted(listofwords, key=lambda tup: tup[1], reverse=True)
word1 = sortedlist[0]
word2 = sortedlist[1]
word3 = sortedList[2]
word4 = sortedlist[3]
word5 = sortedlist[4]

print(word1[0] + ":" + word1[1])


        
