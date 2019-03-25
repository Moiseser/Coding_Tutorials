#here we set a list of things equal to a variable
ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print 'Wait theres not ten things in that list , lets fix that.'
#this line splits the list up and adds commas between each string
stuff = ten_things.split(' ')
#print ten_things.split(' ')
#here we define a list of more thingd
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana','Girl', 'Boy']

while len(stuff) != 10:
    #.pop takes the last term in more_stuff removes it and asigns it to next_one
    next_one = more_stuff.pop()
    #this shows us what term is being added
    print 'Adding:' , next_one
    #here we add the new string to our initial list
    stuff.append(next_one)
    #since we use the %d we see how long the list is
    print 'there are %d items now.' %len(stuff)

#here we print our newly created list!
print 'There we go:' , stuff

print 'Let us do some things with stuff'
#this prints the 1 item in the list in cardinal numbers
print stuff[1]
#this one prints the number at the very end since -1 is before 0 it goes to the end
print stuff[-1]
#again .pop takes the last term in a list
print stuff.pop()
#here the list is printed nd we see corn has been removed
print ' '.join(stuff)
#this prints items in the list from range 3-5, which is 3 and 4. 
print '#'.join(stuff[3:5])
