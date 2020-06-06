# 将常用的函数直接设置成常规可调用的方式

from IPython import display
import matplotlib.pyplot as plt
import torch
import torchvision
import torch.nn as nn
import zipfile

# 设置常规显示方式
def use_svg_display():
    display.set_matplotlib_formats("svg")

# 设置常规画图的大小
def set_figsize(figsize=(3.5,2.5)):
    use_svg_display()
    plt.rcParams["figure.figsize"]=figsize


# 将mnist 数据集的label进行映射
def get_fashion_mnist_labels(labels):
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat',
                   'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]

# mnist 数据集可视化
def show_fashion_mnist(images,labels):
    use_svg_display()
    _,figs=plt.subplots(1,len(images),figsize=(12,12))
    for f,img,label in zip(figs,images,labels):
        f.imshow(img.view(28,28).numpy())
        f.set_title(label)
        f.axes.get_xaxis().set_visible(False)
        f.axes.get_yaxis().set_visible(False)
    plt.show()

# mnist数据集导入
def load_data_fashion_mnist(batch_size,resize=None,num_workers=4,root="../data/FashionMNIST"):
    trans=[]
    if resize:
        trans.append(torchvision.transforms.Resize(size=resize))
    trans.append(torchvision.transforms.ToTensor())

    transform=torchvision.transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(root=root, train=True,
                                                    download=True, transform=transform)

    mnist_test = torchvision.datasets.FashionMNIST(root=root, train=False,
                                                   download=True, transform=transform)

    train_iter = torch.utils.data.DataLoader(mnist_train, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    test_iter = torch.utils.data.DataLoader(mnist_test, batch_size=batch_size, shuffle=True, num_workers=num_workers)

    return train_iter,test_iter

# 定义一个平展层
class FlattenLayer(nn.Module):
    def __init__(self):
        super(FlattenLayer,self).__init__()
    def forward(self,x):
        return x.view(x.shape[0],-1)

# 计算准确率
def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    net.eval()
    for X, y in data_iter:
        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
        n += y.shape[0]
    return acc_sum / n

def semilogy(x_vals, y_vals, x_label, y_label, x2_vals=None, y2_vals=None,
             legend=None, figsize=(3.5, 2.5)):
    set_figsize(figsize)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.semilogy(x_vals, y_vals)
    if x2_vals and y2_vals:
        plt.semilogy(x2_vals, y2_vals, linestyle=':')
        plt.legend(legend)

# 基本的卷积计算实现
def corr2d(X,K):
    """
    :param X: 输入的数组
    :param K: 核数组
    :return: 输出数组
    """
    h,w=K.shape
    Y=torch.zeros(size=(X.shape[0]-h+1,X.shape[1]-w+1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i,j]=(X[i:i+h,j:j+w]*K).sum()
    return Y

def load_data_jay_lyrics(file_path="../data/jaychou_lyrics.txt.zip"):
    with zipfile.ZipFile(file_path) as zin:
        with zin.open("jaychou_lyrics.txt") as f:
            corpus_chars = f.read().decode("utf-8")
    # 将换行符号替换成空格
    corpus_chars = corpus_chars.replace("\n", " ").replace("\r", " ")
    characters = list(set(corpus_chars))
    char2index = dict([(char, i) for i, char in enumerate(characters)])
    index2char = dict([(i, char) for i, char in enumerate(characters)])
    return corpus_chars,len(characters),char2index,index2char

# 梯度裁剪
def grad_clipping(params, theta, device):
    norm = torch.tensor([0.0], device=device)
    for param in params:
        norm += (param.grad.data ** 2).sum()
    norm = norm.sqrt().item()
    if norm > theta:
        for param in params:
            param.grad.data *= (theta / norm)