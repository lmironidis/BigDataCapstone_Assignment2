import re
import codecs
import xml.sax.saxutils as sax

'''
Group Members: Loukas Mironidis, Caitlyn Lambert
Big Data Capstone Assignment 2 Part B
3/7/2017

Description:
This python script cleans the xml data downloaded from Wiki and
produces an output file with the cleaned data output.  For this
libraries re, codecs, and saxutils will be used to do this.

Questions from Part B:
1.  First strip away all HTML tags.
2.  Then translate the most important html entites like this: (<,>,",&).
3.  Finally remove the wiki formatting.
'''

# Reads XML file into a unicode string 
contents = codecs.open("greek_dev.xml", 'r', encoding="UTF-8").read()
text = open("partb_output", "w")

# Removes Wiki Format 
removeWikiFormat = re.sub('[\:\=\#\*\[\]\{\}\d\,]', '', contents)

# Replaces Html Entities with (<,>,",&) 
replaceHtmlEnts = sax.unescape(removeWikiFormat,{"&apos;": "'", "&quot;": '"'})

# Removes Html Tags #
removeHtmlTags = re.sub('<[^<]+?>', '', replaceHtmlEnts)

# Outputs Cleaned XML data 
text.write(removeHtmlTags)

# Closes the file
text.close()
