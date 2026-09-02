import torch
import torch.nn as nn
class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()#super子类，实例
        self.fc1=nn.Linear(2,3)
        self.re=nn.ReLU()
        self.fc2=nn.Linear(3,1)
        self.sigmoid=nn.Sigmoid()
        self.fc1.weight=nn.Parameter(torch.tensor([
            [0.5,0.6],
            [0.8,0.7],
            [-0.3,-0.4]
        ]))
        self.fc1.bias=nn.Parameter(torch.tensor([0.1,-0.2,0.3]))
        self.fc2.weight=nn.Parameter(torch.tensor([[0.6,-0.5,0.9]]))
        self.fc2.bias=nn.Parameter(torch.tensor([0.2]))
    def forward(self,x):
        a1=self.fc1(x)
        z1=self.re(a1)
        a2=self.fc2(z1)
        z2=self.sigmoid(a2)
        return z2
x=torch.tensor([0.9,0.8])
model=Net()
print(f'{model}')
print(f'{model(x)}')

