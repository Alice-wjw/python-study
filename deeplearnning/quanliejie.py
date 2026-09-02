import torch
import torch.nn as nn
from torch.nn import ReLU


class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet,self).__init__()
        self.fc1=nn.Linear(3,4)
        self.relu=ReLU()
        self.fc2=nn.Linear(4,2)
        self.sigmoid=nn.Sigmoid()

    def  forward(self,x):
        z1=self.fc1(x)
        a1=self.relu(z1)
        z2=self.fc2(a1)
        a2=self.sigmoid(z2)
        return z1,a1,z2,a2
torch.manual_seed(42)
model=SimpleNet()

print(f'model:{model}')
#查看网络结构
print('查看各层参数形状')
for name,param in model.named_parameters():
    print(f'{name:12s}->shape:{list(param.shape)}')
#model.named_parameters()是返回迭代器，每次返回一对：参数名字name，参数张量param
#参数名字一般是层的weight和bias
#12s,占12个字符宽度，左右对齐，输出对齐排版
   