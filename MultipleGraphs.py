import matplotlib.pyplot as plt
fig = plt.figure()
rect = fig.patch
rect.set_facecolor('gray')


#plotting multiple points 
x=[3,6,5,8,9,12]
y=[2,4,5,7,9,11]
x2=[3,5,8,3]
y2=[6,8,10,6]
x3=[3,15,7]
y3=[2,17,8]

#Making multiple graphs 
graph1 = fig.add_subplot(2,1,1,facecolor='blue')
graph1.plot(x,y,'white',linewidth=4.0)
graph1.plot(x2,y2,'red',linewidth=6.0)
graph1.plot(x3,y3,'yellow',linewidth=5.0)


graph1.tick_params(axis="x",color="purple")
graph1.tick_params(axis='y',color='purple')
graph1.spines["top"].set_color('y')
graph1.spines["left"].set_color('y')
graph1.spines["right"].set_color('y')
graph1.spines["bottom"].set_color('y')
graph1.set_title('Multiple Graphs Example',color='purple')
graph1.set_xlabel('X-axis',color='red')
graph1.set_ylabel('Y-axis',color='pink')

plt.show()
            
