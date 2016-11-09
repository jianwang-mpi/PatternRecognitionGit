# -*- coding: utf-8 -*-
print(__doc__)

import math
import pylab as pl
import numpy as np
from mnist import MNIST
import random
from collections import Counter


# 按照分布概率采样，生成class随机数
def prob_choice_class(probs):
    rnd = random.random() * sum(probs)
    for i, w in enumerate(probs):
        rnd -= w
        if rnd < 0:
            return i

            # 按照分布概率采样，生成feature随机数


# 按照概率分布进行映射到0～1000区间
def prob_choice_feature(probs):
    rnd = random.random() * 1000
    prob_section = []
    for i in range(0, len(probs)):
        if rnd >= sum(prob_section):
            prob_section.append(int(probs[i] * 1000))
            if rnd < sum(prob_section) or i == len(probs) - 1:
                return i


                # 开源数据集


mndata = MNIST('data')
mndata.load_training()

# 平滑数据，转化为(samples, feature)的矩阵
n_samples = len(mndata.train_images)
data = np.array(mndata.train_images).reshape(n_samples, -1)

# 统计数据
count_class = Counter()
count_feature = {}
# 构建3维数组
for x in range(0, 10):
    ycount = {}
    for y in range(0, 784):
        zcount = {}
        for z in range(0, 256):
            zcount[z] = 0
        ycount[y] = zcount
    count_feature[x] = ycount
# 分别统计class和feature
for i in range(0, len(data)):
    count_class[mndata.train_labels[i]] += 1
    for j in range(0, len(data[i])):
        count_feature[mndata.train_labels[i]][j][int(data[i][j])] += 1

        # 计算class的概率分布
count_class_prob = []
count_class_sum = sum(count_class.values())
for key, value in count_class.iteritems():
    count_class_prob.append(float(value) / count_class_sum)

# 计算每个像素维度的分布概率
count_feature_prob = {}
# 构建3维数组
for x in range(0, 10):
    ycount = {}
    for y in range(0, 784):
        zcount = {}
        for z in range(0, 256):
            zcount[z] = 0
        ycount[y] = zcount
    count_feature_prob[x] = ycount
# 具体计算
for i in range(0, 10):
    for j in range(0, 784):
        count_feature_sum = sum(count_feature[i][j].values())
        for k in range(0, 256):
            count_feature_prob[i][j][k] = float(count_feature[i][j][k]) / count_feature_sum
            ##file_class = open('model/classprob', 'w')
##file_feature = open('model/featureprob', 'w')
##file_class.write(str(count_class_prob))
##file_feature.write(str(count_feature_prob))
##file_class.close()
##file_feature.close()
# 根据模型构建图片
# 指定构建图片数量
nr_target = 10
# 图片的像素维度(28*28=784)
nr_feature = 784
# 开始生成图片像素矩阵
class_ = []
feature = []
for x in xrange(nr_target):
    target = prob_choice_class(count_class_prob)
    class_.append(target)
    for y in xrange(nr_feature):
        feature.append(float(prob_choice_feature(count_feature_prob[target][y])))
features = np.array(feature).reshape((nr_target, 28, 28))

# 根据矩阵保存为相应图片
# 图片命名规则：编号_类别（num_class）
num = 0
for index, (image, prediction) in enumerate(zip(features, class_)):
    pl.subplot(1, 1, 1)
    pl.axis('off')
    pl.imshow(image, cmap=pl.cm.gray_r, interpolation='nearest')
    pl.savefig('pic/' + repr(num) + '_%i' % prediction)
    ##    pl.title('Create: %i' % prediction)
    num += 1

    ##pl.show()