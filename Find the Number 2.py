#Created on Sun Sep  6 19:55:17 2020
#@author: danny
#"""
# Find the Number 2

user_input = input("\n Hello my friend, type any number between 0 and 1000. Try to find the right one.\n >>> ")

# Answer is 303
x = 303

if user_input.isdigit():
    user_input = int(user_input)

    if user_input == x:
        print('Wow bravo you\'r too good')

    elif 303 < user_input <= 1000:
        print("Number too high")
    
    elif 0 <= user_input < 303:
        print("Number too low")
    
    elif user_input > 1000:
        print('You\'r way out buddy!')
    
else:
    print('You just broke the game') 

    

  
  
