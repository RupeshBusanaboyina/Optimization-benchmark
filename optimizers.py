"""This is a module containing optimizers."""


import numpy as np

class StupidGradientDescent:

	def __init__(self ,alpha , x0 . y0 , fgrad):

		self.state = np.array([x0 , y0])
		self.alpha = alpha
		self.fgrad = fgrad

 


