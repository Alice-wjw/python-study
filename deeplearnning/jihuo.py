import  torch
import torch.nn as nn
import torch.nn.functional as F
z=torch.tensor([-3.0,-1.0,0.0,1.0,3.0])
print(f'原始输入z：{z.tolist()}')

sigmoid=nn.Sigmoid()
print(f'Sigmoid(z): {sigmoid(z).tolist()}')

tanh=nn.Tanh()
print(f'Tanh:{tanh(z).tolist()}')

relu=nn.ReLU()
print(f'REeLU(z):{relu(z).tolist()}')

softmax=nn.Softmax(dim=0)
print(f'Softmax(z):{softmax(z)}')
print(f'softmax(z)的sum:{softmax(z).sum().item()}')#。item，从单个元素的张量中取出里面的值转化成普通python数值
