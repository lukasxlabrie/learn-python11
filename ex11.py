#Asks user to enter age, end = tells PY not to end the line with a newline and to go to the next line
print("How old are you?", end = ' ')
#Var defined by user
age = input ()
#asks the user to enter height
print("How tall are you?", end = ' ')
#var defined by user
height = input ()
#asks for input via print string
print("How much do you weigh?", end = ' ')
#var defined by user
weight = input()
#f string which combines all Var into one statement
print(f"So, you're {age} old, {height} tall, and {weight} heavy.")