
from operator import truediv
from optparse import Option
from turtle import color
import console.utils
import colorama
import time
import sys
import math
import os
import art


scene = int(0)
Art = art.text2art("The school", font='block', chr_ignore=True)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def type(text):
  words = text
  for char in words:
    time.sleep(0.04)
    sys.stdout.write(char)
    sys.stdout.flush()
blank = 'print("")'
usernameset = 0
Question = 0
cls()
print(colorama.Fore.LIGHTBLACK_EX + f"{Art}")
type(colorama.Fore.RESET + "Press anything to start")
console.utils.wait_key()
cls()
#Intro

type("Input your new name")
exec(blank)
username = input()



def scene2(): #The second scene
  print(colorama.Fore.RESET + f"You leave the room *Type help for help")
  while Question == 0:
    waitforquestion = input()
    OptionList = "|Leave the room|Call for help|Turn on the lights|"
    if waitforquestion == ("help"):
      print(colorama.Fore.LIGHTRED_EX + "Your current options are:")
      print(colorama.Fore.RESET + f"{OptionList}")






def scene1(): #The first scene
  exec(blank)
  time.sleep(2)
  cls() 
  type("You wake up in a dark room *Type help for help")
  exec(blank)
  time.sleep(0.4)
  exec(blank)
  OptionList = "|Leave the room|Call for help|Turn on the lights|"
  while Question == 0:
    waitforquestion = input()
    if waitforquestion == ("help"):
      print(colorama.Fore.LIGHTRED_EX + "Your current options are:")
      print(colorama.Fore.RESET + f"{OptionList}")
    if waitforquestion == ("Leave the room"):
      scene2()
      break
    if waitforquestion == ("Call for help"):
      print(colorama.Fore.LIGHTRED_EX + f"You call for help but no one is here")
      print(colorama.Fore.RESET)
    if waitforquestion == ("Turn on the lights"):
      print(colorama.Fore.LIGHTBLUE_EX + "The room is a classroom with computers, it seems that the windows are boarded up.")
      print(colorama.Fore.RESET)

    







while usernameset == 0:
  if username != (""):
    type(f"Your new name will be: {username}" )
    scene1()
    break
  else:
    type("username cannot be empty type again")
    exec(blank)
    username = input()
    





