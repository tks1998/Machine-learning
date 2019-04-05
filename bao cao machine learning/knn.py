#from __future__ import print_function
import numpy as np
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from distance import *
from scalingdata import *
#import data  from data.txt

A = np.genfromtxt('data.txt', delimiter=',') 
 

trainX = A[:60,0:5]
trainY = A[:60,5]
trainX = scaling2(trainX)

#print(trainX)
#print(trainY)
testX = A[60:80,0:5]
testX = scaling2(testX)
testY = A[60:80,5]
k = 5
p = 2 
build = computing_knn(trainX,trainY,testX,k,p)

# output f1_score ,  accuracy ,presicion 

ouput(build,testY,k)

#print ( build )



    
