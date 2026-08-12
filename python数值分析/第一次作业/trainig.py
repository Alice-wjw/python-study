import numpy as np
arr=np.array([[120,200,150,80,60],[90,255,180,75,40],[30,100,220,160,70],[50,140,190,210,95],[80,60,170,240,130]])
#创建灰度图像是对的
print('形状：',arr.dtype)
#形状不知道用什么，应该用shape
print('像素总数：',np.sum(arr))
#维度不知道是什么，维度应该是行数
# print('维度：',arr.dtype[0])
print('第一行元素',arr[:1])
print('第一列元素',arr[:,:1])
print('中心区域',arr[1:4,1:4])
print('变亮：',arr+30)
print('变暗：',arr*0.7)
print('反色：',255-arr)

#形状不会，维度不会，像素个数不会，切片不太会
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr[0])
print(arr[:,0])
bright=arr+30
bright=np.clip(bright,0,255)
print(bright)
#没有考虑变亮有范围
#没有考虑变暗要换类型
dark=arr*0.7
dark=dark.astype(int)
print(dark)