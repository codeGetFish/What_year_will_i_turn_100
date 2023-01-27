'''This is a simple project for learning to code in Python, it takes 3 inputs in order to work out what the year will be when you turn 100.'''
# name variable takes an input of the users name
name = input("Enter your name: ")
# age variable takes an input of the users age
age = int(input("Enter your age: "))
# current_year variable takes an input of the current year
current_year = int(input("Enter the current year: "))
# result variable calculates what year you will be 100 by minusing your age from the current year and adding 100
result = int(current_year) - int(age) + 100
# the result is printed below with the users name the string and the result
print(str(name) + " You will turn 100 years old in the year " + str(result))
