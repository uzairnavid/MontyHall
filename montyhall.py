# Simulates a generalized version of the Monty-Hall Problem
# with n-doors, where the narrator opens (n - 2) after the 
# player picks a door. Highlights how the probability of success
# changes based on whether or not the player changes their chosen
# door after the first round.
#
# Uzair N Iftikhar, Dec '17
# [That one time I had 7 hours to kill at Heathrow]

import random
import sys # Can provide a command line argument for the number of doors

# Runs one simulation
# Args: boolean change [whether the player changes after the goat is revealed]; int number of doors
def simulate(change, numDoors):
	carIn = random.randrange(0, numDoors) # The door the car is in
	firstPick = random.randrange(0, numDoors) # The first door the player picks
	montyHallOpens = ([x for x in range(0, numDoors) if x != carIn and x!= firstPick])
	if (firstPick == carIn):
		montyHallOpens = montyHallOpens[:-1] # Need to leave one door closed other than the one the player chose

	if (change):
		originalPick = firstPick
		while (firstPick == originalPick or firstPick in montyHallOpens):
			firstPick = random.randrange(0, numDoors)

	if (firstPick == carIn):
		return True
	else:
		return False

# Driver method
def main():
	if (len(sys.argv) < 2): # If the user didn't provide an argument
		numDoors = 3 		# Default to 3 doors
	else:
		numDoors = float(sys.argv[1]) # In case the user entered a non-int
		if (numDoors <= 2 or numDoors != numDoors//1):
			print("Please enter a valid integer value greater than 2")
			return
	numDoors = int(numDoors)
	runs = 50000					 # Number of simulations to run
	for change in [True, False]: 	 # So we can see how the probability changes
		s = 0
		for i in range(runs):
			if (simulate(change, numDoors)):
				s += 1
		print("Probability of success is ", s/runs, "if change is", change)

if (__name__ == '__main__'):
	main()