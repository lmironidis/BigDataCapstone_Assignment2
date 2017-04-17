import re
import codecs
from collections import Counter
from string import punctuation

'''
Group Members: Loukas Mironidis, Caitlyn Lambert
Big Data Capstone Assignment 2 Part D
3/7/2017

Description:
This Python script can run all questions asked for part D together
Using the cleaned output file from Part B called 'partb_output' also
utilizing re, codecs, Counter, and string libraries

Questions from Part D:
1.  How big is the corpus (# of words)?
2.  What is the average word length? 
3.  Which is the longest word?
4.  How many hapax words are there? How many percent of the corpus are they?
5.  What are the 10 most frequent words? How many percent of the corpus consists of these words?
'''

# Reads XML file into a unicode String
contents = codecs.open('partb_output', 'r', encoding="UTF-8").read()

''' Question 1 '''
# Counts the number of words
NumWords = len(re.findall('\s+', contents))
print('Question 1 - ') 
print('Number of words: %d \n' % (NumWords))



''' Question 2 '''
# Finds the average
average = (len(word) for word in contents.split())
print('Question 2 - ')
print('Average word length: %d \n' % (sum(average)/len(contents.split())))



''' Question 3 '''
# Creates an empty string and finds the longest word
str=''
for word in contents.split():
        if (len(word)) > (len(str)): str = word 
print('Question 3 - ')
print ('Longest Word: %s \nWord Length: %d \n' % ((str), len(str)))



''' Question 4 '''
# Creates two unordered collections of items where there are no duplicates
# It will then search allwords for any duplicates, then print out the
# number of Hapax words and percent of times it shows up.
with open('partb_output') as file:
    allwords = set()
    duplicates = set()
    for word in (word for current in file for word in current.split()):
        if word in allwords:
            duplicates.add(word)
        allwords.add(word)
    unique = allwords - duplicates
print('Question 4 - ')
print ('Number of Hapax words:', len(unique), ' Percent: %.2f' % round(len(unique)/NumWords*100, 2), '\n')



''' Question 5 '''
words = contents.split()

# Takes the data and appends unique words inside an array
uniques = []
for word in words:
  if word not in uniques:
    uniques.append(word)

# Iterates over the unique words and checks if the word is equal to the current unique
# word and appends them as tuples as (count, unique).  Then it will sort and reverse the data
# in the array.
counts = []
for unique in uniques:
  count = 0
  for word in words:
    if word == unique:
      count += 1
  counts.append((count, unique))
counts.sort()
counts.reverse()

# Finds and prints the words with the highest counts and
# displayes frequent word, times, and percent it shows up.
print('Question 5 - ')
for n in range(min(10, len(counts))):
  count, word = counts[n]
  print('Frequent word:', word,'  Number of times:', count, 'Percent: %.2f' % round(count/NumWords*100, 2))
