import numpy as np 
from optimizers import StupidGradientDescent
from function import Rosenbrock

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')

BUDGET = 1000

if __name__ =="__main__":
 #intialize the benchmark function object
 fr = Rosenbrock()
 #this is making sure it is deterministic randomness
 np.random.seed(seed=42)
 #intialize optimization algorithm object
 initstate = 10*(np.random.rand(2,1)-1)[:, 0]
 gd = StupidGradientDescent(0.001, initstate, fr.grad)
 
 #numpy array for logging 
 performance = np.zeros((BUDGET,))
 
 for i in range(BUDGET):
	#Take a gradient step with constant alpha 
       gd.step()
	#save f value 
       performance[i] = fr.eval(gd.state[0], gd.state[1])

 plt.plot(np.log10(performance))
 plt.show() 
