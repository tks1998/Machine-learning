import numpy as np
def scaling(data ):
    for i in range(0,len(data)):
        data[i] = data[i]/(np.sum(data[i]*data[i])+1)
    return data
def scaling2(data):
    t = np.mean(data,axis = 0 ) 
    st = np.std(data,axis = 0)
    for i in range(0,1):
        data[:,i] = (data[:,i] - t[i] ) / st[i] ;  
    return data