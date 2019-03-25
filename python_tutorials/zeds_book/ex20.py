from sys import argv

#here we assign are file to a variable called input_file within the code
script, input_file = argv
#this function prints the entire contents of a file
def print_all(f):
    print f.read()
#this function resents the file to line 0 , so the beginning
#f.seek sets out a specific line
def rewind(f):
        f.seek(0)
#this function prints a specific line, and reads it to print
def print_a_line(line_count,f):
    print line_count, f.readline()


#this assings are initial input file from the terminal to a variable called
#current file
current_file = open(input_file)
#first the entire file is printed using our first funciton
print 'First lets print the whole file:\n'

print_all(current_file)

print 'Now lets rewind , kind of like a tape'
#we reset our function to line 1
rewind(current_file)

print 'Lets print three lines'
#each function prints a line and then skips a line following by printin the next line
current_line = 1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)


current_line = current_line+1
print_a_line(current_line,current_file)
