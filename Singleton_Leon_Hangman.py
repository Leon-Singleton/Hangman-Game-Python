# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:00:31 2020

@author: Leon Singleton
"""

import random 
 
def playHangman():
    
   wordList = []
   
   #reads from the word list text file and creates a list of all the words 
   with open('word_list.txt', encoding='utf-8-sig') as file:
    for line in file:
        for word in line.split():
          wordList.append(word)

    #selects a random word from the word list
    randomWord = random.choice(wordList)
    
    #outputs the random word replacing all letters with the '*' character    
    print("The word to guess is: " + ('*' * len(randomWord)))
   
    #List to store the current guesses that have been made
   guesses = ''
   #Sets the number of guesses allowed per game
   guessesAllowed = 7
    
   #Stores the number of incorrect guesses the player has made
   incorrectGuesses = 0   
   
   #Game ends when number of incorrect guesses is equal to the number of 
   #guesses allowed
   while incorrectGuesses < guessesAllowed:
        
        won = 0
        #used to build a string containing a starred form of the word with 
        #stars removed where a correct letter has been guessed
        output = "The word is currently: "
        
        #Checks whether each guess matches any letters in the word
        for char in randomWord: 
            
            if char in guesses:
                
                output += (char)
            
            else:
                
                output += ("*")
                won+=1
        
        #If all the guesses match letters in the word then the game neds
        if won == 0:
            print ("The word was", randomWord)
            print ("congratulations you win") 
            
            #exits the game
            break     
        
        print(output)
        #Asks for the user to enter their next guess
        guess = input("Please enter your next guess: ")
        
        #Adds the new guess to the current list of guesses
        guesses += guess
        
        if guess not in randomWord:
            
            incorrectGuesses +=1
            
            print("Incorrect guess")
            
            print("You have", + (guessesAllowed -incorrectGuesses), " guesses remaining")
        
        if incorrectGuesses == guessesAllowed:
            print("The word was: ", randomWord)
            print("you lose")

playHangman()
    
