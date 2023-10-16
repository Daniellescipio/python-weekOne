# Danielle Williams
# Python Version 3.11.5
# Activity 2

# part 1

#creates and defines a variable named 'city' with a string wrapped in single quotes. 
city = 'cape canaveral'
#creates and defines a variable named 'nickname' with a string wrapped in single quotes. 
nickname = 'thrusters'

#prints a concatenated string. .title method will capitilize the first letter of each word in the string and the .capitalize methode will capitalize the string assigned to 'nickname'
print("Welcome to " + city.title() + " home of the " + nickname.capitalize())
# displays string in the console prompting the user to enter data. This data will be saved into the name variable.
name = input("Enter Name: ")
#Prints a concatenated string, the nickname variable still has .toCapitlize and the name variable has the .title method which will capitalize it's first letter as well
print("Introducing the latest " + nickname.capitalize() + " player, " + name.title())
 
#Part 2: You will create a python script that accomplishes the following tasks:

#Create 1 variable for each of the 5 Python Data Types (String, Number, List, Tuple & Dictionary) containing an example of that Data Type
a_string = "A string"
a_number = 0
a_list = [1,2,3]
a_tuple = (a_list, [4,5,6,], "more words")
a_dictionary = {"string":a_string, "number":a_number, "list":a_list, "tuple":a_tuple}
#Create 1 variable utilizing the input() method to allow the user to input a string value
color = input("What is your favorite color:")
#Create 1 variable utilizing the input() method to allow the user to input a number value . Ex: varname = int(input("Your string here: "))
age = input("How old are you:")
#Properly concatenate the values stored in the preceding two variables and print them to the screen. 
print (name + " is " + str(age), " and their favorite color is " + color)