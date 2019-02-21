name = input("What is your name")
age = input("How old are you")
DOB = 2019 - int(age)
#year he or she will turn 100
_year = DOB + 100
print(name + " ,you will turn 100 in " +str( _year))


number = input("Input a random number")
if int(number) % 2 == 1:
    print("This number is odd")
else:
    print("This number is even")
