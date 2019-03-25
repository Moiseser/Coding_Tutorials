#this function prints a statement and then performs an addition of two variables
def add(a,b) :
    print ' ADDING %d + %d'%(a,b)
    return a + b
#this function prints a statement and then performs an subtraction of 2 variables
def subtract(a,b):
    print 'SUBTRACTING %d-%d' %(a,b)
    return a - b
#this function prints a statment and then performs a multiplication
def multiply(a,b):
    print 'MULTIPLYING %d*%d' %(a,b)
    return a*b
#this function prints a statement and then performs a division
def divide(a,b):
    print 'DIVIDING %d/%d'%(a,b)
    return a/b

print 'Let us do some math with just functions!'
#each function is assigned to a variables
#since the function contains a print statement values are printed of the action performed
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide (100,2)
#here each variables is printed with the math performed from the function
print 'Age : %d , Height:%d, Weight:%d , IQ:%d' %(age,height,weight,iq)

#A puzzle for the extra credit, type it in anyway-Zed

print 'Here is a puzzle.'
#this puts the functions and vales calculated above inside one another
#it takes the value and uses it in the function whch in turn gives us a value
#this is then used in another function as a value with another calc. value
what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print 'That becomes : ' , what, 'Can you do it by hand?'
