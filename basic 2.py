import prettytable
import datetime
import random
calendar = datetime.datetime.now()
print("welcome to central bank ATM")  #ATM program
restart = "yes"
balance = 5000
chances = 3


while chances > 0:
    pin = int(input("enter the pin"))
    if pin == 1234:
         print("the entered pin is correct\n")
         while restart not in ("NO,no"):
              print("press option 1 to withdrawl")
              print("press option 2 for payment")
              print("press option 3 for balance enquiry")
              print("press option 4 for exit and remove card")
              option  = int(input("what option do you like to choose?"))


              if option == 1:
                 a = True
                 while a:
                  withdrawl = int(input("how much amount do you like to withdrawl\n"))
                  if withdrawl in random.sample(range(0,20001,100),200):
                     balance = balance - withdrawl
                     receipt = input("would you like to get receipt?\n enter yes for get recipt \n if not enter no")
                     if receipt == "yes":
                       my_table = prettytable.PrettyTable(["central bank ATM "])
                       my_table.add_row(["cental bank of ATM"])
                       my_table.add_row([f"amount drawn :{withdrawl} in {calendar}"])
                       my_table.add_row([f" your current balane is {balance}"])
                       print(my_table)
                       a = False
                       restart = input("would you like to go back to main menu?")

                       if restart in ("NO,no"):
                           print("Thank you for visiting central bank ATM")
                           break
                     else:
                      print("your balance is,", balance,"\n")
                      a = False
                      restart = input("would you like to go back to main menu?")
                      if restart in ("NO,no"):
                        print("Thank you for visiting central bank ATM")
                        break
                  else:
                     print("invalid amount\n please enter a valid currency notes (100,200,500,2000)")


              elif option == 2:
                  payment = int(input("how much amount do you like to pay?\n"))
                  balance_1 = payment + balance
                  print("successfully paid")
                  receipt = input("would you like to get receipt?\n enter yes for get recipt \n if not enter no")
                  if receipt == "yes":
                      my_table = prettytable.PrettyTable(["central bank ATM "])
                      my_table.add_row([f"amount paid :{payment} in {calendar}"])
                      my_table.add_row([f" your current balane is {balance_1}"])
                      print(my_table)
                      restart = input("do you like to go back to main menu?")
                      if restart in ("NO,no"):
                          print("Thank you for using central bank ATM")
                          break
                  else:
                    print("your balane is,\n", balance)
                    restart = input("do you like to go back to main menu?")
                    if restart in ("NO,no"):
                      print("Thank you for using central bank ATM")
                      break


              elif option == 3:
                  receipt = input("would you like to get receipt?\n enter yes for get recipt \n if not enter no")
                  if receipt == "yes":
                      my_table = prettytable.PrettyTable(["central bank ATM "])
                      my_table.add_row([f" your current balane is {balance}"])
                      my_table.add_row([f" last seen in ATM {calendar}"])
                      print(my_table)
                      restart = input("do you like to go back to main menu?")
                      if restart in ("NO,no"):
                          print("Thank you for using central bank ATM")
                          break
                  else:
                   print("your balance is\n", balance)
                   restart = input("do you like to go back to main menu?")
                   if restart in ("NO,no"):
                       print("Thank you for using central bank ATM")
                       break


              elif option == 4:

                  remove = input("do you  like to remove you card?")
                  if remove == "yes":
                    print("thank you for using central bank ATM")
                    break
              else:
                  print(f" print a valid option available")
                  continue


    if pin != 1234:
      print("incorrect password, enter a valid password")
      chances = chances - 1
      if chances == 0:
        print("sorry, your entered password is not valid try next time")
































