# creating Wordle175
# create a word game which the user has 6 chances to guess a five letter word
# from a specified word bank

# import module
import random
import os

class ScrabbleDict:
    # creates the dictionary for words in the word bank
    def __init__(self, size, filename):
        
        self.size = size
        self.key = {}
        for word in filename:
            if len(word) == self.size:
                self.key[word[0 : self.size]] = word     
                
    def check(self, word):
        '''
        Check if the word is in the dictionary
        param  - word: the word to be checked
        return - return a boolean if the word is in the dictionary
        '''        
        return word in self.key
    
    def getSize(self):
        '''
        Get the size of the dictionary
        return - returns the size of the dictionary
        '''                
        return len(self.key)
    
    def getWords(self, letter):
        '''
        Get every word that starts with a specific letter
        param  - letter: the letter that the words will start with
        return - returns a sorted list of the words that start with a specific letter
        '''                
        words = []
        for word in self.key.keys():
            if word[0] == letter:
                words.append(word)
            
        return words
    
    def getWordSize(self):
        '''
        Get the length of the words in the dictionary
        return - return the length of the words
        '''                
        return self.size
        
def getInputFile(filename):
    '''
    Read the file inputed, return content of file
    param  - filename: the file to give contents
    return - returns a list containing all the words in the file
    '''  
    file = open("D:\\VS code/New Projects/projects/" + filename, "r")
    
    contents = file.readlines()
    new_list = []
    for word in contents:
        new_list.append(word[0:5])
    file.close()
    return new_list

def main():
    
    # Task 3 main game
    # set up Wordle
    print("Wordle175:")
    answer = random.choice(file)
    answer = answer.upper()
    attempt = 0    
    print(answer)
    same_word = []
    tried_words = []
    correct_guess = False
    
    # set up while loop
    while attempt < 6 and correct_guess == False:
        
        # create letter lists
        green = []
        orange = []
        red = []     
        
        # prompt user for a 5 letter word
        guess = str(input("Attempt " + str(attempt + 1) + ": Please enter a 5 five-letter word: "))
        guess = guess.lower()
        
        # set up conditions for the guess
        if len(guess) > 5:
            print(guess.upper() + " is too long")
        elif len(guess) < 5:
            print(guess.upper() + " is too short")
        elif not word_list.check(guess):
            print(guess.upper() + " is not a recognized word")
        elif guess in same_word:
            print(guess.upper() + " was already entered")
        
        # if the guess is in the word list, find which letters are green, orange, or red
        elif word_list.check(guess):
            
            # check for the same letter
            same_letter = 0
            letter_position1 = 0
            letter_position2 = 0
            for position1 in range(0,5):
                for position2 in range(0,5):
                    if guess[position1] == guess[position2]:
                        same_letter = same_letter + 1
                        letter_position1 = position1
                        letter_position2 = position2
            
            # append letters to the green, orange or red lists
            for i in range(len(answer)):
                if answer[i] == guess[i].upper():
                    green.append(answer[i].upper())
                elif guess[i].upper() in answer:
                    orange.append(guess[i].upper())
                else:
                    red.append(guess[i].upper())
            
            # increase attempt by 1
            attempt = attempt + 1
            
            # append to the same word list, sort the green, orange, and red letter lists
            same_word.append(guess)
            green.sort()
            orange.sort()
            red.sort()
            
            # display the letter results
            tried_words.append(guess.upper() + " Green={" + ", ".join(green) + "} - Orange={" + ", ".join(orange) + "} - Red={" + ", ".join(red) + "}")
            
        
        # display the tried words
        if len(tried_words) > 0:
            for trial in tried_words:
                print(trial)
        
        # if guess is correct, break the loop
        if guess == answer.lower():
            correct_guess = True
    
    # display resulting message
    if attempt < 7:
        print("Found in " + str(attempt) + " attempts. Well done. The word is " + answer) 
    else:
        print("Sorry you lose. The word is " + answer)
    
    
    
if __name__ == '__main__':
    # task 2 testing
    # create the dictionary 

    file = getInputFile("scrabble5.txt")
    word_list = ScrabbleDict(5, file)
    
    # print("Tests: ")
    # check if this word is in the dictionary
    # print(word_list.check('aalii'))
    # print(word_list.check('kunie'))
    
    # check if getSize() works
    # print(word_list.getSize())
    
    # check if a list will return with the words starting with a specificed letter
    # print(word_list.getWords('a'))    
    main()
