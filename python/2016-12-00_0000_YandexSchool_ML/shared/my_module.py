import operator
import numpy as np
    
    
def trace(str):
    print(str)
    return
    
    
def off_trace(str):
    # print(str)
    return
    
    
    
def getModifCountColRow(count=-1, col=-1, row=-1):    
    if count <= 0:
        count = 0
        col = 0
        row = 0
        
    if (row<=0) & (col<=0):
        trace('null row and col')
        row = 0
        col = 0
    elif (col<0):    
        trace('fixed row')
        m = (int)(count % row)
        trace('m %d' % m)
        if m > 0: count += (row - m)
        col = (int)(count / row)
    elif (row<0): 
        trace('fixed col')
        m = (int)(count % col)
        if m > 0: count += (col - m)
        row = (int)(count / col)
    else:  
        trace('fixed col and row')    
        count = row * col;
        
    trace('count %d, col %d, row %d' % (count, col, row))
    return (count, col, row)

    
    
    
def getArange(start, count=-1, col=-1, row=-1):
    count, col, row = getModifCountColRow(count, col, row)    
    if row <= 0:
        return np.arange(start, start+count);
    else:
        return np.arange(start, start+count).reshape((row, col))
    

    
        
def sorted_by_value(inMap):
    return sorted(inMap.items(), key=operator.itemgetter(1))
        
    
from numpy.linalg import eigvals    
       
def run_experiment(niter=100):
    K=100
    results= []
    for _ in range(niter):
        mat = np.random.randn(K, K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results
    