"""
luckysevens.py
Date: 9/13/2019
Author: David T.

The player plays a game of Lucky Sevens where they will decide the initial cash pot, and will play the game until the pot is empty.
After this, the game will display how many rolls they made, and the most money ever in the pot.
	
"""

import random,math

print("\nWelcome to Lucky Sevens!")

pot = int(input("How much money will the pot start at?\n>>> "))

startingPot = pot
maxPot = pot
rolls = 0
auto = False

while True:
	rolls += 1
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	
	# Show the user info about the roll
	print("\nRoll #"+str(rolls)+":")
	print("="*30)
	print("You've rolled a "+str(die1)+" and a "+str(die2)+".\n")
	
	# Print the outcome and decide payout
	if die1+die2 == 7:
		print("Winner!")
		payout = 4
	else:
		print("You lose.")
		payout = -1
	
	print("-"*25)
	print( "%-10s%5s%8s" % ("Pot","$",str(pot)) )
	
	pot += payout
	if pot > maxPot:
		maxPot = pot
	
	print( "%-10s%5s%8s" % ("Win/Loss","-$" if payout < 0 else "+$", str(int(math.fabs(payout)))), sep = "")
	print( "%-10s%5s%8s" % ("Pot is now","$",str(pot)) )
	print("="*30)
	
	# If the pot is 0, end the game
	if pot <= 0:
		break
	
	# Control for displaying rolls
	if auto == False:
		if input("Press ENTER to roll again, or press type A for auto mode.\n").upper() == "A":
			auto = True

# Final outputs
print("\nYou've gone bust.")
print("With a starting pot of $"+str(startingPot)+", and after "+str(rolls)+" rolls, the most the pot ever held was $"+str(maxPot)+".")
input("Press ENTER to exit.\n")