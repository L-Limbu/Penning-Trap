import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

from animation import Positions
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

positions = np.load('./data/positions.npy')

def plotxy():
    Positions = positions[(0,1),:]
    plt.plot(Positions[0], Positions[1])

    plt.ylabel('y (mm)')
    plt.xlabel('x (mm)')


    plt.savefig('./data/AtomTrap')
    plt.close()

def plotxz():
    Positions = positions[(0,2),:]
    plt.plot(Positions[0], Positions[1])

    plt.ylabel('z (mm)')
    plt.xlabel('x (mm)')
    plt.ylim(-1.2, 1.2)

    plt.savefig('./data/AtomTrapXZ')
    plt.close()

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

plotxy()
plotxz()
plot3d()
