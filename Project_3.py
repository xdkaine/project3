#saved

# note i'll be referencing many functions from patch 1.1 since most of the functionalities are actually good

# patch 2.1 will rely more on the profile system created to intergrate well with the user.

# LIBRARIES!

import os
import time
import random

# THESE ARE FOR THE PROGRAM TO REFER BACK TO WHEN IN PROFILE CREATION TO ADAPT THEIR RESPONSE
programNames = ["Adam", "Bob", "Charlie", "Drake", "Evan", "Mike", "Luke"]
programColors = ["Azure", "Blue", "Navy Blue", "Yellow", "Orange", "White", "Gray", "Black", "Brown", "Red", "Pink", "Purple", "Cyan", "Green", "Black"]
primenumberlist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
existingProfiles = ['Admin', 'DarthVeigar69', 'Pabbler']

# COLOR CODING PROGRAM'S RESPONSES TO "POP"
# referenced from patch 1.1
class popcolor:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREENNAMES = '\033[92m'
    YELLOWNOTIFY = '\033[93m'
    RED = '\033[91m'
    WHITEOG = '\033[0m'
    BOLDEDWHITE = '\033[1m'
    UNDERLINE = '\033[4m'

# recoded
def CreateAProfile():
  Question1 = ("What is your Name?  ")
  Question2 = ("\nWhat is your Gender? (Male/Female)  ")
  Question3 = ("\nHow old are you?  ")
  Question4 = ("\nIs this information correct? (Y/N)  ")
  Question5 = ("Which question was it? (1, 2, 3)  ")
  ChooseMyProgramName = random.choice(programNames)
  print("Ok, we are going to ask you some questions.")
  def newprofile():
      NewProfile1 = input("Are you ready? (Y/N)  ")
      if NewProfile1 == "Y":
          print(popcolor.PURPLE+"Starting...",popcolor.WHITEOG)
          
          def name():
             name1 = input(Question1)
             if name1  == ChooseMyProgramName:
                 print("Wow! What are the chances we have the"+ popcolor.GREENNAMES+"same name!",popcolor.WHITEOG)
             elif name1 != ChooseMyProgramName:
                 print("Ok, thats great my name is", popcolor.GREENNAMES + ChooseMyProgramName, popcolor.WHITEOG)
          name()
          def gender():
              gender1 = input(Question2)
              print("Great, I am neither as"+popcolor.GREENNAMES,"I am just a program.",popcolor.WHITEOG)
          gender()
          def age(): 
              age1 = int(input(Question3))
              print("Excellent, "+ popcolor.GREENNAMES +"I am actully", random.randrange(1,10000), "years old", popcolor.WHITEOG)

          age()
              
          time.sleep(1)
          print("Ok, I have gathered some information here, let me repeat it back.")
          time.sleep(1)

          print("You are a", age,"year old", gender,"named,",age)
          check = input(Question4)
          
          if check == "Y":
              time.sleep(1)
              print("Great, we will"+popcolor.GREENNAMES+" end here and save your profile", popcolor.RED + "for this session.", popcolor.WHITEOG)
              time.sleep(2)
              print("We will be proceeding to the"+ popcolor.GREENNAMES+" Game Portion of the Program.", popcolor.WHITEOG)
              time.sleep(2)
              print(popcolor.PURPLE+"Loading...."+popcolor.WHITEOG)
              games()


          if check == "N":
             asking= input(Question5)
             if asking == "1":
                 name = input(Question1)
                 print("Ok, you are a", popcolor. age, "year old", gender,"named,",name)
                 time.sleep(1)
                 print("Great, we will", popcolor.GREENNAMES,"end here and save your profile", popcolor.RED + "for this session.", popcolor.WHITEOG)
                 time.sleep(2)
                 print("We will be proceeding to the", popcolor.GREENNAMES+"Game Portion of the Program.", popcolor.WHITEOG)
                 time.sleep(2)
                 print(popcolor.PURPLE+"Loading...."+popcolor.WHITEOG)
                 games()


          elif asking == "2":
              gender = input(Question2)
              print("Ok, you are a", age, "year old", gender,"named,",name)
              time.sleep(1)
              print("Great, we will", popcolor.GREENNAMES,"end here and save your profile", popcolor.RED + "for this session.", popcolor.WHITEOG)
              time.sleep(1)
              print("We will be proceeding to the", popcolor.GREENNAMES+"Game Portion of the Program.", popcolor.WHITEOG)
              time.sleep(1)
              print(popcolor.PURPLE+"Loading...."+popcolor.WHITEOG)
              games()


          elif asking == "3":
              age = int(input(Question3))
              print("Ok, you are a", age, "year old", gender,"named,",name)
              time.sleep(1)
              print("Great, we will", popcolor.GREENNAMES,"end here and save your profile", popcolor.RED + "for this session.", popcolor.WHITEOG)
              time.sleep(1)
              print("We will be proceeding to the", popcolor.GREENNAMES+"Game Portion of the Program.", popcolor.WHITEOG)
              time.sleep(1)
              print(popcolor.PURPLE+"Loading...."+popcolor.WHITEOG)
              games()


      if NewProfile1 == "N":
          print("Pausing for 5 seconds")
          time.sleep(1) #CHANGE TO 5 in FINAL RELEASE!!!!!!!!
          print("Starting...")
          newprofile()
  newprofile()
