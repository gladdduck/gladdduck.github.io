---
title: 详解PyTorch中加载数据的方法--Dataset、Dataloader、Sampler、collate-fn
categories:
  - 学习笔记
tags:
  - Dataset
  - Dataloader
  - Sampler
  - collate_fn
toc: true# 是否启用内容索引
---

[转载](https://www.jianshu.com/p/1651ed9d48c9)
[作者pytorch其他笔记](https://www.jianshu.com/nb/48831659)

数据读取是所有训练模型任务中最基础最重要的一步，`PyTorch`为数据集的读取、加载和使用提供了很好的机制，使得数据加载的工作变得异常简单而且具有非常高的定制性。

## Dataset、Dataloader、Sampler的关系

`PyTorch`中对于数据集的处理有三个非常重要的类：`Dataset`、`Dataloader`、`Sampler`，它们均是 `torch.utils.data `包下的模块（类）。它们的关系可以这样理解：

- `Dataset`是数据集的类，主要用于定义数据集
- `Sampler`是采样器的类，用于定义从数据集中选出数据的规则，比如是随机取数据还是按照顺序取等等
- `Dataloader`是数据的加载类，它是对于 `Dataset`和 `Sampler`的进一步包装，即其实 `Dataset`和 `Sampler`会作为参数传递给 `Dataloader`，用于实际读取数据，可以理解为它是这个工作的真正实践者，而 `Dataset`和 `Sampler`则负责定义。我们训练、测试所获得的数据也是 `Dataloader`直接给我们的。

**总的来说**，Dataset定义了整个数据集，`Sampler`提供了取数据的机制，最后由 `Dataloader`取完成取数据的任务。

本篇以一个最简单的例子为例，比如有一个文件夹（`data-folder`）中存储训练的数据（一共30张图片：0.png 到 29.png），他们对应的标签被写在了一个 `labels.txt`文件中，第n行对应n-1.png的标签，是一个三分类问题，即0、1和2三种标签（虚构的数据集，不具有任何意义）。目录结构如下：

```bash
|--- Project
   |--- main.py
   |--- labels.txt
   |--- data-folder
      |--- 0.png
      |--- 1.png
      |--- ……
      |--- 29.png
```

## Dataset

`Dataset` 位于 `torch.utils.data `下，我们通过定义继承自这个类的子类来自定义数据集。它有两个最重要的方法需要重写，实际上它们都是类的特殊方法：

- `__getitem__(self, index)`：传入参数 `index`为下标，返回数据集中对应下标的数据组（数据和标签）
- `__len__(self)`：返回数据集的大小

简单说，重写了这两个方法的继承自 `Dataset` 的类都可以作为数据集的定义类使用，即一个 `Dataset`类的必要结构：

```python
class Dataset(torch.utils.data.Dataset):
    def __init__(self, filepath=None,dataLen=None):
        pass
      
    def __getitem__(self, index):
        pass

    def __len__(self):
        pass
```

如下就是我们的例子的加载实例，其中的 `image2tensor` 使用了 `torchvision.transforms` 完成了一个简单的从 `PIL.Image` 格式的图片到 `tensor` 的转换，可以先不必在意，后面会详细地讲到 `transforms` 这个超级重要的工具：

```python
from torch.utils.data import Dataset
from PIL import Image
import os
from torchvision import transforms


class MyDataset(Dataset):
    def __init__(self, images_folder_path, labels_file_path):
        self.images_folder_path = images_folder_path

        with open(labels_file_path, 'r') as file:
            self.labels = list(map(int, file.read().splitlines()))

    def __getitem__(self, item):
        image = Image.open(os.path.join(self.images_folder_path, "{}.png".format(item)))
        image = self.image2tensor(image)
        label = self.labels[item]

        return (image, label)

    def __len__(self):
        return len(self.labels)

    def image2tensor(self, image):
        """
        transform PIL.Image to tensor
        :param image: image in PIL.Image format
        :return: image in tensor format
        """
        transform = transforms.Compose([
            transforms.ToTensor()
        ])
        image = image.convert('RGB')
        return transform(image)


myDataset = MyDataset("./data-folder/", "./labels.txt")
```

## Dataloader

`Dataloader`对 `Dataset`（和 `Sampler`等）打包，完成最后对数据的读取的执行工作，一般不需要自己定义或者重写一个 `Dataloader`的类（或子类），直接使用即可，通过传入参数定制 `Dataloader`，定制化的功能应该在 `Dataset`（和 `Sampler`等）中完成了。

`Dataloader`的完整签名：
[https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader)

### Dataloader的一些常用参数

`Dataloader`的一些重要的参数如下，除了第一个 `dataset`参数外，其他均为可选参数：

- `dataset`（第一个参数，必须的参数）：一个 `Dataset`的实例，即传入的数据集（或者其他可迭代对象）
- `batch_size`：整数值，每个 `batch`的样本数量，即 `batch`大小，默认为1
- `shuffle：bool`值，如果设置为 `True`，则在每个 `epoch`开始的时候，会对数据集的数据进行重新排序，默认 `False`
- `sampler`：传入一个自定义的 `Sampler`实例，定义从数据集中取样本的策略，`Sampler`每次返回一个索引，默认为 `None`
- `batch_sampler`：也是传入一个自定义的 `Sampler`实例，但是与 `sampler`参数不同的是，它接收的 `Sampler`是一次返回一个 batch的索引，默认为 `None`
- `num_workers`：整数值，定义有几个进程来处理数据。0意味着所有的数据都会被加载进主进程，默认0
- `collate_fn`：传入一个函数，它的作用是将一个 `batch`的样本打包成一个大的 `tensor`，`tensor`的第一维就是这些样本，如果没有特殊需求可以保持默认即可（后边会详细介绍）
- `pin_memory：bool`值，如果为 `True`，那么将加载的数据拷贝到 `CUDA`中的固定内存中。
- `drop_last：bool`值，如果为 `True`，则对最后的一个 `batch`来说，如果不足 `batch_size`个样本了就舍弃，如果为 `False`，也会继续正常执行，只是最后的一个 `batch`可能会小一点（剩多少算多少），默认 `False`
- `timeout`：如果是正数，表明等待从加载一个 `batch`等待的时间，若超出设定的时间还没有加载完，就放弃这个 `batch`，如果是0，表示不设置限制时间。默认为0

### Dataloader参数之间的互斥

值得注意的是，`Dataloader`的参数之间存在互斥的情况，主要针对自己定义的采样器：

- `sampler`：如果自行指定了 `sampler`参数，则 `shuffle`必须保持默认值，即 `False`
- `batch_sampler`：如果自行指定了 `batch_sampler`参数，则 `batch_size`、`shuffle`、`sampler`、`drop_last` 都必须保持默认值
  如果没有指定自己是采样器，那么默认的情况下（即 `sampler`和 `batch_sampler`均为 `None`的情况下），`Dataloader`的采样策略是如何的呢：
- `sampler`：
- - `shuffle = True`：`sampler`采用 `RandomSampler`，即随机采样
- - `shuffle = Flase`：`sampler`采用 `SequentialSampler`，即按照顺序采样
- `batch_sampler`：采用 `BatchSampler`，即根据 `batch_size` 进行 `batch`采样
- 

上面提到的 `RandomSampler`、`SequentialSampler`和 `BatchSampler`都是 `PyTorch`自己实现的，且它们都是 `Sampler`的子类，后边会详述。

### Dataloader的实例

下面我们继续我们的例子，定义 `Dataloader`的实例，从我们定义的 `myDataset` 数据集中加载数据，每一个 `batch`大小为8。并且我们使用了一个循环来验证其工作的情况：

```python
from torch.utils.data import DataLoader

myDataloader = DataLoader(myDataset, batch_size=8)

for epoch in range(2):
    for data in myDataloader:
        images, labels = data[0], data[1]
        print(len(images))
        print(labels)
        # train your module
```

```python
8
tensor([0, 1, 1, 1, 2, 0, 1, 2])
8
tensor([0, 2, 1, 1, 1, 1, 2, 0])
8
tensor([1, 0, 0, 0, 0, 1, 1, 0])
6
tensor([2, 0, 1, 1, 1, 2])
8
tensor([0, 1, 1, 1, 2, 0, 1, 2])
8
tensor([0, 2, 1, 1, 1, 1, 2, 0])
8
tensor([1, 0, 0, 0, 0, 1, 1, 0])
6
tensor([2, 0, 1, 1, 1, 2])
```

## Sampler

`Sampler`类是一个很抽象的父类，其主要用于设置从一个序列中返回样本的规则，即采样的规则。`Sampler`是一个可迭代对象，使用 `step`方法可以返回下一个迭代后的结果，因此其主要的类方法就是 `__iter__ `方法，定义了迭代后返回的内容。其父类的代码如下（`PyTorch 1.7`）：

```python

class Sampler(Generic[T_co]):
    def __init__(self, data_source: Optional[Sized]) -> None:
        pass

    def __iter__(self) -> Iterator[T_co]:
        raise NotImplementedError
```

从上述代码可见，其实 `Sampler`父类并没有给出 `__iter__` 的具体定义，因此，如果我们要定义自己的采样器，就要编写继承自 `Sampler`的子类，并且重写 `__iter__ `方法给出迭代返回样本的逻辑。

但是，正如上文提到的，`Dataloader`中的 `sampler`和 `batch_sampler`参数默认情况下使用的那些采样器（`RandomSampler`、`SequentialSampler`和 `BatchSampler`）一样，`PyTorch`自己实现了很多 `Sampler`的子类，这些采样器其实可以完成大部分功能，所以本节主要关注一些 `Sampler`的子类以及他们的用法，而不过多地讨论如何自己实现一个 `Sampler`。

### SequentialSampler

`SequentialSampler`就是一个按照顺序进行采样的采样器，接收一个数据集做参数（实际上任何可迭代对象都可），按照顺序对其进行采样：

```python
from torch.utils.data import SequentialSampler

pseudo_dataset = list(range(10))
for data in SequentialSampler(pseudo_dataset):
    print(data, end=" ")

0 1 2 3 4 5 6 7 8 9 
```

### RandmSampler

`RandomSampler` 即一个随机采样器，返回随机采样的值，第一个参数依然是一个数据集（或可迭代对象）。还有一组参数如下：

- `replacement：bool`值，默认是 `False`，设置为 `True`时表示可以采出重复的样本
- `num_samples`：只有在 `replacement`设置为 `True`的时候才能设置此参数，表示要采出样本的个数，默认为数据集的总长度。有时候由于 `replacement`置 `True`的原因导致重复数据被采样，导致有些数据被采不到，所以往往会设置一个比较大的值

```python
from torch.utils.data import RandomSampler

pseudo_dataset = list(range(10))

randomSampler1 = RandomSampler(pseudo_dataset)
randomSampler2 = RandomSampler(pseudo_dataset, replacement=True, num_samples=20)

print("for random sampler #1: ")
for data in randomSampler1:
    print(data, end=" ")

print("\n\nfor random sampler #2: ")
for data in randomSampler2:
    print(data, end=" ")

for random sampler #1: 
4 5 2 9 3 0 6 8 7 1 

for random sampler #2: 
4 9 0 6 9 3 1 6 1 8 5 0 2 7 2 8 6 4 0 6 
```

### SubsetRandomSampler

SubsetRandomSampler 可以设置子集的随机采样，多用于将数据集分成多个集合，比如训练集和验证集的时候使用：

```python
from torch.utils.data import SubsetRandomSampler

pseudo_dataset = list(range(10))

subRandomSampler1 = SubsetRandomSampler(pseudo_dataset[:7])
subRandomSampler2 = SubsetRandomSampler(pseudo_dataset[7:])

print("for subset random sampler #1: ")
for data in subRandomSampler1:
    print(data, end=" ")

print("\n\nfor subset random sampler #2: ")
for data in subRandomSampler2:
    print(data, end=" ")
for subset random sampler #1: 
0 4 6 5 3 2 1 

for subset random sampler #2: 
7 8 9 
```

### WeightedRandomSampler

`WeightedRandomSampler`和 `RandomSampler`的参数一致，但是不在传入一个 `dataset`，第一个参数变成了 `weights`，只接收一个一定长度的 `list`作为 `weights` 参数，表示采样的权重，采样时会根据权重随机从 `list(range(len(weights)))` 中采样，即 `WeightedRandomSampler`并不需要传入样本集，而是只在一个根据 `weights`长度创建的数组中采样，所以采样的结果可能需要进一步处理才能使用。`weights`的所有元素之和不需要为1。

```python
from torch.utils.data import WeightedRandomSampler

pseudo_dataset = list(range(10))
weights = [1,1,1,1,1,10,10,10,10,10]

weightedRandomSampler = WeightedRandomSampler(weights, replacement=True, num_samples=20)

for data in weightedRandomSampler:
    print(data, end=" ")
7 8 7 7 9 7 8 9 8 7 5 5 9 9 6 5 8 9 6 5 
```

### BatchSampler

以上的四个 `Sampler`在每次迭代都只返回一个索引，而 `BatchSampler`的作用是对上述这类返回一个索引的采样器进行包装，按照设定的 `batch_size`返回一组索引，因其他的参数和上述的有些不同：

- `sampler`：一个 `Sampler`对象（或者一个可迭代对象）
- `batch_size`：batch的大小
- `drop_last`：是否丢弃最后一个可能不足 `batch_size`大小的数据

```python
from torch.utils.data import BatchSampler
pseudo_dataset = list(range(10))

batchSampler1 = BatchSampler(pseudo_dataset, batch_size=3, drop_last=False)
batchSampler2 = BatchSampler(pseudo_dataset, batch_size=3, drop_last=True)

print("for batch sampler #1: ")
for data in batchSampler1:
    print(data, end=" ")

print("\n\nfor batch sampler #2: ")
for data in batchSampler2:
    print(data, end=" ")
for batch sampler #1: 
[0, 1, 2] [3, 4, 5] [6, 7, 8] [9] 

for batch sampler #2: 
[0, 1, 2] [3, 4, 5] [6, 7, 8] 
```

## collate_fn

`Dataloader`其实还有一个比较重要的参数是 `collate_fn`，它接收一个 `callable`对象，比如一个函数，它的作用是将每次迭代出来的数据打包成 `batch`。

举个例子，如果我们在 `Dataloader`中设置了 `batch_size`为8，实际上，从 `Dataloader`所读取的数据集Dataset中取出数据时得到的是单独的数据，比如我们的例子中，每次采样得到一个 `tuple：(image, label)`，因此 `collate_fn` 的作用就有了，它负责包装 `batch`，即每从数据集中抽出8个这样的 `tuple`，它负责把8个 `(image, label)`包装成一个 `list: [images, labels]`，这个 `list`有两个元素，每一个是一个 `tensor`，比如第一个元素，实际上是一个 `8×size(image)` 的tensor，即给原来的数据增加了一维，也就是最前边的 `batch`的维度，`labels`也同理。

有时候我们可能会需要实现自己的包装逻辑，所以需要自定义一个函数来完成定制化的如上的内容，只要将该函数名传递给 `collate_fn`参数即可。

## PyTorch集成的数据集

实际上，`PyTorch`提供了很多常用数据集的接口，如果使用这些数据集的话，可以直接使用对应的包加载，会方便很多，比如：

- `torchvision.datasets` 就提供了很多视觉方向的数据集：https://pytorch.org/docs/stable/torchvision/datasets.html?highlight=torchvision%20datasets
- `torchtext` 则提供了很多文本处理方向的数据集
- `torchaudio` 提供了很多音频处理方向的数据集

当然 `PyTorch`也可以配合其他包来获得数据以及对数据进行处理，比如：

- 对于视觉方面，配合 `Pillow、OpenCV`等
- 对于音频处理方面，配合 `scipy、librosa`等
- 对于文本处理方面，配合 `Cython、NLTK、SpaCy`等
