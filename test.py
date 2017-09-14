
import numpy as np

# a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
b.shape=(1,3)

a=np.array([[1,2,3],
            [4,5,6]])

print np.concatenate((a,b))
print a.shape
b= np.delete(a, (0), axis=0)
print b
#
# c=np.array([8,9])
# c.shape=(2,1)
# print c.shape
# print a.shape
# print c
# d=np.hstack((a,c))
# print d.shape
# print d
# print d[:,4]
# print type(d)