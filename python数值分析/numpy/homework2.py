import numpy as np
s=np.array([
    [120,200,150,80,60],
    [90,255,180,75,40],
    [30,100,220,160,70],
    [50,140,190,210,95],
    [80,60,170,240,130]
])

# 1. 输出图像的：平均亮度、最亮像素值、最暗像素值
print('平均亮度：',np.mean(s))
print('最亮像素值：',np.max(s))
print('最暗像素值：',np.min(s))
# 2. 完成图像像素筛选：
# - 找出所有高亮像素（>200）
print(s>200)
print('高亮元素',s[s>200])
# - 统计高亮像素数量
print(s[s>200].size)
# - 找出所有较暗像素（<50）
print('较暗元素',s[s<50])
# 3. 完成图像统计分析：
# - 计算每一行平均亮度
print(np.mean(s,axis=1))
# - 计算每一列平均亮度
print(np.mean(s,axis=0))
# - 找出最亮的一行
a=np.sum(s,axis=1)
b=np.argmax(a)
print(s[b])
# - 找出最暗的一列
a=np.sum(s,axis=0)
b=np.argmin(a)
print(s.T[b])
# 4. 完成图像排序分析：
# - 对所有像素进行升序排序
print(np.sort(s,axis=None))
# - 输出最亮的5个像素
print(np.sort(s,axis=None)[:-6:-1])
# 提示：
# np.sort()
# np.argmax()
# np.argmin()
# 提高挑战（选做）
# 尝试使用 np.where() 实现图像二值化：
# - 像素 >= 128 → 255
# - 像素 < 128 → 0
print(np.where(s>=128,'255','0'))
#找位置，判断，重新赋值