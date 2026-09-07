#torchvision.datasets.MNIST
#trainsforms.ToTensor,transforms.Normalize,reansforms.Compose原始图片转化为标准张量
#torch.utils.data.DataLooader包装成可迭代的批次流
#nn.Sequential把多个层按顺序串联成一个完整的模型
# #nn.Flatten多维向量展开为一维向量
#
# # model.state_dict()
#
# # torch.save(),torch.load,model.load_state_dict()
# import torchvision
# import torchvision.transforms as transforms
# transform=transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Normalize((0.1307,),(0.3081,))
# ])
# train_dataset=torchvision.datasets.MNIST(
#     root='./data',
#     train =True,
#     download=True,
#     transform=transform
# )
# test_dataset=torchvision.datasets.MNIST(
#     root='./data',
#     train=False,
#     download=True,
#     transform=transform
# )
# from torch.utils.data import DataLoader
# train_loader=DataLoader(train_dataset,batch_size=64,shuffle=True)
# test_loader=DataLoader(test_dataset,batch_size=64,shuffle=False)
# for images,labels in train_loader:
#
# # import torch.nn as nn
# # model=nn.Sequential(
#     nn.Flatten(),
#     nn.Linear(784,256),
#     nn.ReLU(),
#     nn.Linear(256,128),
#     nn.ReLU(),
#     nn.Linear(128,10)
# )
#
# output=model(input_tensor)
# import torch
# torch.save(model.state_dict(),'checkpoints/minist_model.pth')
# model=MNISTNet()
# state=torch.load('checkpoints/minist_model.pth',weights_only=True)
# model.load_state_dict(state)
# model.eval()
