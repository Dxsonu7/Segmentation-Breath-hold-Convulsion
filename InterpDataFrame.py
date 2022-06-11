
"""
Created on Sat Jun 11 15:00:19 2022

@author: Sonu Gupta
"""

#imports
import numpy
import pandas as pd
import matplotlib.pyplot as plt

####I am creating similar sequence function like in R
def seq(start, end, by = None, length_out = None):
    len_provided = True if (length_out is not None) else False
    by_provided = True if (by is not None) else False
    if (not by_provided) & (not len_provided):
        raise ValueError('At least by or n_points must be provided')
    width = end - start
    eps = pow(10.0, -14)
    if by_provided:
        if (abs(by) < eps):
            raise ValueError('by must be non-zero.')
    #Switch direction in case in start and end seems to have been switched (use sign of by to decide this behaviour)
        if start > end and by > 0:
            e = start
            start = end
            end = e
        elif start < end and by < 0:
            e = end
            end = start
            start = e
        absby = abs(by)
        if absby - width < eps:
            length_out = int(width / absby)
        else:
            #by is too great, we assume by is actually length_out
            length_out = int(by)
            by = width / (by - 1)
    else:
        length_out = int(length_out)
        by = width / (length_out - 1)
    out = [float(start)]*length_out
    for i in range(1, length_out):
        out[i] += by * i
    if abs(start + by * length_out - end) < eps:
        out.append(end)
    return out

        ####reading data now
dat = pd.read_csv (r'C:\Users\sonu7\Desktop\testpy.csv')
#plt.plot(data)

          ####columns from Data:
A = 283.44
B = 267.617
C = 245.427
D = 244.023
E = 214.651
F = 316.48
G = 391.768
H = 485.182 

####segmenting the data according to our need
#start is range of index of starting row and ending 
#the second parament in dat.loc is column name - here it is 485.182. 
start = 160000
end = 224560          
y = dat.loc[start:end,'485.182']



#### sequence for interpolation
# we are creating certain range of datato match the length with our collected data - so we can finally start time normalization
#since in interp function - length of x and y must be equal so we are choosing certain data to maintain the length
#seq(1,10000) suggests it will maintain the data points within 1-10000 range!
length = 64561        
x = seq(1, 10000, length_out=length)



####using Numpy.interp
#finally I am interpolating the data - keeping the data points between 1-10000 range and the length of the data will be 10,000
#x and y are the same length - so this function can run smoothly
#and finally we will map/plot the interpolated data using plt.plot
d= numpy.interp(seq(1, 10000, length_out=10000), x, y)
plt.plot(d)