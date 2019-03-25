#print statements to test our \ symbols and remember what they do
print 'Let us practive everything'
print 'You\'d need to know \' bout escapes with \\ that do \n newlines and \t tabs'
#three quotations will print in individual lines as formatted Here
#also we are setting this block of text to variable 'poem'
poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
'''

print '_ _ _ _ _ _ _ _ _ _ _ _ '
print poem
print '_ _ _ _ _ _ _ _ _ _ _ _ '
#set a series of numerical operations value to a variable
five = 10 -2 + 3 -6
we write out the value of previous variable
print 'This should be five %s' %five
#create a function that uses values calculated in next newlines
#return saves the values to those variables
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return jelly_beans, jars, crates
#set a value to a variable
start_point = 10000
#set variable equal to the values stored by return character
beans , jars , crates = secret_formula(start_point)
#print out our values
print 'With a starting point of : %d' %start_point
print 'We have %d beans, %d jars, and %d crates' %(beans,jars,crates)

start_point = start_point / 10

print 'We can also do that this way:'
print 'We have %d beans , %d jars, and %d crates' %(secret_formula(start_point))
