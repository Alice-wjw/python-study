import torch#主包，提供基础数据结构
import torch.nn as nn#神经网络模块，提供现成的组件
import numpy as np
a=np.array([1.0,2.0,3.0])
t=torch.tensor([1,2,3])
print(a)
print(t)
print (t.shape)

scaler=torch.tensor(2)
vector=torch.tensor([1.0,2.0,3.0])
matrix=torch.tensor([[1,2,3],[4,5,6]])
print(scaler.shape,vector.shape,matrix.shape )
torch.manual_seed(42)
neuron=nn.Linear(in_features=3,out_features=1)
print(neuron.weight.data)
print(neuron.bias.data)
z=neuron(vector)
print(z.data)
print(0.4414+0.4792*2-0.1353*3+0.5304)
print(vector@neuron.weight.data.T+neuron.bias.data)
fc_layer=nn.Linear(in_features=3,out_features=4)
out=fc_layer(vector)
print(out)

