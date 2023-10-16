# Danielle Williams
# Python Version 3.11.5
# Activity 4

#a greeting rinted to the console
print("Welcome to class! Let's get to know eachother...")

# five variables are creaed to gather user name, age, where they are from,and what they are excited about
#these variables use the input method to gather data from a user which is then assigned to the variable
name = input("What name do you go by?")
age = input("How old are you?")
orgin = input("Where are you from?")
activity = input("What are you most excited about for the class")

#f string using string interpolation to concate an introduction string with variables with user info.
print(f"Everyone please welcome {name}. {name} is {age} and hails from {orgin}. {name} is most excited about {activity} with everyone in class!")