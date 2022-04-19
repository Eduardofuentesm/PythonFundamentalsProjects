import os
import time

#Ask a user for their personal information in a single round of questions. It then verifies that the information entered is valid. Finally, it prints a summary of all the information that has been entered.
def main():

    name = input('What is your name?: ')
    name = name
    last_name = input('What is your last name?: ')
    last_name = last_name
    birthday = input('When is your birthday?: ')
    birthday = birthday
    direction = input('What is your direction?: ')
    direction = direction
    goals = input('What are your goals?: ')
    goals = goals

    #When everything is entered correctly, a summary like the one shown below appears:
    if name.isalpha() and last_name.isalpha:
        print('Your name is: ' + name)
        print('Your last name is: ' + last_name)
        print('Your birthday is: ' + birthday)
        print('Your direction is: ' + direction)
        print('Your goals are: ' + goals)
    #For example: What is your name? If the user enters *, it should indicate that the entry is incorrect and the user is prompted to correctly enter a valid name.
    else: 
        print('\nEscribiste mal tu nombre o tu apellido, intenta de nuevo')
        time.sleep(2)
        os.system("clear")
        main()


if __name__ == '__main__':
    main()