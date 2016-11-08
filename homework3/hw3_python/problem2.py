import numpy as np


def read_data(file_route):
    with open(file_route,encoding="utf-8") as file:
        x1_line = file.readline()
        x1_array = x1_line.split("\t")
        x2_line = file.readline()
        x2_array = x2_line.split("\t")
        data = []
        for i in range(0,len(x1_array)):
            arr = np.array([1,float(x1_array[i]),float(x2_array[i])])
            arr.shape=(3,1)
            #print(np.array([1,2,3]).reshape(1,3).dot(arr)[0][0])
            data.append(arr)
        return data
def Ho_Kashyap(filename1,filename2,k_max=1000000,step_length0 = 0.05):
    data1 = read_data(filename1)
    data2 = read_data(filename2)
    for i in range(0, len(data2)):
        data2[i] = -1 * data2[i]
    Y=[]
    step_length = step_length0
    for i in range(0,len(data1)):
        for j in range(0,3):
            Y.append(data1[i][j][0])
    for i in range(0,len(data2)):
        for j in range(0,3):
            Y.append(data2[i][j][0])
    Y = np.array(Y).reshape(len(data1)*2,3)
    k=1
    a = np.array([0]*3).reshape(3,1)
    b = np.array([1.0]*(len(data1)*2)).reshape(len(data1)*2,1)
    b_min = 0.01
    print(Y)
    while(True):
        print(k)
        k+=1

        e = Y.dot(a)-b
        e_plus = 1/2*(e+np.abs(e))
        b = b+2*step_length*e_plus
        #step_length = step_length0/k
        a=np.linalg.pinv(Y).dot(b)
        if np.abs(e).all()<b_min:
            print (a)
            print(b)
            break
        if k == k_max:
            print("error")
            break





if __name__=="__main__":
    #Ho_Kashyap("./w1.txt","./w3.txt")
    Ho_Kashyap("./w2.txt", "./w4.txt")
