# conditonals - logic, storyline, etc

# init turtle + screen
import turtle as trtl
import time
import random as rand
import animations
screen_h = 400
screen_w = 420

# init story + character
wn = trtl.Screen()
cac_jck = trtl.Turtle
wn.setup(width=screen_w, height=screen_h)
cactus_img = "/Volumes/Classes/High/ITAMS/TCalabresi/Period2/Group/gavin, hamza, rayyan/cactus.gif"
wn.addshape(cactus_img)
cac_jck_alive = True
story_progress = 0

# 1 — Beginning
print("Welcome to this adventure game!\nYou will be Cactus Jack looking for a jewel.\nThis is a choice game, so if you pick the wrong choice, YOU DIE!")
# 2 - Ghost 
choice1 = input("You have encountered a ghost, oh dear god. You have 2 options.\nType 't' to talk to the ghost, or type 'f' to fight the ghost: ")
if choice1 == 't':
   print("You have talked to the ghost.\nThe ghost tells you that you need to go get a special jewel and eat it before sundown to turn back into a non-cactus.")
#3 - Turtle
   choice2 = input("Cactus Jack has started his adventure, and you are heading towards a cave. To get there, you have to go through the treacherous desert. However, you've encountered a turtle.\nType 'e' to eat the turtle, or type 'b' to befriend the turtle: ")
   if choice2 == 'e':
     print("You tried to eat the turtle, but the turtle fights back and snaps you in half. Then he eats you.\nGAME OVER!")
     quit()
   elif choice2 == 'b':
      print("You have attempted to befriend the turtle and...SUCCESS! You have gained a companion.")
      time.sleep(1)
# 4—mid-adventure
      print("almost halfway there! You and you're turtle friend approach the cave, but a wild John Cena has appeared (you can't see him).\n You and your turtle friend decide to either fight him together or alone")
      choice3 = input("\n Type either 't' to fight together or 'a' to fight alone: ")
      if choice3 == 't' or 'a':
         print("OH NO! The turtle decides to take on the wild John Cena by himself. He pushes you to side and takes him on.")
         time.sleep(1)
         print("He doesn't survive.")
         time.sleep(1)
# 5 - Ad Break
         print("OK, I feel kinda bad for the turtle dying.\n You have 2 options to help your turtle friend:\n  1. Bury him and promise to avenge him (b)\n  2. Play a guess the number game for a chance to bring him back (p)")
         choice4 = input("Choose wisely: ")
         if choice4 == 'b':
            print("You bury the turtle and move on to the cave. It's entrance is super dark and scary (oh noes)")
            print("After avoiding some evil looking spiders, you find two jewels: one is red and the other is blue (TOTALLY NOT A MATRIX REFERENCE)")
            choice5 = input ("Choose 'r' for the red jewel and 'b' for the blue jewel")

         elif choice4 == 'p':
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
               print("ha, you wasted your time")
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

elif choice1 == 'f':
   print("You tried to fight the ghost. You have been obliterated and turned into a cactus smoothie.\nGAME OVER!")
   quit()

 
# 6—Cave Found -- OPTIONAL/DELEGATED
   # - we finally get to cave and go inside, find a spider in the cave and try to dodge (can prob use key presses to avoid the spooder)
   # - animation here - spomg to make quick

# 7—Jewel found
   # - Find jewel— if we have turtle friend then he eats the jewel and becomes supreme turtle, otherwise he defeats us and eat the jewel and then becomes the ghost from earlier (eyes turn red)
   # -animation is turtle eating and then become ghost and then eyes turn red


# screen persist