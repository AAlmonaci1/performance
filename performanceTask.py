#Mad Libs Generator: Create a program that generates 
#funny stories based on user input.

print("Welcome to Mad Libs! Where you can create funny stories based on your input!")

while True:
    startGame =  input("Will you like start?").lower()
    if startGame == "yes":
        print("Great let's start!")
        break
    elif startGame == "no":
        print("Ok. Suit yourself!")
        break
    else:
        print("Please enter either 'yes' or 'no'")

storyPaths = ["fairytale", "disaster"]

print("Which story path will you like to take? Fairytale or Disaster...").lower()

def 

