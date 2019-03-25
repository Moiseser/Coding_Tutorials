#statment beginning the set of options
print 'You enter a dark room with two doors. Do you go through door #1 or door #2?'
#raw input allows to put in our own variable from the terminal
door = raw_input('>')
#depending on our input we we either on or first if statement, or elif, or else
if door == '1' :
    print 'There is a giant here eating cheese cake. What do you do?'
    print '1. Take the cake'
    print '2.Scream the bear'
#we are given two options to choose from and again input a choice from the terminal
    bear == raw_input('>')
#these next if statement are all within the first if statement
    if bear == '1':
        print 'The bear eats your face off. Good job.'
    elif bear == '2':
        print  'The bear eats your legs off. Good job'
    else :
        print 'Well doing $s is probably better. Bear runs away.'    %bear
#this is the begining of the second option if 1 was not selecged
elif door == '2' :
    print 'You stare into the endless abyss at Cthulus retina'
    print '1.Blueberries'
    print '2. Yellow Jacket clothespins'
    print '3. Understanding revolvers yelling melodies'

    insanity == raw_input('>')

    if insanity == '1' or insanity == '2' :
        print 'Your body survives powered by a mind of jello. Good Job!'

    else :
        print 'The insanity rots our eyes into a pool of muck. Good job.'
#if neither if statement was completed we go with else statement
else :
    print 'you stumble aound and fall on a knife and die. Good job!'
