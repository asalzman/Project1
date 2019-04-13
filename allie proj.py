#import csv
import requests
import json
import unicodecsv as csv

#f = open("/Users/michelleglewis/Downloads/ira_tweets_csv_hashed.csv", "rb")
userinput = input('Enter name of file')
f = open(userinput, "rb")
df = csv.reader(f, encoding = 'utf-8')

dictionary = {}

count = 0
_ = next(df)
for i in df:
    words = i[12].split()
    for x in words:
        if x not in dictionary:
            dictionary[x] = 1
        else:
            dictionary[x] = dictionary[x] + 1
    if count%100000 == 0:
        print (count)
    count = count + 1

listofwords = [(x, dictionary[x]) for x in dictionary.keys()]
# not sure if x is the right thing to use in ^
#listofwords = [(list(dictionary.keys())[i], list(dictionary.values())[i]) for i in range(len(dictionary.keys()))]

sortedlist = sorted(listofwords, key=lambda tup: tup[1], reverse=True)

for i in range(5):
    word = sortedlist[i]
    print(word[0] + ": " + str(word[1]))
