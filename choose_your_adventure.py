name = input("Type your name: ")
print("Welcome", name, "to the adventure!")

answer = input(
    "You are on a dirt road and it has come to an end. You can either go left or right. Type 'left' for left OR 'right' for right. "
).lower()

if answer == "left":
    answer = input(
        "You come to a river and you can walk around it or swim through it. Type walk for walk OR 'swim' for swim. "
    ).lower()

    if answer == "swim":
        print(
            "You attempt to swim through the river and are surrounded by alligators. You lose the game."
        )
        quit()
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
        quit()
    else:
        print("That is not a valid option. You lose.")
        quit()

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, would you like to cross or turn back? Type 'cross' for cross OR 'back' for back. "
    ).lower()

    if answer == "back":
        print("You go back to the main road and lose the game.")
        quit()
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them? Type 'yes' for yes OR 'no' for no. "
        ).lower()
        if answer == "yes":
            print(
                "You talk to the stranger and they give you 25 million dollars. You win the game."
            )

        elif answer == "no":
            print(
                "You ignore the stranger. He walks away with all your hopes of escape. You lose the game."
            )
        else:
            print("That is not a valid option. You lose.")
            quit()

    else:
        print("That is not a valid option. You lose.")
        quit()

    print()
else:
    print("That is not a valid option. You lose.")
    quit()
