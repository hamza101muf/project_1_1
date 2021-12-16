### conditonals - logic, storyline, etc

# init turtle + screen
import time
import turtle as trtl
import random as rand
#import animations as anim


screen_h = 2100
screen_w = 2000
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)

#----- def screen size vars
screen_h = 2100
screen_w = 2000

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)

# img init for 0th section
def chc_0():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/cac_jack_solo.gif") 

# img init for 1st section
def chc_1():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/cac_jack_ghost.gif")

# img init for 2nd section
def chc_2():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/jack_landscape_left.gif")

# SKIP #3

# img init for 4th section
def chc_4():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/trtl_grv.gif")

def spdr():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/spdr.gif")

def cave():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/jack_cv_entr.gif")

def choice():
    wn.bgpic("/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/project_1_1/choose.gif") 

# 0 — Beginning
print("Welcome to this adventure game!\nYou will be a cactus man looking for a jewel.\nThis is a choice game, so if you pick the wrong choice, YOU DIE!")
# 1 - Ghost
chc_0()
choice_1 = input("You have encountered a ghost, oh dear god. You have 2 options.\nType 't' to talk to the ghost, or type 'f' to fight the ghost: ")
if choice_1 == 't':
   chc_1()
   print("You have talked to the ghost.\nThe ghost tells you that you need to go get a special jewel and eat it before sundown to turn back into a non-cactus.")
# 2 - Turtle
   choice_2 = input("You have started your adventure, and you are heading towards a cave. To get there, you have to go through the treacherous desert. However, you've encountered a turtle.\nType 'e' to eat the turtle, or type 'b' to befriend the turtle: ")
   time.sleep(1)
   chc_2()
   if choice_2 == 'e':
      time.sleep(1)
      print("You tried to eat the turtle, but the turtle fights back and snaps you in half. Then he eats you.\nGAME OVER!")
   elif choice_2 == 'b':
      chc_2()
      print("You have attempted to befriend the turtle and...SUCCESS! You have gained a companion.")
      time.sleep(1)
# 3 — mid-adventure
      print("Almost halfway there! You and your turtle friend approach the cave, but a wild John Cena has appeared (you can't see him).\n You and your turtle friend decide to either fight him together or alone")
      choice_3 = input("\n Type either 't' to fight together or 'a' to fight alone: ")
      if choice_3 == 't' or 'a':
         print(">>>>OH NO!<<<< The turtle decides to take on the wild John Cena by himself. He pushes you to side and takes him on.")
         time.sleep(1)
         print("He doesn't survive.")
         chc_4()
         time.sleep(1)
# 4 - Ad Break
         print("OK, I feel kinda bad for the turtle dying.\n You have 2 options to help your turtle friend:\n  1. Bury him and promise to avenge him (b)\n  2. Play a guess the number game for a chance to bring him back (p)")
         choice_4 = input("Choose wisely: ")
         if choice_4 == 'b':
            print("You bury the turtle and move on to the cave. It's entrance is super dark and scary (oh noes)")
      # 4a — Jewel found
         # 5 - Ending
            choice_5 = input("After avoiding some evil looking spiders, you find two jewels: one is red and the other is blue (TOTALLY NOT A MATRIX REFERENCE) \n\n   1. Choose 'b' for the blue jewel \n\n   2. Choose 'r' for the red jewel \n\n")
            spdr()
            time.sleep(1)
            cave()
            time.sleep(1)
            choice()
            if choice_5 == "r":
               print("You eat the red jewel, nothing happens, you cry. Then everything just becomes still\n\n the ghost stands in front of you, his eyes RED")
               print("Cactus don't exist anymore, but they do. I AM CACTUS. YOU ARE CACTUS. CACTUS. CACTUSSS. CaCTus!!!!")
            elif choice_5 == "b":
               print("You are dead. The blue jewel was actually a moldy spooder. Spooder will consume you. >:)")
      # 4b - Minigame + turtle live
         elif choice_4 == 'p':
            print("OK, let's get started then")
            # start num guess game
            secret = rand.randint(1,21)
            num_guesses = 0
            password = input("Do you know the password: ")
            # check password
            if password == 'turtles':
               print("correct, here's the secret number", (secret+2))
            elif password == 'no':
               print("Semi-acceptable, secret num is close to this number", secret-2 )
            else:
               print("Incorrect, move on.")
            #start num game
            guess = int(input('I have a number between 1 and 20, start guessing: '))
            if guess == secret:
               print("Congrats! The turtle is alive again and now comes with you to the cave!")
            else:
               if num_guesses == 0:
                  num_guesses += 1
                  if guess == secret:
                     print('Right, my number is', guess, end='!\n')
                     print("Congrats! The turtle is alive again and now comes with you to the cave!")
                     num_guesses+=10
                  else:
                     print('Wrong, you have ', 3-num_guesses, " guesses left!")
                     if guess > secret:
                        print("Guess lower")
                     else:
                        print("Guess higher")
               if num_guesses == 1:
                  guess = int(input("What is your 2nd guess:"))
                  num_guesses += 1
                  if guess == secret:
                     print('Right, my number is', guess, end='!\n')
                     print("Congrats! The turtle is alive again and now comes with you to the cave!")
                     num_guesses+=10
                  else:
                     print('Wrong, you have ', 3-num_guesses, " guesses left!")
                     if guess > secret:
                        print("Guess lower")
                     else:
                        print("Guess higher")      
               if num_guesses == 2:
                  guess = int(input("What is your final guess:"))
                  num_guesses +=1
                  if guess != secret:
                     print('Wrong, you have ', 3-num_guesses, " guesses left!")
                     print('The secret number was: ', secret)
                     print("Well, let's continue...")
                  else:
                     print('Right, my number is', guess, end='!\n')
                     print("Congrats! The turtle is alive again and now comes with you to the cave!")
# 5 - Ending
            choice_5 = input("Choose 'r' for the red jewel and 'b' for the blue jewel")
            spdr()
            time.sleep(1)
            cave()
            time.sleep(1)
            choice()
            if choice_5 == "r":
               print("You eat the red jewel, nothing happens, you cry. Then everything just becomes still\nthe ghost stands in front of you, his eyes RED")
               print("Cactus don't exist anymore, but they do. I AM CACTUS. YOU ARE CACTUS. CACTUS. CACTUSSS. CaCTus!!!!\n ERROR 504 - 348RT3984957")
            elif choice_5 == "b":
               print("You are dead. The blue jewel was actually a moldy spooder. Spooder will consume you. >:)")
elif choice_1 == 'f':
   print("You tried to fight the ghost. You have been obliterated and turned into a cactus smoothie.\nGAME OVER!")

# screen persist
wn = trtl.Screen()
wn.mainloop()