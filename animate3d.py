import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

import mpl_toolkits.mplot3d.axes3d as p3


ion = 'caesium'
am = 55





position_xyz = np.load('./data/positions.npy')
position_xy = position_xyz[0:2]
position_z = position_xyz[2]
numFrames = len(position_xyz[2])

fig = plt.figure()
fig.set_size_inches(9, 6)
ax = p3.Axes3D(fig)
fig.add_axes(ax)

ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
ax.set_zlabel('z (mm)')
ax.set_title('3D trajectory of %s ion in a penning trap'%ion)

x = y = 1.5
z = 1
ax.set_xlim(-x,x)
ax.set_ylim(-y,y)
ax.set_zlim(-z,z)

line = plt.plot(0, 0, 0, '.-' ,c='blue')[0]

def animation_function (time):
    j=50
    positions = position_xyz[(0,1,2),::j]
    while time <positions[0].shape[0]:
        line.set_data(positions[(0,1), :time])   
        line.set_3d_properties(positions[2,:time]) 
        
        return line

ani = FuncAnimation(fig, func=animation_function, interval=5, blit=False)

plt.show()
plt.close()

print(position_xyz[0:2, :2].shape)