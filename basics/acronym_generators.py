def main():

    user_input = input('Enter a phrase: ') # The user input has been stored in a variable "user_input".
    phrase = (user_input.replace('of', '')).split() #Here in "user_input.replace('of', '')" we are using the ".replace()" function to ignore 'of' from the input, if it exists, And then we use the ".split()" function to split the string into individual words and store them as a list in the "phrase" variable.
    acronym = "" #We need an empty string variable to store our acronym

    #Here in "acronym = acronym + word[0]", we are cutting the first letter of the words stored in "phrase" using the cut operator and adding it to our variable "acronym".
    for word in phrase:
        #We are also using the ".upper()" function to capitalize the acronyms.
        acronym = acronym + word[0].upper()
    # Finally, just add a "print" statement that will print the acronym on the console.
    print(f'Acronym of {user_input} is: {acronym}')

if __name__ == '__main__':
    main()