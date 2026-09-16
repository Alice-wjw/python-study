import os,sys,torch
sys.path.insert(0,os.path.dirname(__file__))
from data.loader import get_data
from model.net import FashionMLP
SAVE_PATH='checkpoints/model.pth'

def load_model(path):
    model=FashionMLP()
    model.load_state_dict(torch.load(path,weights_only=True))
    model.eval()
    return model
def predict(model,images):
    with torch.no_grad():
        return model(images).argmax(dim=1)
def main():
    if not os.path.exists(SAVE_PATH):
        print(f'未找到模型权重文件{SAVE_PATH}')

    model=load_model(SAVE_PATH)
    print('已加载')
    _,test_loader=get_data(batch_size=64)
    imgs,true_ibls=next(iter(test_loader))

    preds=predict(model,imgs[:5])
    for i in range(5):
        mark='yes'if preds[i].item()==true_ibls[i] else 'no'
        print(f'样本{i} |预测:{preds[i].item()} |真实:{true_ibls[i].item()} |是否正确:{mark}')
if __name__=='__main__':
    main()