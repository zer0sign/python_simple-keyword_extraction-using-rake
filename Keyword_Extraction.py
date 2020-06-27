# AHMAD AL HASAN 32601700003
# in this simple program i using a library from python the name of this library is RAKE(Rapid Automatic Keyword Extraction Algorithm)
# RAKE is using to make keyword extraction
# btw this program is author make to complete task from exame in information Retrieval
# the author is ahmad al hasan with his student number/NIM 32601700003 UNISSULA


# first import the library, if you dont have RAKE, first you need to install RAKE with write
# this in terminal "sudo pip install rake-nltk" btw i using ubuntu 18.04 lts.

import rake
import operator


# now load a text and apply rake on it
lokasi_file = "text.txt"
text_rake = rake.Rake(lokasi_file)

sample = open("/home/zerosign/Desktop/dev/Python/information_retrieval - Keyword Extraction/text.txt", "r")
text = sample.read()
keywords = text_rake.run(text)

print(keywords)

# output
# [('python', 1.0), ('rake', 1.0), ('keyword', 1.0), ('extraction', 1.0)]





