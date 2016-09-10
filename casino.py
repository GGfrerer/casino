secret = int("7")
guess = int(raw_input("Guess the secret number: "))
if guess == secret:
    print "Congratulations. You guessed the number correctly!"
else:
    print "Sorry. The number is not correct."
