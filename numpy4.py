import numpy as np

A=np.array([1,1,1])
B=np.array([2,2,2])

C=np.vstack((A,B)) #vertical stack
D=np.hstack((A,B)) #horizontal stack

print(C)
'''
[[1 1 1]
 [2 2 2]]
'''
print(D) # [1 1 1 2 2 2]
print(A.shape,C.shape) # ((3,), (2, 3))
print(A.shape,D.shape) # ((3,), (6,))

print(A.T) #[1 1 1]
print(A.T.shape) #(3,)

print(A.size) #3
print(A[:,np.newaxis]) # 转置操作
'''
[[1]
 [1]
 [1]]
'''
print(A.reshape(A.size,1))
'''
[[1]
 [1]
 [1]]
'''

#--------------------------------------------------
print('---------------------')
A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]

C=np.vstack((A,B)) #vertical stack
D=np.hstack((A,B)) #horizontal stack

print(C)
'''
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]]
'''
print(D) #
'''
[[1 2]
 [1 2]
 [1 2]]
'''
print(A.shape,C.shape) # (3, 1) (6, 1)
print(A.shape,D.shape) # (3, 1) (3, 2)


#--------------------------------------------------
print('---------------------')
C = np.concatenate((A,B,B,A),axis=0) #合并操作需要针对多个矩阵或序列
#axis参数很好的控制了矩阵的纵向或是横向打印
print(C)
"""
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]
 [2]
 [2]
 [2]
 [1]
 [1]
 [1]]
"""

D = np.concatenate((A,B,B,A),axis=1)

print(D)
"""
[[1 2 2 1]
 [1 2 2 1]
 [1 2 2 1]]
"""

