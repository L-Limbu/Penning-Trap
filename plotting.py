import numpy as np
import matplotlib.pyplot as plt


positions = np.load('./data/positions.npy')


def plotxy():
    Positions = positions[(0,1),:]
    plt.plot(Positions[0], Positions[1])

    plt.ylabel('y (mm)')
    plt.xlabel('x (mm)')
    plt.ylim(-1.6, 1.6)

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



plotxy()
plotxz()

