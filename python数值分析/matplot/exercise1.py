import matplotlib.pyplot as plt
import numpy as np
# x=np.arange(10)
# y=x**2

plt.rcParams['font.sans-serif']=['Microsoft Yahei']
plt.rcParams['axes.unicode_minus']=False
###
# plt.plot(x,y,color='r',linestyle='--')
# plt.title('基础图',fontsize=12)
# plt.xlabel('x轴(0-9)',fontsize=10)
# plt.ylabel('y轴(x的立方)',fontsize=10)
# plt.show()
# x=np.arange(5)
# categories=['类别A','类别B','类别C','类别D','类别E']
# height=[12,25,18,30,22]
# plt.bar(x,height,width=0.6,color='skyblue',edgecolor='black')
# plt.xticks(x,categories)

# plt.title('柱形图',fontsize=20)
# plt.xlabel('类别',fontsize=10)
# plt.ylabel('数值',fontsize=10)
# plt.show()
###
x=np.arange(10)
y=x**2
fig=plt.figure(figsize=(8,4))
ax=fig.add_subplot(1,1,1)
ax.plot(x,y,color='purple',linestyle='-')
ax.set_title('面向对象')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True,alpha=0.3)
plt.show()