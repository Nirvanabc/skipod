import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# xpos = [8, 64]
# ypos = [50, 100]
# zpos = [0, 0]

xpos = []
ypos = []
zpos = []
dz = []
f = open("results_bluegene.txt")
line = f.readline()
while line != '':
    thr, size, time = line.split()
    xpos.append(int(thr))
    ypos.append(int(size))
    zpos.append(0)
    dz.append(float(time))
    line = f.readline()
f.close()

dx = 1
dy = 200
# dz = [0.000448, 0.003049666666666667]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
ax.set_xlabel('threads')
ax.set_ylabel('matrix size')
ax.set_zlabel('time')
plt.show()
