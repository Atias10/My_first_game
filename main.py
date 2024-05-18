print("Welcome to my computer game!")

playing = input("Do you wanna play? ").capitalize()

if playing != "Yes":
    quit()

print("Ok, lets play :) ")
score = 0

answer = input("What is the best way to open a girl? ").capitalize()

if answer == ("Indirect"):
    print("Correct!")
    score += 1
else:
    print("Wrong answer")

answer = input("What do you need to do after opening the girl ? ").capitalize()

if answer == ("Build rapport"):
    print("Correct!")
    score += 1
else:
    print("Wrong answer")

answer = input("What do you need to do next ? ").capitalize()

if answer == ("Create attraction"):
    print("Correct!")
    score += 1
else:
    print("Wrong answer")

answer = input("What do you need to do after that ? ").capitalize()

if answer == ("Close"):
    print("Correct!")
    score += 1
else:
    print("Wrong answer")


print(f"Your score is {((score/4)*100)} ")

