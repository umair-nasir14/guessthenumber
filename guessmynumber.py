# program to decide a number and let user find out the number

# import the random range generator library
from random import randrange

game_run_status=False
allowed_guesses=5
guess_count=0

# make a number guess between 0 and 20
machineguess=randrange(20)

# greet and inform the user about the guess.
print "I have chosen a number between 0 to 20 ... \n"
def get_a_guess() :
	while True:
		try:
			guess = int(raw_input("Please guess the number I have chosen: "))
		except ValueError:
			print("Please enter an integer!")
			continue
		else:
			# print "You entered "+ str(guess)
			return guess
			break 

def guess_responder(myguess,machineguess):
	if myguess==machineguess:
		print "You got it! "+str(myguess)+" is the number I chose.\n"
		return True
	elif myguess < machineguess :
		print "The number I chose is larger than your guess, try again.\n"
		return False
	else :
		print "The number I chose is smaller than your guess, try again.\n"
		return False


while game_run_status==False:
	myguess=get_a_guess()
	game_run_status=guess_responder(myguess,machineguess)
	guess_count=guess_count+1
	if  guess_count>allowed_guesses :
		print "**************** YOU LOST !***********************************************\n"
		print "     You LOST ! You are not allowed more than "+str(allowed_guesses)+ " guesses\n"
		print "     The number I had chosen was "+str(machineguess)+" . Better luck next time\n"
		print "**************************************************************************\n"
		break
	pass

if guess_count<allowed_guesses :
	print "**************** YOU WON !************************************************\n"
	print "     You WON ! Guessed it right in "+ str(guess_count) +" attempts!\n"
	print "**************************************************************************\n"
