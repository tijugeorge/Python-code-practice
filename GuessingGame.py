import random

highest = 10
answer = random.randrange(highest)
guess = raw_input("Guess a number from 0 to %d:" %highest)
while (int(guess)!=answer):
    if (int(guess)<answer):
        print "Answer is higher"
    else:
        print "Answer is lower"
    guess = raw_input("Guess a number from 0 to %d: "%highest)
raw_input("You're a winner Face!!!")
