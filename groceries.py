#!/usr/bin/env python
# open file for appending and reading, create if doesn't exist
f = open('glist', 'a+')
# create empty grocery list
groceries = []
choice=raw_input("Add grocery items?")
while choice[0] == 'y':
    gitem = raw_input("Enter a grocery item: ")
    if gitem in f.read():
        print "You already added " + gitem + "to the list."
    else:
        print("Adding " + gitem + " to the list")
        groceries.append(gitem)
        f.write(gitem + '\n')
	print f.read()
	choice=raw_input("Add another item? ")
print("Goodbye!")
