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
print("\n")

# Practical Example: Managing an Inventory List
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current Inventory:", inventory)
inventory.append("Eggs")
print("After adding Eggs:", inventory)
inventory.remove("Bananas")
print("After removing Bananas:", inventory)
inventory.sort()
print("Final Updated Inventory:", inventory)

print("\n")
# Practical Example: Temperature Readings Throughout the Day
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])
print("Afternoon Peak Readings:", temperatures[3:6])
print("Last 3 Hours:", temperatures[-3:])

print("\n")




# Tuple Immutability Example
screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
print("Tuples cannot be modified!")
screen_res[0] = 1280  # This will raise a TypeError