# start
def start():
  print(popcolor.YELLOWNOTIFY+"note: the resposnes are longer than others, while using the terminal, please widen your screen!\n")

  time.sleep(1)
  print (popcolor.WHITEOG+"I don't know if I have ever seen you here before...")
  time.sleep(1)

  askForProfiles = input("Have you created a profile on here before? (Y/N)  ")
  if (askForProfiles) == "Y":
    os.system("clear")
    print (popcolor.PURPLE ,"\nCHECKING....", popcolor.WHITEOG)
    time.sleep(3)
    print(existingProfiles)
    askForWhichProfile = input("Which Profile is it?  ")
    if askForWhichProfile in (existingProfiles):
      time.sleep(1)
      print(popcolor.PURPLE +"Loading Profile...", popcolor.WHITEOG)
      time.sleep(3)
      os.system("clear")
      print("Hello "+ askForWhichProfile +"!\nWelcome Back!")
      games()


    elif askForWhichProfile != (existingProfiles):
      #time.sleep(1)
      print(popcolor.PURPLE+"That Profile does not seem to exist.",popcolor.WHITEOG)
      time.sleep(3)
      askProfileAgain = input("Would you like to try again? Y/N  ")
      if askProfileAgain == "Y":
        askForWhichProfile()
      elif askProfileAgain == "N":
        os.system("clear")
        CreateAProfile()

  elif (askForProfiles) == "N":
    os.system("clear")
    print (popcolor.PURPLE,"\nCREATING....",popcolor.WHITEOG)
    CreateAProfile()

def games():
  choose = input("(1) Guess the Lottery Winner\n(2) What number am I think of?\n(3) Prime Number Checker\n(4) Calculator\n> ")
  if choose == "1":
    def LotterySystem():
      userlist = ["Molly", "Amy", "Claire", "Tanner", "DeAndre"]
      winnerpick = random.choice(userlist)
      print (userlist)
      guesses = 1
      askthem = input("Who do you think won the lottery? > ")
      for users in userlist:
        print(users + ", ", end="")
        while input("> ") != winnerpick:
          print ("Guess Again!")
          guesses += 1
        print("Congratulations, You've gussed in", guesses,"tries!")
        return guesses
      time.sleep(3)
    LotterySystem()
    time.sleep(4)
    games()
  elif choose == "2":
    hidden = random.randrange(1,50)
    randNum =  random.randrange(1,50)
    def game2():
      guess = int(input("Pick a Number:"))
      while guess != randNum:
        guess = int(input("Try Again!: "))
        if guess == randNum:
             print ("Good Job")
             os.system("clear")
             games()
        if guess < randNum:
          print ("A little higher...")
          if guess > randNum:
            print ("A little lower...")
    game2()
  elif choose == "3":
   def game3():
    print("Welcome to the Prime Number Checker")
    asker = int(input("What number do you want to check? "))
    for dd in primenumberlist:
        if dd == asker:
            print(popcolor.RED, "YES", popcolor.WHITEOG)
            time.sleep(2)
            os.system("cls")
            games()
        elif dd != asker:
            print(popcolor.RED, "NO", popcolor.WHITEOG)
            time.sleep(2)
            os.system("cls")
            games()
   game3()

  elif choose == "4":
      def game4():
          def add():
              value1 = int(input("What is Value A? "))
              value2 = int(input("What is Value B? "))
              sum = int(value1) + int(value2)
              print(sum)
              time.sleep(3)
              games()
          def subtract():
              value1 = int(input("What is Value A? "))
              value2 = int(input("What is Value B? "))
              difference = int(value1) - int(value2)
              print(difference)
              time.sleep(3)
              games()
          def multiply():
              value1 = int(input("What is Value A? "))
              value2 = int(input("What is Value B? "))
              product = int(value1) * int(value2)
          functions = input("What function do you want to use?\n(0) Return Back\n(1) Add\n(2) Subtract\n(3) Multiply\n ")
          if functions == "1":
              add()
          elif functions == "2":
              subtract()
          elif functions == "3":
              multiply()
          elif functions == "0":
              games()
      game4()




start()