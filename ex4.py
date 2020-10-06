cars = 100
#value of the variable "cars" is equal to 100
space_in_a_car = 4.0
#value of the variable "space_in_a_car" is equal to 4.0
drivers = 30
#value of the variable "drivers" is equal to 30
passengers = 90
#value of the variable "passengers" is equal to 90
cars_not_driven= cars - drivers
#value of the variable "cars_not_driven" is equal to cars-drivers
cars_driven = drivers
#value of the variable "cars_driven" is equal to drivers
carpool_capacity = cars_driven * space_in_a_car
#value of the variable "carpool_capacity" is equal to cars_driven*space_in_a_car
average_passengers_per_cab = passengers / cars_driven

print ("There are", cars, "cars available.")  # There are 100 cars available.
print ("There are only", drivers, "drivers available.") # There are only 30 drivers available.
print ("There will be", cars_not_driven, "empty cars today.") # There will be 70 empty cars today.
print ("We can transport", carpool_capacity, "people today.") # We can transport 120.0 people today.
print ("We have", passengers, "to carpool today.") # We have 90 to carpool today.
print ("We need to put about", average_passengers_per_cab, "in each car.") # We need to put about 3 in each car.

#Study Drills
#When I wrote this program the first time I had a mistake, and Python told me about it like this:
#Traceback (most recent call last):
#File "ex4.py", line 8, in <module>
#average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined
#Explain this error in your own words. Make sure you use line numbers and explain why.
# Easy, we never defined a variable named car_pool_capacity, we never paired it with a value, so the program can not execute calculations with it. car_pool_capacity is a different variable (in our case it is a not defined one) than carpool_capacity.
#1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4? # As we learned earlier, if we do not use floating point numbers, our result aren't going to be precise, they will lack the fractional part after the decimal.
#Here’s more Study Drills:
#2. Remember that 4.0 is a “floating point” number. Find out what that means. # Hell, I just explained it, but no problem Sir, we write 4.0 instead of 4 to get a floating point number which is valueable for us many times.
#3. Write comments above each of the variable assignments.
#4. Make sure you know what = is called (equals) and that it’s making names for things.
#5. Remember that _ is an underscore character.
#6. Try running Python as a calculator like you did before and use variable names to do your
#calculations. Popular variable names are also i, x, and j.
#Common Student Questions
#What is the difference between = (single- equal) and == (double- equal)?
#The = (single- equal) assigns the value on the right to a variable on the left. The == (double- equal)
#tests if two things have the same value, and you’ll learn about this in Exercise 27.
#Can we write x=100 instead of x = 100?
#You can, but it’s bad form. You should add space around operators like this so that it’s easier to
#read.
#How can I print without spaces between words in print?
#You do it like this: print "Hey %s there." % "you". You will do more of this soon.
#What do you mean by “read the file backward”?
#Very simple. Imagine you have a file with 16 lines of code in it. Start at line 16, and compare it to
#my file at line 16. Then do it again for 15, and so on, until you’ve read the whole file backward.
#Why did you use 4.0 for space?
#It is mostly so you can then find out what a floating point number is and ask this question. See
#the Study Drills.


