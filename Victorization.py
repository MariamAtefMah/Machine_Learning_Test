import numpy as np

w = np.array([[0.5, 1.3, 3.3], [3.2, 3, 4]]) #2 rows and 3 coloumns.
d = np.array([0.3, 0.2, 0.4])

w = w-0.1*d
print(d.shape) #it will print the number of rows and coloumns.
print(w) #will print solution of last equation.