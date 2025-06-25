students={"Alice":85,"Rocky":90,"Ram":100}
name=input("Enter the student's name:")
if(name in students):
    print( f"{name}'s marks are {students[name]}")
else:
    print("Student not found.")