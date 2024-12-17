import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(1, 11)
y = 6*x+2+x+1

plt.plot(x,y)
plt.show()