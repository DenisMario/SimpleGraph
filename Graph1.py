import matplotlib.pyplot as plt

fig = plt.figure()

#fig.patch is used to change the background of the graph 
rect = fig.patch
rect.set_facecolor('orange')

x=[3,5,8,9,13]
y=[2,4,7,8,11]


#Instead of using "axisbg" use facecolor, it's used to change the graph's background color
graph1 = fig.add_subplot(2,1,1,facecolor='blue')
graph1.plot(x,y,'white',linewidth=4.0)


#".tick" is used to change the color or size of the ticks
graph1.tick_params(axis="x",color="purple")
graph1.tick_params(axis='y',color='purple')


#".spines" is used to change the color of the border inside the graph
graph1.spines["top"].set_color('y')
graph1.spines["left"].set_color('y')
graph1.spines["right"].set_color('y')
graph1.spines["bottom"].set_color('y')


#Giving the graph a name is done by ".set_title()" + #Giving the x and y axis names is done by "set_xlabel and set_ylabel"
graph1.set_title('Random Example',color='green')
graph1.set_xlabel('X-axis',color='red')
graph1.set_ylabel('Y-axis',color='pink')

plt.show()


