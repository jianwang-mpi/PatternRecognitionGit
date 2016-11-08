import re
def analyze():
    with open("resultfile.txt", mode="r",encoding="utf-8") as resultfile:
        with open("t10k-labels.idx1-ubyte", mode="rb") as testLabelFile:
            testLabelFile.seek(4)  # jump over the magic number
            s1 = testLabelFile.read(4)  # the amount of items
            number = int.from_bytes(s1, byteorder="big")

            number = int(number);


            each_num_total=[0]*10
            each_num_correct=[0]*10

            resultlist = re.split(" +",resultfile.read())

            for i in range(0, number):  # get the data
                if i % 100 == 0:
                    print(i)
                label = int.from_bytes(testLabelFile.read(1), byteorder="big")
                result=int(resultlist[i])

                each_num_total[label]+=1
                if result==label:
                    each_num_correct[label]+=1
            for i in range(0,10):
                print(each_num_correct[i]/each_num_total[i])

if __name__=="__main__":
    analyze()