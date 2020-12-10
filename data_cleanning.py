# -*- coding: utf-8 -*-
"""data_cleanning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l0GwIhV1CDCXiUJHQc6UeJJ8FsmsQbEm

# Goal

This data cleaning aims to solve the errors that might appear when using ann and txt to create conll file.
It does not change any word content, instead it just removes some unnecessary but disturbing punctuation.

# Function
"""

def text_cleanup (textfile):
    # This function clean up the text to remove some unnecessary but disturbing punctuation
    # input: txt file
    # output: create a txt file
    # basic rules:
    # " …" -> ","
    # " -" -> " "
    # " ," -> " "
    # "\\'" -> "\\"
    # " ." -> "."
    # ".," -> ","
    # ",." -> "."
    # "  " -> " "
    to_be_replaced = [" …"," -"," ,","\\'"," .",".,",",.","  "]
    replace = [","," "," ","\\",".",",","."," "]
    f = open(textfile, 'r')
    text = f.read()
    f.close()
    l = len(to_be_replaced)
    for i in range(l):
        text = text.replace(to_be_replaced[i],replace[i])
    for i in range(3):
        text = text.replace(to_be_replaced[l-1],replace[l-1])   
    text = text.lstrip()
    outputfile = open("output.txt", "w") 
    outputfile.write(text) 
    outputfile.close()

"""# Example"""

filename = "int119.txt"
text_cleanup(filename)

from google.colab import files
files.download('output.txt')