import torch.nn as nn
criterion=nn.MSELoss(reduction='mean')#本身只求了平方误差
loss=criterion(predictions,targets)
criterion=nn.BCELoss(reduction='mean')
loss=criterion(pred_probs,targets)
criterion=nn.CrossEntropyLoss(reduction='mean')
loss=criterion(logits,target_classes)
loss=criterion(pred,target)
loss.backward()
#计算所有张量的梯度，默认是覆盖的
#torch.optim.SGD
optimizer=optim.SGD(model.parameters(),lr=0.01)
optimizer.zero_frad()
loss.backward()
optimizer.step()
with torch.no_grad():
    pred=model(x)


