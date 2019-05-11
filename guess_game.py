import random
input_func = raw_input
key = random.randint(1, 10)
print "\tGUESS GAME in Python 2.7 using random.randint() Function\n"
print key
counter = 0
attempts = 3
num = input_func("Enter number between 1 and 10: ")
counter = counter+1
print "Counter = ", counter
attempts = attempts-1
print "Attempts remaining = ", attempts
if num == key:
    print "You guessed the number. The number was ", key
while num != key:
    num = input_func("Enter number between 1 and 10: ")
    counter = counter+1
    print "Counter = ", counter
    attempts = attempts-1
    print "Attempts remaining = ", attempts
    if num == key:
        print "You guessed the number. The number was ", key
        break
    if counter > 2:
        print "You Failed to guess the number in 3 attempts."
        break
