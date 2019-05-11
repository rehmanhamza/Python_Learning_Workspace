import random
game_running=True
while game_running:
	print()
	print("I'm thinking of number between 1 and 10")
	secret_number=random.randint(0,10)
	guess_number=-1
	while guess_number!=secret_number:
		print()
		guess=input("Enter Number: ")
		if guess=="quit":
			game_running=False
			break
		else:
			guess_number=int(guess)
		if guess_number==secret_number:
			print()
			print("Congrats!")
		else:
			print()
			print("That's not my number")