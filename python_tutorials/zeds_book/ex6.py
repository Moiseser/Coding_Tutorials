#This line allocates a string with a number value to th variable 'x'
x = 'There are %d types of people' %10
#This allocates the word binary to the character binary
binary = 'binary'
#This line allocates the word dont to the string do_not
do_not = "dont"
#This allocates a string of text with two python commans to the varible 'y'
y= 'Those who know %s and who %s' %(binary,do_not)
#these commands print everything associated to the variables x and y
print x
print y
#These lines print a string which contains a command that uses th variables defined above
print 'I said : %r' %x
print ' I also said %r' %y

hilarious = False
joke_evaluation = 'Isnt that joke so funny ?! %r'

print joke_evaluation %hilarious

w = 'This is the left side of ...'
e = 'a string with a right side'

print w + e
