import numpy as np

A = np.arange(3,15)

print(A) # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(A[3]) # 6

A = np.arange(3,15).reshape(3,4)

print(A)
'''
[[ 3,  4,  5,  6]
 [ 7,  8,  9, 10]
 [11, 12, 13, 14]]
'''
print(A[2]) # [11, 12, 13, 14]
print(A[2][1]) # 12
print(A[2,1]) # 12
print(A[2,:]) # [11, 12, 13, 14]
print(A[:,1]) # [ 4  8 12] 
print(A[1,2:3]) #  [9]
print(A[1,1:3]) # [8 9]

for row in A:
    print(row)
'''
 [3 4 5 6]
 [ 7  8  9 10]
 [11 12 13 14]
'''


for column in A:
    print(column)
'''
[3 4 5 6]
[ 7  8  9 10]
[11 12 13 14]
'''


print(A.T)
'''
[[ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]
 [ 6 10 14]]
'''
for column in A.T:
    print(column)
'''
 [ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]
 [ 6 10 14]
'''

#flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列
print(A.flatten())  # [ 3  4  5  6  7  8  9 10 11 12 13 14]

#flat是一个迭代器，本身是一个object属性
for item in A.flat:
    print(item)
'''
 3
 4
 5
 6
 7
 8
 9
 10
 11
 12
 13
 14
'''


