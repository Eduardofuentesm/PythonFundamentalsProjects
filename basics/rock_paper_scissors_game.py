#Author: Eduardo Fuentes
#Twitter: @edufdev

#In this game, the user has the first opportunity to choose the option between rock, paper, scissors. After the computer selects between the two remaining options (randomly), the winner is decided according to the rules.

import random
import os
import time

def main():

    print("***Winning Rules of the Rock paper scissor game as follows: ***")
    print("\n\tRock vs paper -> paper wins")
    print("\tRock vs scissor - >Rock wins")
    print("\tpaper vs scissor - >scissor wins") 
  
    while True: 
        print("\n\tEnter choice (1 - 3) \n\n \t1. Rock \n \t2. paper \n \t3. scissor \n") 
        
        
        choice = int(input("\n\tUser turn: "))
    
        
        
        
        
        
        while choice > 3 or choice < 1: 
            choice = int(input("\n\tenter valid input: ")) 
            
    
        
        
        if choice == 1: 
            choice_name = 'Rock'
        elif choice == 2: 
            choice_name = 'paper'
        else: 
            choice_name = 'scissor'
            
        
        print("\n\tuser choice is: " + choice_name) 
        print("\n\tNow its computer turn.......")
        time.sleep(3)
        print()
    
        #In this set, the built-in function "randint()" is used to generate a random integer value within the given range.
        
        
        comp_choice = random.randint(1, 3) 
        
        
        
        while comp_choice == choice: 
            comp_choice = random.randint(1, 3) 
    
        
        
        if comp_choice == 1: 
            comp_choice_name = 'Rock'
        elif comp_choice == 2: 
            comp_choice_name = 'paper'
        else: 
            comp_choice_name = 'scissor'
            
        print("\n\tComputer choice is: " + comp_choice_name)
        time.sleep(2) 
    
        print(f'\n\t{choice_name} V/s {comp_choice_name}')
        time.sleep(2)
    
        
        if((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice ==1 )): 
            print("\n\tpaper wins => ", end = "") 
            result = "paper"
            time.sleep(2)
            
        elif((choice == 1 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)): 
            print("\n\tRock wins =>", end = "") 
            result = "Rock"
            time.sleep(2)
        else: 
            print("\n\tscissor wins =>", end = "") 
            result = "scissor"
            time.sleep(2)
    
        
        if result == choice_name: 
            print("\n\t*** User wins ***")
            time.sleep(2) 
        else: 
            print("\n\t*** Computer wins ***")
            time.sleep(2)
        menu()


def menu(): 
          
    print("\n\tDo you want to play again?(Y/N)") 
    ans = input()
    time.sleep(2)
    os.system("clear")

    if ans == 'n' or ans == 'N':
        
        print("\n\tThanks for playing\n")
        exit()
    time.sleep(2)


if __name__ == '__main__':
    main()
    