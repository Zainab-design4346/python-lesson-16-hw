try:
    age=int(input('Enter your age:'))
    print("Age:",age)
    if age%2==0:
        print("age number is even") 
    else:
        print("age number is odd")

except:
    print("Please anter correct number or data")