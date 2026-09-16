import os,sys,torch
sys.path.insert(0,os.path.dirname(__file__))
from data.loader import get_data
from model.net import FashionMLP
import torch.nn as nn
import matplotlib.pyplot as plt
#导入部分
######################################
#超参数
EPOCHS=20
LR=1e-3
BATCH_SIZE=64
SAVE_PATH='checkpoints/model.pth'
import sys
# for p in sys.path:
#     print(p)
######################################
#评估函数
#
def evaluate(model,loader):
    model.eval()
    correct=total=0
    with torch.no_grad():
        for imgs,lbls in loader:
            out=model(imgs)#这里只是logits
            pred=out.argmax(dim=1)#logit里取概率最大的
            correct+=(pred==lbls).sum().item()#
            total+=lbls.size(0)
    return correct/total

def main():
    torch.manual_seed(42)
    train_loader,test_loader=get_data(BATCH_SIZE)
    model = FashionMLP()
    #定义损失·
    criterion=nn.CrossEntropyLoss()
    #定义优化
    optimizer=torch.optim.Adam(model.parameters(),lr=LR)
    print(f'模型参数量：{sum(p.numel() for p in model.parameters()):,}')
    print('训练过程')
    for epoch in range(1,EPOCHS+1):
        model.train()
        total_loss=0.0
        for imgs,lbls in train_loader:
            optimizer.zero_grad()
            loss=criterion(model(imgs),lbls)
            loss.backward()
            optimizer.step()
            total_loss+=loss.item()
        print(f'Epoch{epoch}/{EPOCHS} 平均loss：{total_loss/len(train_loader):4f}')

        acc=evaluate(model,test_loader)
        print(f'测试集准确率：{acc*100:2f}%')

        os.makedirs(os.path.dirname(SAVE_PATH),exist_ok=True)
        torch.save(model.state_dict(),SAVE_PATH)
        print(f'权重已经保存至：{SAVE_PATH}')

if __name__=='__main__':
    main()

