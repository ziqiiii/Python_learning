import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)

print(a) #[10 20 30 40]
print(b) #[0 1 2 3]

c = a+b
print(c) #[10 21 32 43]

c = a-b
print(c) #[10 19 28 37]

c = a*b
print(c) #[  0  20  60 120]

c = b/a
print(c) #[0.         0.05       0.06666667 0.075     ]

c= 10*np.sin(a)
print(c) #[-5.44021111  9.12945251 -9.88031624  7.4511316 ]

c= np.cos(a)
print(c) #[-0.83907153  0.40808206  0.15425145 -0.66693806]

c= np.tan(a)
print(c) #[ 0.64836083  2.23716094 -6.4053312  -1.11721493]


c= b**2
print(c) #[0 1 4 9]

print(b) #[0 1 2 3]
print(b<3) #[ True  True  True False]
print(b==3) #[False False False  True]


a = np.array([[1,1],
              [0,1]])
b = np.arange(4).reshape(2,2)

print(a)
#[[1 1]
# [0 1]]

print(b)
#[[0 1]
# [2 3]]

c = a*b
print(c) #矩阵乘法：1.对应元素相乘
# [[0 1]
#  [0 3]]

c_dot = np.dot(a,b) #矩阵乘法:2.标准的矩阵乘法运算，即对应行乘对应列得到相应元素
print(c_dot)
#[[2 4]
# [2 3]]

#另外的一种关于dot的表示方法:
c_dot_2 = a.dot(b)
print(c_dot_2)


d= np.random.random((2,4)) #从0到1的随机数
#[[0.85495172 0.9741222  0.41543361 0.33450706]
# [0.58007087 0.43367435 0.72388887 0.16034378]]
print(d)

print(np.sum(d))
#4.476992464110268

print(np.sum(d,axis=1)) #each line，当axis的值为1的时候，将会以行作为查找单元
#[2.57901459 1.89797787]


print(np.min(d)) #0.16034377580836667

print(np.min(d,axis=0))#each column，当axis的值为0的时候，将会以列作为查找单元
#[0.58007087 0.43367435 0.41543361 0.16034378]


print(np.max(d))
#0.9741222029914546




