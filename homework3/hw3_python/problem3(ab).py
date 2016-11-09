import numpy as np
import matplotlib.pyplot as plt

def read_data(file_route: str) -> list:
    with open(file_route, encoding="utf-8") as file:
        x1_line = file.readline()
        x1_array = x1_line.split("\t")
        x2_line = file.readline()
        x2_array = x2_line.split("\t")
        x = []
        y=[]
        for i in range(0,len(x1_array)):
            x.append(float(x1_array[i]))
            y.append(float(x2_array[i]))
        x = np.array(x)
        y = np.array(y)

        data = []
        for i in range(0, len(x1_array)):
            arr = np.array([1, float(x1_array[i]), float(x2_array[i])])
            arr.shape = (3, 1)
            # print(np.array([1,2,3]).reshape(1,3).dot(arr)[0][0])
            data.append(arr)
        return data,x,y


def SSRM(filename1, filename2, step_length=2, b=0.5):
    data1,x1,y1 = read_data(filename1)
    data2,x2,y2 = read_data(filename2)
    plt.scatter(x1,y1,c="red")
    plt.scatter(x2,y2)
    for i in range(0, len(data2)):
        data2[i] *= -1
    data1.extend(data2)
    data = data1
    a = np.array([0.0, 0.0, 0.0])
    a.shape = (3, 1)
    print(a)
    print(data)
    count = 0
    false_set = []
    for d in data:
        false_set.append(d)
    x_line = np.arange(-10,10,0.1)
    while len(false_set) != 0:

        count = count + 1
        for y in false_set:
            a = a - step_length*(a.transpose().dot(y) - b) / np.sum(np.square(y)) * y
        false_set.clear()
        for y in data:
            if a.transpose().dot(y)<=b:
                false_set.append(y)
        print(count)
        if count%7==0:
            plt.plot(x_line, -(a[0] + a[1] * x_line) / a[2],label = str(count))


    print(a)
    plt.plot(x_line, -(a[0] + a[1] * x_line) / a[2])
    plt.legend(loc = "upper left")
    plt.show()


if __name__ == "__main__":
    SSRM("./w2.txt", "./w3.txt")
