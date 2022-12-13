from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

X,Y,Z = [2,4,6,8],[1,2,3,4],[3,6,9,12]

fig = plt.figure()

ax = fig.add_subplot(1,1,1,projection='3d')

#Use chart.plot instead of chart.plot_wireframe
ax.plot(X,Y,Z)

plt.show()
