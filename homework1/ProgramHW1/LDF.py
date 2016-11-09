import numpy as np

mean = [np.array([0] * 28 * 28)] * 10  # init
variance = [np.matrix([[0] * 28 * 28] * 28 * 28)] * 10

w = [np.array([0] * 28 * 28)] * 10
w0 = [0] * 10


def train():
    with open("train-labels.idx1-ubyte", mode='rb') as trainLabelFile:
        with open("train-images.idx3-ubyte", mode="rb") as trainImageFile:
            trainLabelFile.seek(4)  # jump over the magic number
            trainImageFile.seek(4)
            s1 = trainLabelFile.read(4)  # the amount of items
            s2 = trainImageFile.read(4)
            number = int.from_bytes(s1, byteorder="big")
            assert (number == int.from_bytes(s2, byteorder="big"))  # if the amount of images are equal

            number = int(number)
            rows = int.from_bytes(trainImageFile.read(4), byteorder="big")  # get rows and columns
            columns = int.from_bytes(trainImageFile.read(4), byteorder="big")

            Images = [[0] * rows * columns] * number  # data struct to save the data
            Labels = [0] * number

            for i in range(0, number):  # get the data
                if i % 100 == 0:
                    print(i)
                label = int.from_bytes(trainLabelFile.read(1), byteorder="big")
                image = []
                for j in range(0, rows * columns):
                    image.append(int.from_bytes(trainImageFile.read(1), byteorder="big"))
                Labels[i] = label
                Images[i] = image

            total = [np.array([0] * rows * columns)] * 10  # init the total array
            totalVariance = [np.matrix([[0] * rows * rows] * columns * columns)] * 10

            for i in range(0, number):  # get the mean
                if i % 100 == 0:
                    print(i)
                label = Labels[i]
                total[label] = total[label] + Images[i]
            for i in range(0, 10):
                mean[i] = total[i] / number

            for i in range(0, number):  # get the variance
                if i % 100 == 0:
                    print(i)
                label = Labels[i]
                imageArray = np.array(Images[i])
                diff = imageArray - mean[label]
                diff.shape = (28 * 28, 1)
                totalVariance[label] = totalVariance[label] + diff.dot(np.transpose(diff))

            for i in range(0, 10):
                variance[i] = totalVariance[i] / number + variance[i]

            averageVariance = np.matrix([[0] * rows * rows] * columns * columns)
            for i in range(0, 10):
                averageVariance = averageVariance + variance[i]
            averageVariance = averageVariance / 10

            for i in range(0, 10):
                mean[i].shape = (28 * 28, 1)
                temp = np.linalg.pinv(averageVariance)
                w[i].shape = (28 * 28, 1)
                w[i] = temp.dot(mean[i])
                w0[i] = -0.5 * np.transpose(mean[i]).dot(temp).dot(mean[i])
                w[i] = np.transpose(w[i])


def test():
    with open("t10k-images.idx3-ubyte", mode="rb") as testImageFile:
        with open("t10k-labels.idx1-ubyte", mode="rb") as testLabelFile:
            testLabelFile.seek(4)  # jump over the magic number
            testImageFile.seek(4)
            s1 = testLabelFile.read(4)  # the amount of items
            s2 = testImageFile.read(4)
            number = int.from_bytes(s1, byteorder="big")
            assert (number == int.from_bytes(s2, byteorder="big"))  # if the amount of images are equal

            number = int(number)
            rows = int.from_bytes(testImageFile.read(4), byteorder="big")  # get rows and columns
            columns = int.from_bytes(testImageFile.read(4), byteorder="big")

            Images = [np.array([0] * rows * columns)] * number  # data struct to save the data
            Labels = [0] * number

            for i in range(0, number):  # get the data
                if i % 100 == 0:
                    print(i)
                label = int.from_bytes(testLabelFile.read(1), byteorder="big")
                image = []
                for j in range(0, rows * columns):
                    image.append(int.from_bytes(testImageFile.read(1), byteorder="big"))
                Labels[i] = label
                Images[i] = np.array(image)
                Images[i].shape = (28 * 28, 1)

            count = 0
            max_pos = 0
            count_every=[0]*10
            correct_every=[0]*10
            for i in range(0, number):
                max = float("-inf")
                for j in range(0, 10):
                    temp = w[j].dot(Images[i]) + w0[j]
                    if temp > max:
                        max = temp
                        max_pos = j
                count_every[Labels[i]]+=1
                if max_pos == Labels[i]:
                    count = count + 1
                    correct_every[Labels[i]]+=1
            print(count / number)
            for i in range(0,10):
                print("the correctness of "+str(i)+" is "+ str(correct_every[i]/count_every[i]))


if __name__ == "__main__":
    train()
    test()
