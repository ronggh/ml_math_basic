import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def mysigmoid(x):
    """
    定义函数
    :param x:
    :return:
    """
    y = 1.0/(1+np.exp(-x))
    return y

if __name__=="__main__":
    x = np.linspace(-10, 10, 1000)
    y = mysigmoid(x)

    # 绘制图像
    plt.figure(figsize=(20,8),dpi=100)
    # 绘制图像
    plt.plot(x,y)
    plt.grid()

    # 显示图像
    plt.show()