#Mad Libs Generator: Create a program that generates 
#funny stories based on user input.

print("Welcome to Mad Libs! Where you can create funny stories based on your input!")

while True:
    startGame =  input("Will you like start? ").lower()
    if startGame == "yes":
        print("Great let's start!") ################# put all code after here
        break
    elif startGame == "no":
        print("Ok. Suit yourself!")
        break
    else:
        print("Please enter either 'yes' or 'no'")

story_option = ["fairytale", "disaster"]

def storyPlay(story_option):
    while True:  
        if story_option == "fairytale":
            adj = input("1/10 Enter an adjective: ").lower()
            main_character = input("2/10 Enter a noun for your main character: ").lower()
            place = input("3/10 Enter a noun for a place to live in: ").lower()
            noun = input("4/10 Enter a noun: ").lower()
            magic_item = input("5/10 Enter another noun: ").lower()
            place2 = input("6/10 Enter another noun for a different place: ").lower()
            feeling = input("7/10 Enter a feeling: ").lower()
            animal = input("8/10 Enter a creature: ").lower()
            valuable_noun = input("9/10 Enter a noun: ").lower()
            handsome = input("10/10 Enter another noun for a character:").lower()
        
            print(f"""
                                                        the magical {magic_item}
Once upon a time there was a {adj} {main_character} who lived in a giant {place}. One day a {noun} came to visit, bringing news about a magical {magic_item} in a nearby {place2}.
The {main_character} was very {feeling} to hear such interesting news and quickly made plans to visit the {place2}.
Before they arrived, a ghastly {animal} leaped out in front of their carriage. The {animal} demanded all of their {valuable_noun}s.
It was then that a handsome {handsome} appeared as if out of nowhere and chased away the {animal}. The {main_character} and the handsome {handsome} decided to throw a grand party to celebrate.
The end.
""")
            other_story= input("Would you like to hear the other story?")
            if other_story == 'yes':
                    story_option = input("Which story path will you like to take? Fairytale or Disaster...").lower()
            else:
                break
            
        elif story_option == "disaster":
            noun = input("1/15 Enter a noun: ").lower()
            adj = input("2/15 Enter an adjective: ").lower()
            adv = input("3/15 Enter an adverb: ").lower()
            verb = input("4/15 Enter a present tense verb: ").lower()
            verb2 = input("5/15 Enter a past tense verb: ").lower()
            adj2 = input("6/15 Enter an adjective: ").lower()
            adv2 = input("7/15 Enter an adverb: ").lower()
            adj3= input("8/15 Enter an adjective: ").lower()
            verb3 = input("9/15 Enter a past tense verb: ").lower()
            noun2 = input("10/15 Enter a noun: ").lower()
            adj4 = input("11/15 Enter an adjective: ").lower()
            noun3 = input("12/15 Enter a noun: ").lower()
            adj5 = input("13/15 Enter an adjective: ").lower()
            noun4 = input("14/15 Enter a noun: ").lower()
            feeling = input("15/15 Enter a feeling: ").lower()

            print(f"""
                                        {feeling} to be alive
One morning, on the 22nd of july, I was walking near a {noun} when I heard a(n) {adj} cracking BANG! I {adv}
turned to look in the direction it came from. What I saw made me {verb}. I couldn't believe it!
The entire side of the mountain had {verb2} and there was a(n) {adj2} cloud of smoke {adv2} it. I was frozen in place until the second {adj3} 
bang came. It shook me to the core! Large rocks {verb3} out of the {noun2} and {adj4} lava started flowing down the valley. 
Survival mode suddenly kicked in and the last thing I can remember was running for my life towards the {noun3}. I woke up hours later
with a {adj5} {noun4}. I am very {feeling} to be alive today!
""")
            other_story= input("Would you like to hear the other story?")
            if other_story == 'yes':
                    story_option = input("Which story path will you like to take? Fairytale or Disaster...").lower()
            else:
                break
        
        elif story_option != "fairytale" or "disaster":
            print("please enter either 'fairytale' or 'disaster'")
            story_option = input("Which story path will you like to take? Fairytale or Disaster...").lower()

       
    
