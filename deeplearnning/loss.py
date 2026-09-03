import torch.nn as nn
criterion=nn.MSELoss(reduction='mean')#本身只求了平方误差
loss=criterion(predictions,targets)
criterion=nn.BCELoss(reduction='mean')
loss=criterion(pred_probs,targets)
criterion=nn.CrossEntropyLoss(reduction='mean')
loss=criterion(logits,target_classes)
