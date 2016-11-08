import numpy as np
import collections

def train():
    with open("train-labels.idx1-ubyte", mode='rb') as trainLabelFile:
        with open("train-images.idx3-ubyte", mode="rb") as trainImageFile:
            trainLabelFile.seek(4)  # jump over the magic number
            trainImageFile.seek(4)
            s1 = trainLabelFile.read(4)  # the amount of items
            s2 = trainImageFile.read(4)
            number = int.from_bytes(s1, byteorder="big")

            number = int(number)
            print(number)
            rows = int.from_bytes(trainImageFile.read(4), byteorder="big")  # get rows and columns
            columns = int.from_bytes(trainImageFile.read(4), byteorder="big")

            Images = []  # data struct to save the data
            Labels = []
            for i in range(0,number):
                Images.append(np.array([0]))
                Labels.append(0)

            for i in range(0, number):  # get the data
                if i % 100 == 0:
                    print(i)
                label = int.from_bytes(trainLabelFile.read(1), byteorder="big")
                image = []
                for j in range(0, rows * columns):
                    image.append(int.from_bytes(trainImageFile.read(1), byteorder="big"))
                Labels[i] = label
                Images[i] = np.array(image)
                Images[i].shape = (28 * 28, 1)

            return(Labels,Images)




def test(Labels,Images):
    with open("t10k-images.idx3-ubyte", mode="rb") as testImageFile:
        with open("t10k-labels.idx1-ubyte", mode="rb") as testLabelFile:
            testLabelFile.seek(4)  # jump over the magic number
            testImageFile.seek(4)
            s1 = testLabelFile.read(4)  # the amount of items
            s2 = testImageFile.read(4)
            number = int.from_bytes(s1, byteorder="big")

            number = int(number);
            rows = int.from_bytes(testImageFile.read(4), byteorder="big")  # get rows and columns
            columns = int.from_bytes(testImageFile.read(4), byteorder="big")

            testImages = []  # data struct to save the data
            testLabels = []
            for i in range(0, number):
                testImages.append(np.array([0]))
                testLabels.append(0)

            for i in range(0, number):  # get the data
                if i % 100 == 0:
                    print(i)
                label = int.from_bytes(testLabelFile.read(1), byteorder="big")
                image = []
                for j in range(0, rows * columns):
                    image.append(int.from_bytes(testImageFile.read(1), byteorder="big"))
                testLabels[i] = label
                testImages[i] = np.array(image)
                testImages[i].shape = (28 * 28, 1)


            resultFile = open("resultfile-3NN.txt",mode="w+",encoding="utf-8")
            sameCount = 0

            for i in range(0,number):
                if i % 100 == 0:
                    print("number: "+str(i))
                finalResult=0
                firstThree = [float("inf")]*3
                firstThreeLabel = [0]*3

                for j in range(0,len(Labels)):
                    temp = np.linalg.norm(testImages[i]-Images[j])
                    biggest,pos = find_biggest(firstThree)
                    if temp<biggest:
                        firstThree[pos]=temp
                        firstThreeLabel[pos]=Labels[j]

                finalResult = getPopular(firstThreeLabel)
                print(finalResult)
                if finalResult==testLabels[i]:
                    sameCount+=1
                resultFile.write(str(finalResult)+" ")

            print(sameCount/number)

def find_biggest(lst):
    biggest=float("-inf")
    pos = 0
    for i in range(0,len(lst)):
        if lst[i]>biggest:
            biggest=lst[i]
            pos=i
    return biggest,pos

def getPopular(lst):
    counter = collections.Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][0]

if __name__ == "__main__":
    Labels,Images = train()
    test(Labels,Images)
