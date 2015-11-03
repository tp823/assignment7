import numpy
import numpy as np
from numpy import *

class get_array(np.ndarray):
	'''Stores an numpy array into a subclass.'''
	def __new__(cls, array): 
		try: 
                	return array.view(cls)
                except AttributeError:
        		print 'Not a proper array. Must construt an array using numpy.'
