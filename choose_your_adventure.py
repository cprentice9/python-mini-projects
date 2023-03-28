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
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("That is not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, would you like to cross or turn back? Type 'cross' for cross OR 'back' for back. "
    ).lower()

    if answer == "cross":
        print(
            "You successfully cross the bridge. After crossing you see a car and a bicycle. Which will you choose? Type 'car' for car OR 'bicycle' for bicycle. "
        )
    elif answer == "back":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("That is not a valid option. You lose.")

    print()
else:
    print("That is not a valid option. You lose.")
