import random

import word_list
import hangman_img


class Hangman:
    """Class implementing the game of Hangman"""

    def __init__(self):
        """Initializes the Hangman game with necessary variables"""
        self.__tried_letters = []  # list - letters that were already tried
        self.__hang_word = ''  # word of the hangman
        self.__hang_state = ''  # current state of the hangman (guessed letters with _ as unguessed)
        self.__hang_letters = []  # list - letters from the hangman word
        self.__current_round = 0  # current round
        self.__current_mistakes = 0  # mistake counter
        self.__game_is_active = True  # game active status
        self.__is_first_round = True  # first round status

        self.__hang_word = self.get_random_word()
        self.start_game()

    def start_game(self):
        """Starts all the necesary function to make the game moving"""
        while self.__game_is_active:
            self.update_hang_state()
            self.__hang_letters = self.letter_scan(self.__hang_word)
            
            if '_' not in self.__hang_state:
                self.__game_is_active = False
                print(f"""
                      
correct word was: {self.__hang_word}
                
                        Y O U   W I N !
                
                """)
            elif self.__current_mistakes < 10:
                self.play_round()
            else:
                self.__game_is_active = False
                print(f"""
                
                        G A M E   O V E R

                        corect word: {self.__hang_word}
                
                """)

    def play_round(self):
        """Takes care of all the proceses needed for each round"""
        if self.__current_round == 0:
            if self.__is_first_round == True:
                self.__is_first_round = False
                print(f'''
                    Welcome to the GAME!''')
            
            print(f'''{hangman_img.HANGMAN[self.__current_mistakes]}
                  mistakes: {self.__current_mistakes}/10
                  guest letters: {', '.join(self.__tried_letters)}''')
            print(f'{self.__hang_state}')
            
            letter_memory = self.letter_check()
            self.update_hang_state(letter_memory)

    def letter_check(self):
        """
        gets players letter to guess, checks if correctly

        Returns:
            str: valid letter from the player
        """
        letter_memory = ''
        print(letter_memory)

        while letter_memory == '':
            letter_memory = input('Enter your letter: ')
            letter_memory = letter_memory.strip().lower()

            if letter_memory in self.__tried_letters:
                print(
                    'E: You already tried this letter! Try a new one'
                    )
                letter_memory = ''
            elif not letter_memory.isalpha():
                print('E: You entered invalid character! Try again')
            elif len(letter_memory) > 1:
                print('E: You entered too many letters! Try again')
                letter_memory = ''

        self.__tried_letters += letter_memory
        return letter_memory
        
    def update_hang_state(self, letter='.'):
        """
        Updates the state of the hangman word

        Args:
            letter (str): word that shows state of the game
        """
        __hang_state_memory = ''
        if letter in self.__hang_letters or letter=='.':
            for i in self.__hang_word:
                if i not in self.__tried_letters:
                    __hang_state_memory += '_'
                else:
                    __hang_state_memory += i
        else:
            print(
                f'Letter "{letter}" doesnt appear in this word, try again!'
                )
            self.__current_mistakes += 1
        self.__hang_state = __hang_state_memory

    def letter_scan(self, word):
        """
        Creates list of words that are located in each word for hangman
        
        Args:
            word (str): word to be scanned

        Returns:
            list: List of uniqe letters
        """
        local_memory = []
        for i in word:
            if i not in local_memory:
                local_memory.append(i)
        return local_memory
    
    def get_random_word(self, dict=word_list.common_words):
        """
        Chooses random word from the given dictionary

        Args:
            dict (list): List of words to choose from

        Returns:
            str: Randomly chosen word from the dictionary        
        """
        return random.choice(dict)

if __name__ == '__main__':
    Hangman()