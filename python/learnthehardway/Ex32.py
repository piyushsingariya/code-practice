#Loops and List
the_count = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list

for number in the_count:
    print ("This is the count %d") % number

# same as above
for fruits in fruits:
    print ("A fruit of type: %s") % fruits

# aslo we can go through mixed lists too
# notice we have to usue %r since we don't know what's in it

for i in change:
    print ("I got %r from the change list") % i

# we can also build lists, first start with an empty one.
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print ("Adding %d to the list.") % i
    # append is a function that lists understand
    elements.append(i)

# Now we can print them out too
for i in elements:
    print ("An Element was %d ") % i

print ("This is the End!!! Thank You...")