x = ("There are %d types of people.") % 10
binary = 'Binary'
do_not = "don't"
y = ("Those who know %s and those who %s.") % (binary, do_not)
print (x) 
print (y)

print ("I said: %r.") % x
print ("I also said: '%s'.") % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation) % hilarious

w = "This is the left side of ..."
e = "A string with the right side."

print (w + e)