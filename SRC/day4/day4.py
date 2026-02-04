#simple key value pairs in a dictionary
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print("Dictionary:", my_dict)
# print("Name:", my_dict["name"])

# print("\n")

student = {
    "name":"amit",
    "age":21,
    "course":"engineering"
}
print(student["name"])
student["age"]=22
student["city"]="delhi"
print(student)

#dictionary methonds and iteration
marks={"maths":90,"science":75,"english":85}
print(marks.get("maths"))
print(marks.get("history",0))
for subject,score in marks.items():
    print(subject,score)
#updating marks
marks["science"]=80
print(marks)
#removeing value
removed_score=marks.pop("english")
print(marks)

print("\n")
# Practical Example: Tracking Purchases with a Dictionary
purchases={
    "alice":150,
    "bob":200,
    "charlie":300
}

for name,amount in purchases.items():
    print(f"{name} spent ${amount}")

print("total customers:",len(purchases))


print("\n")
#input dictionary from user
n=int(input("Enter number of customers: "))
user_purchases={}

for i in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name]=amount
    
    print("User Purchase Data:",user_purchases)
top_customer=max(user_purchases,key=user_purchases.get)
print("top spending customer:",top_customer)
min_customer=min(user_purchases,key=user_purchases.get)
print("least spending customer:",min_customer)

print("\n")
#sets & unique collections