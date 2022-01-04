from matplotlib import lines, pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

data = np.load('./data/positions.npy')
Positions = data[(0,2),:]

figure, ax = plt.subplots()
figure.set_size_inches(9, 6)

# Setting limits for x and y axis
x = 1.6
y = 1.1
ax.set_xlim(-x, x)
ax.set_ylim(-y, y)

#Setting label for axis
ax.set_xlabel('x (mm)')
ax.set_ylabel('z (mm)')

A, = ax.plot(0, 0, '.-', color='blue')

def animation_function(i):
    j=60
    while i<Positions[0].shape[0]/j:
        A.set_data(Positions[0,::j][i], Positions[1,::j][i])
        return 
  
animation = FuncAnimation(figure,func = animation_function,interval = 10)
plt.show()
plt.close()