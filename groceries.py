#!/usr/bin/env python
# open file for appending and reading, create if doesn't exist
f = open('glist', 'a+')
# print file contents below
print f.read()
# create empty grocery list
groceries = []
gitem = raw_input("Enter a grocery item: ")
print("Adding " + gitem + " to the list")
groceries.append(gitem)
f.write(gitem + '\n')
print(groceries)
print f.read()
