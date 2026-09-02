import torch.nn as nn
import torch
sigmoid =nn.Sigmoid()
input1=torch.Tensor([1.0,2.0,3.0])
output=sigmoid(input1)
import torch
output2=torch.sigmoid(input1)
tanh=nn.Tanh()#(-1~1)
output3=tanh(input)
relu=nn.ReLU(inplace=False)
softmax=nn.Softmax(dim=1)


