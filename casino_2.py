import random
n = 100
secret = random.randint(1,n)

guess = 0
while guess != secret:
    guess = int(input("Erraten Sie die geheime Zahl (1-100): "))
    if guess > 0:
        if guess > secret:
            print("Die Zahl ist zu hoch. Versuchen Sie es noch einmal.")
        elif guess < secret:
            print("Die Zahl ist zu klein. Versuchen Sie es noch einmal.")
else:
    print("Gratulation. Sie haben richtig geraten!!!")
    