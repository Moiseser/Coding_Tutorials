import numpy as np 
#In this script I will play around with np arrays/matrices to learn them 
#numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

#This is how you reading a 2D array AKA matrix 
Gamma = np.array([[5.,1],[3,8.]])
#print Gamma
#print Gamma*.5
#I was messing with order option, F = fortran = column major, C= row major
xGamma = np.array([[5,0],[0,8]],order = 'F')
this_is_column = np.array([[5,1],[2,8]],order = 'F')
this_is_row = np.array([[5,1],[2,8]],order = 'C')
#print this_is_column
#print this_is_row
#Still not sure how this works? Ill deal with it later. 

#A matrix can be created from np.array which is a subclass of ndarray
#In other words matrices are strictly 2-dimensional arrays. 

a=np.mat('4 3; 2 1')
b=np.mat('1 2; 3 4')
#print a, b 
#matrices are handy because you can do matrix multiplication with '*' operator 
#print a*b

#Lets try this with our 2d array generated above
#print Gamma * Gamma
#As you can see this simply takes each element and multiply them 
# A(i)*B(i), this does not do actual matrix multiplication 
#To do matrix multiplication with ndarrays you use the np.dot object
#print (np.dot(Gamma,Gamma))

#Some final notes 
#the '**' operator behaves different. , .H abd .I are mat exclusive objects
#np.asmatrix and np.asarray allow you to convert one to the other (as long as the array is 2-dimensional)

#Initializing arrays
#this fills your array with zeros 
zero = np.zeros((2,2))
print zero 
#this fills with ones 
ones = np.ones((2,2))
print ones 

# np.empty fills with random numbers and is faster , np.full can specific a number to fill it with 

#multiplication of a matrix with a vector 
column = np.array([2,2])
print column
print (np.dot(a,column))
