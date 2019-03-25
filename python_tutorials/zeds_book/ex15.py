#This allows your script to ask you on the terminal for an input
from sys import argv
#this command asks you what the name of your text file you want to read is
script,filename = argv
#this opens the file and then assigns the opened file to a variable
txt = open(filename)

#here we print the name of the file
print 'Heres your file %s' % filename
#here the contents of the file are printed onto the terminal
print txt.read()
#text is printed on the terminal
print 'Type the filename again'
#here we again manually input into script whht the name of the of the file is
file_again = raw_input('>')
#the opened file again is assigned to this variable
txt_again = open(file_again)
#contents printed
print txt_again.read()
