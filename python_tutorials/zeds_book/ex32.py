the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges','pears','apricots']
change = [1, 'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
#this assings the list of numbers from the defined 'the_count'
#for numbers in the_count :
    #print 'This is count %d' %numbers

#same s above
#again this just writes out a list which is assinged to fruit
#for fruit in fruits:
#    print 'A fruit of type %s' %fruit

#also we can go thorugh mixed lists too
#notice we have to use %r since we dont know whats in it
#this again assigns our list to a variable but we have to use r
#since its a list of mixed numbers and characters
#for i in change :
#    print 'I got %r' %i

#we can also build lists, first start with an empty one
#here an empty list is built
elements = []

#then use the range function to do 0 to 5 counts
#here we create a list for a range in variable i
for i in range (0,6):
    print 'Adding %d to the lists' %i
    #append is a function that lists underground
    elements.append(i)

#now we can print them out too
for i in elements :
    print 'Element was %d' %i
