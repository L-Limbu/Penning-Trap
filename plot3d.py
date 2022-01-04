import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

positions = np.load('./data/positions.npy')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def plot3d():
    Positions = positions
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    ax.plot(Positions[0], Positions[1], Positions[2])
    ax.set_xlabel('x (mm)')
    ax.set_ylabel('y (mm)')
    ax.set_zlabel('z (mm)')
    plt.savefig('./data/AtomTrap3D')
    plt.close()

plot3d()