story_option = storyPlay(input("Which story path will you like to take? Fairytale or Disaster... ").lower())
print("Thank you for playing")

print("""     
_____________________________________________________________________________________________________________________________________________________________________________     
      """)

print("Wait hold on! We have more stories in Mad Libs!")

while True:
    startGame =  input("Would you like to hear a Spooky or Funny mad lib? ").lower()
    if startGame == "yes":
        print("Great let's start!") ################# put all code after here
        break
    elif startGame == "no":
        print("Ok. Suit yourself!")
        break
    else:
        print("Please enter either 'yes' or 'no'")

story_option2 = ["spooky", "funny"]

def storyPlay2(story_option2):
     while True:  
        if story_option2 == "spooky":
            noun = input("1/13 Enter a noun: ").lower()
            verb = input("2/13 Enter a present tense verb: ").lower()
            noise = input("3/13 Enter a sound: ").lower()
            place= input("4/13 Enter a noun for a place to live in: ").lower()
            verb2 = input("5/13 Enter a verb: ").lower()
            noun2 = input("6/13 Enter a noun: ").lower()
            verb3 = input("7/13 Enter a verb: ").lower()
            creature = input("8/13 Enter a creature: ").lower()
            noun3 = input("9/13 Enter a noun: ").lower()
            noun4 = input("10/13 Enter a noun: ").lower()
            adj = input("11/13 Enter an adjective: ").lower()
            verb4 = input("12/13 Enter a present tense verb: ").lower()
            adj2 = input("13/13 Enter an adjective: ").lower()
        
            print(f"""
                                            the scary {noise}
One night me and my {noun} were {verb} along a hidden path. All of a sudden we heard a loud {noise} from deep in
the {place}. The noise made us {verb2} out of our {noun2}. We started to {verb3} as fast as we could! Just when we
thought we got far enough away, we stumbled upon a {creature} that started talking to us about {noun3}. Never in my
life have I seen a talking {creature}! I was relieved to spot a {noun4} in the distance that hopefully could give us 
a place to hide. As we made our way towards it, we heard that {adj} noise again! We start {verb4} and finally
reached our destination. What a {adj2} night it was!

""")
            other_story= input("Would you like to hear the other story? ")
            if other_story == 'yes':
                    story_option2 = input("Which story path will you like to take? Spooky or Funny... ").lower()
            else:
                break
            
        elif story_option2 == "funny":
            noun = input("1/11 Enter a noun: ").lower()
            verb = input("2/11 Enter a present tense verb: ").lower()
            noun2 = input("3/11 Enter a noun: ").lower()
            proper_noun = input("4/11 Enter a proper noun: ").lower()
            verb2 = input("5/11 Enter a past tense verb: ").lower()
            noun3 = input("6/11 Enter a noun: ").lower()
            bodyPart = input("7/11 Enter a body part").lower()
            person = input("8/11 Enter a character:").lower()
            adj = input("9/11 Enter an adjective: ").lower()
            activity = input("10/11 Enter an activity: ").lower()
            restaurant = input("11/11 Enter a restaurant name").lower()
                
           
            print(f"""
                                            not so {adj} {noun}
A {noun} in {state} was arrested this morning after they {verb} in front of {noun2}. {proper_noun}, had a history of {verb} with a {noun3} stuck
in their {bodyPart}. Their {person} states, "I thought they were {adj}, I never thought they would do anything like this... this is {feeling}!"
After a brief {activity} , the cops followed them to {restaurant} where they reportedly {verb2} in the back of the restaurant. After witnessing 
them {verb} with a {noun2} there. They are probably going to need a whole lot of therapy...
""")
            other_story= input("Would you like to hear the other story? ")
            if other_story == 'yes':
                    story_option2 = input("Which story path will you like to take? Spooky or Funny... ").lower()
            else:
                break
        
        elif story_option2 != "horror" or "funny":
            print("please enter either 'spooky' or 'funny'")
            story_option2 = input("Which story path will you like to take? Spooky or Funny... ").lower()

       
    
story_option2 = storyPlay2(input("Which story path will you like to take? Spooky or Funny... ").lower())
print("Thank you for playing")
