import matplotlib.pyplot as plot
import math
import numpy as np
x = np.arange(0,5,0.1)
line, = plot.plot(x,np.sin(x))
plot.scatter(x,x,c= "red")
plot.scatter(x,x*x)
plot.show()