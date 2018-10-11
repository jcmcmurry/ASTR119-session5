import numpy as np

x = 1.0
y = 2.0

#exponentials and logs
print(np.exp(x))        #e^x
print(np.log(x))        #ln(x)
print(np.log10(x))      #log(x)
print(np.log2(x))       #log_2(x)

#min/max/absolute value
print(np.fabs(x))       #absolute value as a float
print(np.fmin(x,y))     #min of x and y
print(np.fmax(x,y))     #max of x and y

n = 100
z = np.arange(n,dtype=float)
z *= 2.0*np.pi / float(n-1)     #
sin_z = np.sin(z)               #get an array sin(z)

#interpolation (approx. points between graph)
print(np.interp(0.75,z,sin_z))  #interpolates sin(0.75) from the sin_z function
print(np.sin(0.75))