print("Welcome to the quiz")

playing = input("Would you like to play a game? ")

if playing != "yes":
    quit()

print("Okay! Let's play :) ")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("That is incorrect, let's try again!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("That is incorrect, let's try again!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("That is incorrect, let's try again!")

answer = input("What does PSU stand for? ")
if answer == "power supply unit":
    print("Correct!")
else:
    print("That is incorrect, let's try again!")