name=input("enter your name: ")
goal=input("enter your goal: ")


with open("journal.txt", "a") as file:
    file.write(f"name:{name} , Goal :{goal}\n")
    file.close()