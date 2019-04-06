#from __future__ import print_function
import numpy as np
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from distance import *
from scalingdata import *
#import data  from data.txt

A = np.genfromtxt('data.txt', delimiter=',') 
 

trainX = A[:60,0:5]
p = np.array(np.zeros(60)) 
for i in range (0,60):
    p[i] = np.sqrt((np.sum(A[i]*A[i])))

trainY = A[:60,5]
t = np.mean(trainX,axis = 0 ) 
st = np.std(trainX,axis = 0)
   
#trainX = scaling2(trainX,t,st)
trainX=scaling(trainX,p)
#print(trainX)
#print(trainY)
testX = A[60:80,0:5]
#testX = scaling2(testX,t,st)
testX = scaling(testX,p)
print(testX)
testY = A[60:80,5]
k = 5
p = 2 
build = computing_knn(trainX,trainY,testX,k,p)

# output f1_score ,  accuracy ,presicion i

ouput(build,testY,k)

#print ( build )




    
