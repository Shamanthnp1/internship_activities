#list exmple
numbers = [1, 2, 3, 4, 5]
#tuple example
coordinates = (10.0, 20.0)
print("Numbers List:", numbers)
print("Coordinates Tuple:", coordinates)

#indexing and sliceing
a=[100,200,300,400,500,600,700,800,900]
print(a[1:4])
print(a[:5])
print(a[5:])
print(a[-3:-1])
print(a[2:9:3])
print(a[-2:-9:-3])


#list methods & mutability
print("List Methods & Mutability")
num=[10,20,30,40,50]
print(num)
num.append(60)
print(num)
#ascending order
num.sort()
print(num)
#descending order
num.reverse()
print(num)
print(num.pop())
print(num)
num.remove(30)
print(num)
num.insert(2,25)
print(num)
num.extend([70,80,90])
print(num)