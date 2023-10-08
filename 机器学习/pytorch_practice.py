#1、Tensor 的概念
# Tensor 中文为张量。张量的意思是一个多维数组，它是标量、向量、矩阵的高维扩展。
# 标量可以称为 0 维张量，向量可以称为 1 维张量，矩阵可以称为 2 维张量，RGB 图像可以表示 3 维张量。你可以把张量看作多维数组。

import numpy as np
import torch

# Tensor 创建的方法
def test1():
    # data可以是list、numpy
    # torch.tensor(data, dtype=None, device=None, requires_grad=False, pin_memory=False)
    arr = np.ones((3, 3))
    print("ndarray的数据类型：", arr.dtype)
    # 创建存放在 GPU 的数据
    # t = torch.tensor(arr, device='cuda')
    t= torch.tensor(arr)
    print(t)

#修改
def test2():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    t = torch.from_numpy(arr)
    # 修改 array，tensor 也会被修改
    # print("\n修改arr")
    # arr[0, 0] = 0
    # print("numpy array: ", arr)
    # print("tensor : ", t)

    # 修改 tensor，array 也会被修改
    print("\n修改tensor")
    t[0, 0] = -1
    print("numpy array: ", arr)
    print("tensor : ", t)

# 根据数值创建 Tensor
def test3():
    out_t = torch.tensor([1])
    # 这里制定了 out
    t = torch.zeros((3, 3), out=out_t)
    print(t, '\n', out_t)
    # id 是取内存地址。最终 t 和 out_t 是同一个内存地址
    print(id(t), id(out_t), id(t) == id(out_t))

# 创建自定义数值的张量
def test4():
    t = torch.full((3, 3), 1)
    print(t)

# 创建等差的 1 维张量。注意区间为[start, end)。
def test5():
    t = torch.arange(2, 10, 2)
    print(t)

# 创建均分的 1 维张量。数值区间为 [start, end]
def test6():
    # t = torch.linspace(2, 10, 5)
    t = torch.linspace(2, 10, 6)
    print(t)

#     创建对数均分的 1 维张量。数值区间为 [start, end]，底为 base。base
def test7():
    # t = torch.logspace(2, 10, 5)
    t = torch.logspace(2, 10, 6)
    print(t)

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    test7()