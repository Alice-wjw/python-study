import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader,TensorDataset
import torchvision
import torchvision.transforms as transforms

def get_dataloaders(batch_size):
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_ds=torchvision.datasets.MNIST(
        './data/raw',
        train=True,
        download=True,
        transform=transform
    )
    test_ds=torchvision.datasets.MNIST(
        './data/raw',
        train=False,
        download=True,
        transform=transform
    )
    print('数据来源：MNIST(torchvision)')
    train_loader=DataLoader(train_ds,
                            batch_size=batch_size,
                            shuffle=True,
                            )
    test_loader=DataLoader(test_ds,batch_size=batch_size,shuffle=False)
    return train_loader,test_loader