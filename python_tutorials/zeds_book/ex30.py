#sets numbers equal to numbers
people = 30
cars = 30
buses = 15

#This command compares the values of the two variables
#and prints a command depending on the value or goes on to the if
if cars > people :
    print 'We should take the cars.'
#depending on the if statement it will move on to the else if and look at another
#boolean expression to determine the next thing to do
elif cars < people :
    print 'We should not take the cars'
#if both if statements fail then it goes to an else which is a final choice
else:
    print 'We cant deicde!'

if buses > cars :
    print 'There are too many buses'
elif buses < cars :
    print 'Maybe we could take the buses'
else :
    print 'We still cant decide'
#another if statmenet comparing two numbers
if people > buses :
    print 'Alright , lets just take the buses'
#an else statement can be used after an if as well 
else :
    print 'Fine lets stay hom.e'
