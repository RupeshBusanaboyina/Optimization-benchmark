import numpy as np 
from optimizers import StupidGradientDescent
from functions import Rosenbrock


if__name =="__main__":
 #intialize the benchmark function object
 fr = Rosenbrock()
 #intialize optimization algorithm object
 #at position (3, 3) in parameter space
 gd = StupidGradientDescent(0.001, 3., 3., fr,grad)
 
 #numpy array for logging 
 log = np.zeros((BUDGET))
 
 for i in range(BUDGET)
	#Take a gradient step with constant alpha 
	gd.step()
	#
 
