#simple key value pairs in a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])

print("\n")

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

A={1,2,3}
B={3,4,5}
print(A | B)  #union
print(A & B)  #intersection
print(3 in A)


# Practical Example: Managing a Contact List with a Dictionary
contacts = {
    "yash": "123-456-7890",
    "chethan": "9876543210",
    "harish": "3456456789"
}

contacts["jeevan"] = "1142243432"

contacts["manoj"] = "4524287371"

print("manoj's Contact:", contacts.get("manoj"))
print("Eve's Contact:", contacts.get("Eve", "Contact not found"))

for name, number in contacts.items():
    print(f"Contact: {name} | Phone: {number}")

print("\n")


 # Practical Example: Tracking Unique Website Visitors
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print("Unique User IDs:", unique_users)
print("Is 'ID05' a unique user?", "ID05" in unique_users)
print("Total Logins:", len(raw_logs))
print("Unique Visitors:", len(unique_users))
print("\n")# Practical Example: Analyzing Survey Responses
survey_responses = ["Yes", "No", "Maybe", "Yes", "No", "Yes"]
unique_responses = set(survey_responses)
print("Unique Survey Responses:", unique_responses)
print("Total Responses:", len(survey_responses))
print("Unique Responses Count:", len(unique_responses))
print("\n")


# Practical Example: Comparing Interests Between Two Friends
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_interests_a = friend_a - friend_b
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Unique Interests for Friend A:", unique_interests_a)
