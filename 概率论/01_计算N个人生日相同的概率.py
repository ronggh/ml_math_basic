import matplotlib.pyplot as plt


def mydiv(n):
    a = 1.0
    for i in range(n):
        b = 365 - i
        c = b / 365.0
        a = a * c
    return a


if __name__ == "__main__":
    # 定义一对数组
    x = [i for i in range(51)]
    y = [i for i in range(51)]

    for i in range(1, 51):
        f = 1.0 - mydiv(i)

        y[i] = f
        if i % 5 == 0:
            print("%d ----> %f" %(i,f))

    # 绘制图形
    plt.figure(figsize=(20,8),dpi=80)
    plt.plot(x,y)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()