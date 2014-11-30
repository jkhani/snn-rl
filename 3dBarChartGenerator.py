# from http://pythonprogramming.net/3d-bar-charts-python-matplotlib/
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pylab as pylab
 
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
 
#xpos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
xpos = np.ones(60)
xpos[15:30] *= 2
xpos[30:45] *= 3
xpos[45:60] *= 4
#ypos = [2,3,4,5,1,6,2,1,7,2]
ypos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

num_elements = len(xpos)
#zpos = [0,0,0,0,0,0,0,0,0,0]
zpos = np.zeros(60)
dx = np.ones(60)*.1
dy = np.ones(60)*.5
#dz = [1,2,3,4,5,6,7,8,9,10]
dz = [0.70106319, 0.00286898, 0.99854988, 0.00329543, 0.99749023, 0.00282395, 0.00237953, 0.29986343, 0.00294557, 0.00333794, 0.99891019, 0.00343499, 0.00283253, 0.70053738, 0.29950164,
0.30006903, 0.00455598, 0.99983094, 0.00402913, 0.99792467, 0.00310329, 0.00341758, 0.00273908, 0.70096318, 0.00440027, 0.99921323, 0.00441362, 0.00439755, 0.30008903, 0.70175336,
0.00433631, 0.00440846, 0.30120874, 0.00427499, 0.9998187, 0.7008399, 0.00359899, 0.70084357, 0.99970516, 0.0044827, 0.99950441, 0.70234639, 0.00449171, 0.00369084, 0.30203318,
0.00364221, 0.00362818, 0.63197624, 0.00505983, 0.9985362, 0.37257988, 0.00489438, 0.99985426, 0.3709176, 0.0038792, 0.99896611, 0.37106075, 0.00546044, 0.00523001, 0.63009559]
 
'''dz = [0.69165956, 0.618529, 0.79847699, 0.71046667, 0.57002514, 0.60882116, 0.51300664, 0.61922419, 0.63503936, 0.71963286, 0.87615812, 0.74055465,  0.61066999, 0.57829879, 0.54122366,
0.55243714, 0.98223234, 0.96355223, 0.86864663, 0.55257701, 0.6690428, 0.73680235, 0.59052183, 0.67009813, 0.94866078, 0.83037857, 0.95153942,  0.94807559, 0.55675044, 0.84045428,
0.93487134, 0.9504267, 0.79814978, 0.92165249, 0.9609133, 0.64352012, 0.7759134, 0.64431177, 0.9364345,  0.96643233, 0.89315432, 0.96830611, 0.9683759, 0.79571364, 0.97589131,
0.63603714, 0.63358592, 0.87223201, 0.88359407, 0.74437726, 0.92339993, 0.85470172, 0.97455033, 0.63311808, 0.67742265, 0.81945328, 0.658115, 0.95355213, 0.91331258, 0.54381546]'''

colors = ['r']*15+['g']*15+['b']*15+['y']*15

xLabel = ax1.set_xlabel('\nOutput Neuron', linespacing=1.2)
yLabel = ax1.set_ylabel('\nInput Neuron', linespacing=1.2)
zLabel = ax1.set_zlabel('\nWeight', linespacing=1.2)

neuron1 = plt.Rectangle((0, 0), 0.1, 0.1,fc='r')
neuron2 = plt.Rectangle((0, 0), 0.1, 0.1,fc='g')
neuron3 = plt.Rectangle((0, 0), 0.1, 0.1,fc='b')
neuron4 = plt.Rectangle((0, 0), 0.1, 0.1,fc='y')

ax1.legend((neuron1,neuron2,neuron3,neuron4),("neuron 1","neuron 2","neuron 3","neuron 4"),'best')

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.5)
ax1.view_init(elev=60.0, azim=40)

pylab.savefig('Weights3dBar.jpg')

plt.show()
