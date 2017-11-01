'''
xierhacker.2017.11.1

    #storage dataSet
    #split dataset

'''
import sys
import os
from sklearn.model_selection import ShuffleSplit

class Data():
    def __init__(self,dataSet):
        self.dataSet=dataSet

    #传入参数为数据集分割次数,和数据集,默认按照测试机0.3,训练集0.7分割,分割10次
    #返回的是训练集和测试集合迭代器对象.
    def split(self,n=10,test_size=0.3,train_size=0.7):
        #建立一个分割对象
        sp=ShuffleSplit(n_splits=n,test_size=test_size,train_size=train_size)
        return sp.split(X=self.dataSet);






