import nltk
import codecs
from nltk.tokenize import RegexpTokenizer

'''
Group Members: Loukas Mironidis, Caitlyn Lambert
Big Data Capstone Assignment 2 Part C
3/7/2017

Description:
This python script will tokenize the cleand output data file from Part B.
For this librarie nltk, codecs, and RegexpTokenizer will be used to do this.

Questions from Part C:
Write another Python function that reads the plain-text corpu, tokenize it
and returns a list of the tokens in the corpus
'''

# Reads XML file into a unicode string 
contents = codecs.open("partb_output", 'r', encoding="UTF-8").read()

# Creates a Tokenizer to seperate words using regex command (\s+)
tokenizer = RegexpTokenizer('\s+', gaps=True)

# Tokenizes the cleaned output file
x = tokenizer.tokenize(contents)

# Prints output to the Python Shell
print(x)
