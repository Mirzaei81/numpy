import numpy as np
import timeit 

def nump():
    arr = np.arange(1000)
    mask = np.logical_or(arr%3==0,arr%5==0)
    sum(arr[mask])

def aristadel():
    sum=0
    for i in range(1000):
        if(i%3==0 or i%5==0):
            sum+=i
aristadel()
nump()
print(f"Completed nump Execution in {timeit.Timer(nump).timeit(1000)} seconds")    
print(f"Completed aristadel Execution in {timeit.Timer(aristadel).timeit(1000)} seconds")    
