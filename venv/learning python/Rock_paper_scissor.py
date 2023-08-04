import random

choices=["Rock", "Paper", "Scissors"]

computer= random.choice(choices)
player= None

while player not in choices:
    player = input("rock , paper or scissors: ").capitalize()

print("your choice is : "+player)
print("Computer choice is: "+computer)

if(player== computer):
    print("you Guessed right! You win.")
else:
    print("Your guessed is wrong ! You Lost.")