'''
Program: Guessing Game
Filename: guessingGame-tRaj-00.py
Author: Tushar Raj
Description: This guessing game is based on an algorithm called a “binary search”. The goal is to guess a number within a certain range in the fewest number of guesses
Revisions: No revisions made
'''
import math #Math module is imported for log function to work
import random #random module is imported to generate secret value in program
#There are no literal constraint
#There are no class defined

def inputdata(number): #checks the user input is correct
    '''
    This function accepts the input from the user and checks if the value contains any special character,alphabets.It even checks that the value is not negative for the number of sequence
    Input: user input from the console which is string type
    output: returns converted strings into float/int data type
    '''
    count = 1
    special = "!@#$%^&*()+?_=,<>/"
    alphabet = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
    while(count): 
        if(any( i in alphabet for i in number)): #checks if the value entered in number variable is having any character or not
            print("****Entered value can not have characters. Please Enter the valid entry****\n") #prints the error message
            progress = input("Please enter if you want to continue with Guessing Game(y/n): ") #ask users if he wants to continue with program
            if( progress == 'y' or progress == 'Y' ):#checks the response of the user if its yes, asks to enter the diameter again
                number = input("\nEnter a number: ")
            if( progress == 'n' or progress == 'N' ):#exits the program if response in no
                exit()
            continue
        elif (any( i in special for i in number)): #picks up each character from the number variable and then checks in special variable if it is present, if present run this elif
            print("****Input cant have special character. Please Enter the valid entry****\n")
            progress = input("Please enter if you want to continue with Guessing Game(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nEnter a number: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        elif (int(float(number))<=0): #checks if value is less than or equal to zero
            print("****Input cant be Zero or less than zero. Please Enter the valid entry****\n")
            progress = input("Please enter if you want to continue with Guessing Game(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nTry entering last value again: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        else:
            return int(float(number))



### Step 1: Announce, prompt and get Response
print("Guessing Game:")
print("Guess the Secret Number\n")
data = input("Enter the maximum number in the range: ")

#checking the user input is valis of not for the range value
checked_data = inputdata(data)

#Creating a random number which need to be prdicted by the user
secretNumber = random.randint(1,checked_data)

print("\nTry to guess a secret number from 1 to {0} (inclusive).\n".format(checked_data))

#Calculating the number of guess allocated for the user
nGusses =  int(math.log2(checked_data)+1)

#Prompt user to get the number for average
for i in range(nGusses):
    if(nGusses - i != 1): #check if the number of guess is greater than 1 to maintain the pluraliry of the comments
        print("Your have {} guesses available.".format(nGusses-i)) #display the number of guess available
        guessInput = input("Enter your guess number: ") #accept the number guess number
        checked_guessInput = inputdata(guessInput) #check if the data entered by use is appropriate
        if(checked_guessInput<secretNumber): #check the input is greater or smaller and display the appropriate comment
            print("The secret number is more than {}.".format(guessInput))
        elif(int(checked_guessInput) == int(secretNumber)):
            print("Correct. Well done!")
            break #break if the user have predicted the guess number
        else:
            print("The secret number is less than {}.".format(guessInput))
    else: #check if only one attempt is left then change plural words to singular
        print("Your have {} guess available.".format(nGusses-i))
        guessInput = input("Enter your guess number: ")
        checked_guessInput = inputdata(guessInput)
        if(checked_guessInput<secretNumber):
            print("The secret number is more than {}.".format(guessInput))
        elif(int(checked_guessInput) == int(secretNumber)):
            print("Correct. Well done!")
            break
        else:
            print("The secret number is less than {}.".format(guessInput))
else: #if the user is not able to find the guess number the execute the else statement
    print("\nSorry. No more guesses are allowed.")
    print("The secret number was {}.".format(secretNumber))

###Anounce that Guess Game has ended
print("\n\n****Guessing Game program ended****")
