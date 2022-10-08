#Adam Altice
#Project Week 2

#Intro, introduce user to the story options

print('please choose from the following scenarios to complete: \n')

print('A: You are a rogue who found a chest you think contains treasure. Successfully picklock the chest to gain wealth. But be careful, if you fail to open the chest it magically locks forever. \n')

print('B: You are fishing in a local tournament. Pick the best lure option for catching the winning fish! \n')

print('C: You are camping and foraging for local food. You see a few options and decide to try one, hoping it is delicious! \n ')

#Prompt the user for their choice
userChoice = input("Please choose from the above options, A, B or C to beging the scenario. \n\n")

#If block, starting with option A
if userChoice == "A".lower():
  print('You are close to unlocking the chest with the treasure of your wildest dreams... but you run in to a twist, you are presented the following test to prove your worthiness!\n ')
  choiceA = int(input('Your picklocking skills are great, Rogue. But how about your Math skills? Tell me, what is 100 X 4.\n '))
  #If correct choice
  if choiceA == (400):
    print('You earned the treasure!! Enjoy your wealth and use it for good.')
  #If wrong choice
  else:
    print('You are unworthy of this treasure! Be gone, Rogue')
#elif to start second option block
elif userChoice =="B".lower():
  choiceB = input("It is early morning, fish are hitting the surface. Choose between the following options: \n A: popper\n B: worm\n C: jig\n D: grub \n")
  #If correct
  if choiceB == "A".lower():
    print('You destroy it user the topwater bait! The tournament is yours! Hooray!')
  #Not correct
  else: print('You had a decent result but missed out on the topwater opportunity. Better luck next time. You congratulate the winner and return home.')
#Else statement, prompts if the first two options aren't triggered
else:
  #User input for choice
  choiceC = input('Camping in your favorite local park, you come across a variety of wild foods to choose from and decide to try one!  ..... Choose A, B or C ...\n\n A: red and black berry\n B: neon green mushroom\n C: red cherry')
  #Outcome for red and black berry
  if choiceC == "A".lower():
    print('Thinking a sweet red berry would be a good snack, you forgot that black spotted means it is bad for consumption! You get sick and your camping trip is ruined.')
  #Outcome for a neon green muchroom lol
  elif choiceC == "B".lower():
    print('Idk why you would choose a neon green mushroom, but you are now an alien. Bad bad choice.')
  #outcome for a red cherry
  else:
    print('The cherry is delicious, reminding you of childhood and picking cherries from your grandparents bush. You are nostalgic and at peace.')
                
                



