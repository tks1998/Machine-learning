import numpy as np
def scaling(data ):
    for i in range(0,len(data)):
        data[i] = data[i]/(np.sum(data[i]*data[i])+1)
    return data