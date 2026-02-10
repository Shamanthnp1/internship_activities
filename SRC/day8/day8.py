import  numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
result=a+b
print(result)


#vectorized vs loop example
print("\nLoop operation:")
arr=np.random.rand(1000000)
print(arr)

#vectorized
print("\nVectorized operation:")
squared=arr*2
print(squared)

#zero dimensional array
print("\nZero Dimensional Array:")
zero_dim=np.zeros((4,2))
print(zero_dim)

#one dimensional array
print("\nOne Dimensional Array:")
one_dim=np.array([1,2,3,4,5])   
print(one_dim)

#two dimensional array
print("\nTwo Dimensional Array:")
two_dim=np.array([[1,2,3],[4,5,6]])
print(two_dim)

#three dimensional array
print("\nThree Dimensional Array:")
three_dim=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three_dim)

#reshaping arrays
print("\nReshaping Arrays:")
arr=np.arange(12)
reshaped=arr.reshape(3,4)
print(reshaped)

#vertical stacking
print("\nVertical Stacking:")
a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print(vstacked)

#horizontal stacking
print("\nhorizontal stacking")
hstacked=np.hstack((a,b))
print(hstacked)


#statistical functions in nummpy
print("\n statistical mean")
data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))


#linear algebra basics with numpy
print("\n alebra basics with numpy")
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

print(np.dot(A,B))

