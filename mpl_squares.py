import matplotlib.pyplot as plt
from random_walk import RandomWalk
#input_valuse = [1,2,3,4,5]
# squares = [1,4,9,16,25]
# plt.plot(input_valuse,squares,linewidth=2)
#
# #设置图标标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("x",fontsize=30)
# plt.ylabel("y",fontsize=30)
# #设置点
# plt.scatter(input_valuse,squares,c=(0,0.4,0),s=100)
# #设置刻度标记的大小
# plt.tick_params(axis='both',labelsize=14)
#
# plt.axis([0,6,0,26])
#
# plt.savefig('squares_plot.png')
# plt.show()

rw = RandomWalk(50000)
point_numbers = list(range(rw.num_points))
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s = 1)
# plt.scatter(0,0,c='green',s=100)
# plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)
print(len(rw.y_values))
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()