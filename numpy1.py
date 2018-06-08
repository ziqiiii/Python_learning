import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)

print(a)
print(b)

c = a+b
print(c)

c = a-b
print(c)

c = a*b
print(c)

c = b/a
print(c)

c= np.sin(a)
print(c)

c= np.cos(a)
print(c)

c= np.tan(a)
print(c)


print(b)
print(b<3)
print(b==3)


a = np.array([[1,1],
              [0,1]])
b = np.arange(4).reshape(2,2)

print(a)
print(b)

c = a*b
print(c)

c = a*b
print(c)

c_dot = np.dot(a,b)
print(c_dot)
c_dot_2 = a.dot(b)
print(c_dot_2)


d= np.random.random((2,4))

print(d)
print(np.sum(d))
print(np.sum(d,axis=1)) #each line
print(np.min(d))
print(np.min(d,axis=0))#each column
print(np.max(d))





