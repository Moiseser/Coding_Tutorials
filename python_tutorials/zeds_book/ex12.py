#raw_input allows to enter our own variables on the terminal we can insert
# a phrase in quotes to tell the user what to write
age = raw_input('How old are you?')
height = raw_input('How tall are you?')
weight = raw_input('How much do you weigh?')

print 'So you are %s old, %s tall and %s heavy.' % (age, height, weight)
