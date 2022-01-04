import matplotlib.pyplot  as plt
from matplotlib.animation import FuncAnimation

import numpy as np

data = np.load('./data/positions.npy')
Positions = data[(0,1),:]

figure, ax = plt.subplots()
figure.set_size_inches(9, 6)
# Setting label and limit for x and y axis

ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')

x = 2
y = 1.5
ax.set_xlim(-x, x)
ax.set_ylim(-y, y)

A, = ax.plot(0, 0, '.-', color='blue')

def animation_function(i):
    j=60
    while i<Positions[0].shape[0]/j:
        A.set_data(Positions[0,::j][i], Positions[1,::j][i])
        return 
  
animation = FuncAnimation(figure,func = animation_function,interval = 10)

plt.show()
plt.close()


