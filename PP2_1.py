'''
    Practice Questions: If statments
    Author: Johnny Zhao
    Date Created: Oct 9, 2024
    Date Last Modified: Oct 9, 2024
'''

def q1(): 
  numQ1 = int(input("In: ")) #Asking the user to input a integer
  if numQ1 % 2 == 0: #division to see if there's a remainder(to see if it's even)
    print(f"{numQ1} is even") #outputting "_their integer_ is even"
  else: #if the integer is not even(odd)
    print(f"{numQ1} is odd") #outputting "_their integer_ is even"

def q2(): 
  nameQ2 = str(input("In: ")) #Asking the user to input a name
  if nameQ2 == "Kalisz": #test is the name is "Kalisz"
    print(f"teacher") #outputting "teacher"
  else: #if the name is not "Kalisz"
    print(f"student") #outputting "student"

#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
