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

w3_data = read_data("./w3.txt")
w2_data = read_data("./w2.txt")
for i in range(0,len(w2_data)):
    w2_data[i] = -1*w2_data[i]

false_set = []
a = np.array([0.0,0.0,0.0])
a.shape=(3,1)
for i in range(0,len(w3_data)):
    false_set.append(w3_data[i])
    false_set.append(w2_data[i])
step_length = 1
count=0
while len(false_set) != 0:
    for data in false_set:
        a += step_length*data
    false_set.clear()
    for i in range(0,len(w3_data)):
        if a.reshape(1,3).dot(w3_data[i]) <=0:
            false_set.append(w3_data[i])
        if a.reshape(1,3).dot(w2_data[i])<=0:
            false_set.append(w2_data[i])
    count+=1
    print(count)
print(a)