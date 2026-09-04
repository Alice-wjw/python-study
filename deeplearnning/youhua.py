import torch
import torch.nn as nn

x=torch.tensor([[1.0],[2.0],[3.0],[4.0]])
y=torch.tensor([[3.0],[5.0],[6.0],[9.0]])
#这个train的设计真好啊
def train(optimizer_name):
    torch.manual_seed(42)
    model=nn.Linear(1,1)
    criterion=nn.MSELoss()

    if optimizer_name=="SGD":
        optimizer=torch.optim.SGD(model.parameters(),lr=0.01)
    else:
        optimizer=torch.optim.Adam(model.parameters(),lr=0.1)
    print(f'{optimizer_name:12f} 初始参数：w={model.weight.item():4f}.b={model.bias.item():4f}')
    for epoch in range(1,101):
        pred=model(x)
        loss=criterion(pred,y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if epoch%10==0:
            print(f'epoch:{epoch},loss:{loss.item():4f}\n')
    return model

print(f'model.weight.requires_grad:{nn.Linear(1,1).weight.requires_grad}')
print(f'目标参数：w=2.0，b=1.0')

model_sgd=train('SGD')
model_adm=train('Adam')
print('9-4,学习项目')

