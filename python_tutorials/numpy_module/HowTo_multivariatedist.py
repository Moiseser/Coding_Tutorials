import numpy as np 
from matplotlib import pyplot as plt

#Generating random numbers from a multivariate distribution
#A multivariate distribution is a highly dimensional gaussian
#numpy.random.multivariate_normal(mean, cov[, size, check_valid, tol])

#Generate array of N gaussian numbers 
#input mean : array of legnth N 
#input covariance matrix which is a diagonal (N,N) matrix


x = np.zeros ([2,2])
x[0,0] = 5
x[1,1] = 8
mean_x = [0,0]
print x 
random_x = np.random.multivariate_normal([0,0],x)
print random_x
print random_x[0]
print random_x[1]
