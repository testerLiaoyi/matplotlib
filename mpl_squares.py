import matplotlib.pyplot as plt

input_valuse = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_valuse,squares,linewidth=2)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("x",fontsize=30)
plt.ylabel("y",fontsize=30)
#设置点
plt.scatter(input_valuse,squares,c=(0,0.4,0),s=100)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.axis([0,6,0,26])

plt.show()