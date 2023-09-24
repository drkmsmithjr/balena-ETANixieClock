#!/usr/bin/python

import pickle
import sys


# load the destinations and origins

BurninFile = "/data/burnin.txt"

# main loop
# the datafile can be at another location .. for debug
# for example SetupBurnin.py [datafile]


if len(sys.argv) < 2:
#blank digits
   BurninFile = "/data/burnin.txt"
# python SetupBurnin.py [datafile]
elif len(sys.argv) == 2:
   BurninFile = sys.argv[1]

# check to see if the locations.txt file exists.  If it does not then create it.   
# otherwise, read
try:
   with open(BurninFile,'r') as f:
      BurnInMinutes,BurnInStart,BurnInStop,DigitsToTest,DigitsTimeTest = pickle.load(f)
except:
    BurnInMinutes = 20
    BurnInStart = 20
    BurnInStop = 1
    DigitsToTest =   [0  ,3  ,4  ,9  ,1  ,2  ,5  ,6  ,7  ,8]
    DigitsTimeTest = [0.6,0.3,0.3,0.7,0.1,0.7,0.1,0.1,0.1,0.2]

while True:

   print("\n\n===================================================================")
   print("SET THE BURNIN FOR CLOCK \n")
   print("BurnInMinutes = %s" % BurnInMinutes)
   print("BurnInStart to BurnInStop (24 hour) = %s - %s" % (BurnInStart,BurnInStop))
   print("DigitsToTest = %s" % DigitsToTest)
   print("DigitsTestTime = %s" % DigitsTimeTest)

   print("\n[S]: Start Time:")
   print("[P]: Stop Time:")
   print("[M]: Burnin Minutes:")
   print("[D]: Digits to Test: ")
   print("[T]: Digit Test Time:")
   print("[W]: Write the burnin file")
   print("[x]: Write and exit")
   
   raw_option = raw_input("")
   if raw_option == "S":
      while True:
          raw_option2 = raw_input("Enter New Start time (24hr format 0-24): ")
          try:
              c = int(raw_option2)
              if c >= 0 and c <= 24:
                 BurnInStart = c    
                 break
              else:
                 raise Exception("The incorrect hour was entered - must be range 0-24")
          except (ValueError,Exception) as error:
              print(error)
   if raw_option == "P":
      while True:
          raw_option2 = raw_input("Enter New Stop time (24hr format 0-24): ")
          try: # test condition
              c = int(raw_option2)
              if c >= 0 and c <= 24:
                 BurnInStop = c    
                 break
              else: # raise error is on within range
                 raise Exception("The incorrect hour was entered - must be range 0-24")
          except (ValueError,Exception) as error:
              print(error)
   if raw_option == "M":
      while True:
          raw_option2 = raw_input("Enter New Burin Minutes: ")
          try: # test condition
              c = int(raw_option2)
              if c >= 0 :
                 BurnInMinutes = c    
                 break
              else: # raise error is on within range
                 raise Exception("The incorrect minutes was entered - must be greater than zero")
          except (ValueError,Exception) as error:
              print(error)
   if raw_option == "D":
      tempDigitsToTest = []
      for x in range(1,11):
          while True:
              raw_option2 = raw_input("Enter %s Digit to Test " % x)
              try: # test condition
                  c = int(raw_option2)
                  if c in tempDigitsToTest:
                     raise Exception("You Already entered this Digit")
                  if c >= 0 and c <=9  :
                     tempDigitsToTest.append(c)    
                     print("Current Digits %s" % DigitsToTest)
                     print("New %s" % tempDigitsToTest)
                     break
                  else: # raise error is on within range
                     raise Exception("Incorrect Digit - must be within 0 - 9")
              except (ValueError,Exception) as error:
                  print(error)
      DigitsToTest = tempDigitsToTest 
   if raw_option == "T":
      tempTimeToTest = []
      for x in range(0,10):
          while True:
              raw_option2 = raw_input("Enter Digit %s's Test Time " % DigitsToTest[x])
              try: # test condition
                  c = float(raw_option2)
                  if c >= 0 and c <=3  :
                     tempTimeToTest.append(c)    
                     print("New %s" % tempTimeToTest)
                     break
                  else: # raise error is on within range
                     raise Exception("Incorrect Digit Test Time - must be within 0 - 3")
              except (ValueError,Exception) as error:
                  print(error)
      DigitsTimeTest = tempTimeToTest 
   elif raw_option == "W":
      with open(BurninFile,'w') as f:
         pickle.dump((BurnInMinutes,BurnInStart,BurnInStop,DigitsToTest,DigitsTimeTest),f)
   elif raw_option == "x":
      with open(BurninFile,'w') as f:
         pickle.dump((BurnInMinutes,BurnInStart,BurnInStop,DigitsToTest,DigitsTimeTest),f)
      break
   else:
      print("The choice was not valid, please try again")

