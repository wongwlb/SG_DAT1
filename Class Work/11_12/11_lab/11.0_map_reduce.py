# -*- coding: utf-8 -*-
"""
Created on Wed Aug 4

@author: sinanozdemir
adapted from https://www.wakari.io/sharing/bundle/nkorf/MapReduce%20Example
"""

# this function should turn a string into a list of (word, 1)
def mapper(line):
    result = []
    # CODE ME PLEASE
    return result
    # output is a list of (key, value) pairs

## Solution
def mapper(line):
    result = []
    for i in line.split():
        result.append((i, 1))
    print result
    return result

mapper("Hi everyone Hi Hi")
# [('Hi', 1), ('everyone', 1), ('Hi', 1), ('Hi', 1)]
# note that duplicates are expected

## Output:
[('Hi', 1), ('everyone', 1), ('Hi', 1), ('Hi', 1)]

# the shuffle function gathers up the like key words
# once it gathers them up, it calls the reduce function!
# I have sorted everything by key for you
# run through the words one by one and create a dictionary
# where the word is the key and the value is the total count
# this is essentially a rehashed Counter but our own :)
# You can print out the results instead of returning them
# As long as the count is clear
def reducer(words):
    # sorting the words
    # CODE ME PLEASE    

## Solution 
def reducer(words):
    sorted_keys = sorted(words)
    tmp=""
    value=''
    for i in sorted_keys:
        if i[0]!=tmp and tmp!="": # saw a new word!
            print tmp, value
            reducer(tmp,value)
            value=1
            tmp=i[0]
            value.append(i[1])
        elif i[0]==tmp or tmp=="":
            tmp=i[0]
            value.append(i[1])
    # get the last key value pair
    print tmp, value
    reducer(tmp,value)

    ## THIS IS WRONG REDO, PHOTO IN PHONE PHOTOS 27/2/2016

reducer([('Hi', 1), ('everyone', 1), ('Hi', 1), ('Hi', 1), ('sinan', 1), ('sinan', 1)])
# Hi 3
# everyone 1
# sinan 2

    
sentences = ['hello big data big big big data ',
             'big data is the best',
             'big data is the best data big',
             'hello big data how are data',
             'big big big data',
             'data data big big']
# list of sentences to analyze   



# TODO run map reduce on sentences


# TODO run MR on a scraped web document (relatively big doc)


