from data import Data
import numpy as np
import sys

#分批读取
def loadfile(filename):
    ''' load a file, return a generator. '''
    fp = open(filename, 'r')
    for i, line in enumerate(fp):
        #print(i,line)
        yield line.strip('\r\n')
        if i % 100000 == 0:
            print('loading %s(%s)' % (filename, i), file=sys.stderr)
    fp.close()
    print('load %s succ' % filename, file=sys.stderr)


#生成用户-物品评分矩阵
Set=np.zeros(shape=(6050,4000))
for line in loadfile("data/ml-1m/ratings.dat"):
    userID,movieID,rate,timestamp=line.split("::")
    # print(userID,movieID,rate,timestamp)
    Set[int(userID),int(movieID)]=int(rate)
print(Set.shape)
print(Set)

d=Data(Set)
print(d.dataSet.shape)

#返回迭代器对象
indexes=d.split()






