#There are 10 types of people. %d will be replaced with %10
types_of_people = 10
x = f"There are {types_of_people} types of people."
#the value of variable binary is equal to binary
binary= "binary"
#the value of the variable do_not is equal to don't
do_not = "don't"
#the value of the variable y is equal to Those who know binary and those who don't
y = f"Those who know {binary} and those who {do_not}."
#gonna print the value of x
print (x)
#print the value of y
print (y)
#print I said: %r will be replaced with the value of x
print (f"I said: {x}.")
#I also said: %s will be replaced with the value of y
print (f"I also said: '{y}'")
# value of variable hilarious is equal to False
hilarious = False

joke_evaluation = "Isn't that joke funny?! {}"

print (joke_evaluation.format (hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)
