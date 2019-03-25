#here we set an intial value for i
i = 0
#we create an empty list
numbers = []
#set our while statement for our loop
while i < 6 :
#everytime we go through the loop we want to see what the new value of i is
    print 'At the top i is %d' %i
#we add the new number to our list
    numbers.append(i)
#here is our piece of code that is increasing i
    i= i + 1
#here we check what our list looks like now
    print 'Numbers now:' , numbers
    print 'At the bottom i is %d' % i

#here we print the full list
print 'The numbers:'
for numeros in numbers:
    print numeros
