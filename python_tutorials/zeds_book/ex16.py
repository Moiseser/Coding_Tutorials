#this allows us to use the argv command
from sys import argv
#this lets us type in our filename when executing our script
script,filename = argv
#here we print out a series of commands containg information to be told to the user
print 'We are going to erase %r' %filename
print 'If you dont want that hit CTRL-C'
print 'If you do want that, hit RETURN'
#here we choose which direction to take
raw_input('?')

#A file is opened, the 'w' command opens it in write mode
print 'Opening the file...'
target = open(filename,'w')

#here we delete in previous text in the file
print 'Truncating the file. Goodbye!'
target.truncate()


print 'Now I am going to ask you for three lines'
#we create three variables, which we each assign a characters to manually
line1 = raw_input('line1:')
line2 = raw_input('line2:')
line3 = raw_input('line3:')

print 'Im going to write these to a file'
#we write the assigned variables to a file
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
#the file is closed!
print 'Finally we close it'
target.close()

text = open(filename)
print text.read()
