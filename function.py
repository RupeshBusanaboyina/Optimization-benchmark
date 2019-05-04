# this is the functional curve for f= (a - x)^2 + b(y - x^2)^2


import numpy as np

	class Rosenbrock:

		def__init__(self , a=1., b-100.):
			self.a = a
			self.b = b

		def eval(self,x,y):

			return (self.a-x)** + self.b*(y-x**2)**2

		def grad(self , x, y):

			return np.array([-2,*(self.a-x),0


