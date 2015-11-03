import numpy
import numpy as np
import get_array
from numpy import *



# Question #1

a= get_array(np.arange(1,16).reshape(3,5).T)

# Question 1a
new_array= concatenate((a[1],a[3]))
print 'Solution to Question 1a:', '\n', new_array


# Question 1b
return_col= a[:,1]
print 'Solution to Question 1b:', '\n', return_col

# Question 1c
rec_array = a[np.arange(1,4)]
print 'Solution to Question 1c:', '\n', rec_array

# Question 1d 
return_array_arange= sort(a[np.where(np.logical_and(a>3, a<11))])
print 'Solution to Question 1d:', '\n', return_array_arange

import numpy
import numpy as np
from numpy import *
import get_array


#Question 2
a=np.arange(25).reshape(5, 5)
b=np.array([1., 5, 10, 15, 20])
divide_array= np.divide(a.T,b).T



print 'Solution to Question 2:', '\n', divide_array
      

# Question 3      
         
array= get_array(np.random.rand(10,3))
new_array= np.argmin(abs(array-.5), axis=1).choose(array.T)
print  'Solution to 3a:' , '\n',  new_array



# Question 4

some_threshold=50

x,y=np.ogrid[-2:1:500j,-1.5:1.5:500j]

print('')
print('Grid set')
print('')

c=x + 1j*y
z=0

for g in range(50):
        print('Iteration number: ',g)
        z=z**2 + c

threshold = 50
mask=np.abs(z) < threshold

print('')
print('Plotting using imshow()')
plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])

print('')
print('plotting done')
print('')

plt.gray()

print('')
print('Preparing to render')
print('')

plt.show()











