my_name= 'Zed A. Shaw'
my_age= 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print (f"Let's talk about {my_name}.")
print (f"He'{my_height} inches tall.")
print (f"He's {my_weight} pounds heavy.")
print (f"Actually that's not too heavy.")
print (f"He's got {my_eyes} eyes and {my_hair} hair.")
print (f"His teeth are usually {my_teeth} depending on the coffe.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print (f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Study Drills
# Change all the variables so there isnt the my_ in front. Make sure you change the name
# everywhere, not just where you used = to set them.
# Try more format characters. %r is a very useful one. It's like saying print this no matter
# what.
# Search online for all the Python format characters.
# Try to write some variables that convert the inches and pounds to centimeters and kilos.
# Do not just type in the measurements. Work out the math in Python.
# Common Student Questions
# Can I make a variable like this: 1 = 'Zed Shaw'?
# No, the 1 is not a valid variable name. They need to start with a character, so a1 would work, but
# 1 will not.
# What does %s, %r, and %d do again?
# You'll learn more about this as you continue, but they are "formatters". They tell Python to take
# the variable on the right and put it in to replace the %s with its value.
# I don't get it, what is a formatter? Huh?
# The problem with teaching you programming is that to understand many of my descriptions, you
# need to know how to do programming already. The way I solve this is I make you do something,
# and then I explain it later. When you run into these kinds of questions, write them down and see
# if I explain it later.
# How can I round a fl oating point number?
# You can use the round() function like this: round(1.7333).
# I get this error TypeError: 'str' object is not callable.
# You probably forgot the % between the string and the list of variables.
# Why does this not make sense to me?
# Try making the numbers in this script your measurements. It's weird, but talking about yourself
# will make it seem more real
