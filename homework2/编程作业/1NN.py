import numpy as np



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

            result = []
            resultFile = open("resultfile.txt",mode="w+",encoding="utf-8")
            sameCount = 0

            for i in range(0,number):
                if i % 100 == 0:
                    print("number: "+str(i))
                minDistance = float("inf")
                minResult = 0
                for j in range(0,len(Labels)):
                    temp = np.linalg.norm(testImages[i]-Images[j])
                    if temp<minDistance:
                        minDistance=temp
                        minResult=Labels[j]
                print(minResult)
                if minResult==testLabels[i]:
                    sameCount+=1
                resultFile.write(str(minResult)+" ")

            print(sameCount/number)







if __name__ == "__main__":
    Labels,Images = train()
    test(Labels,Images)
