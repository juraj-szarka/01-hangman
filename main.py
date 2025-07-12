import random
import word_dict




class hangman:
    def __init__(self):
        self.tried_letters = []  # list - letters that were already tried
        self.hang_word = ''  # word of the hangman
        self.hang_state = ''  # current state of the hangman (guessed letters with _ as unguessed)
        self.hang_letters = []  # list - letters from the hangman word
        self.current_round = 0  # current round
        self.current_mistakes = 0  # mistake counter
        self.letter_to_guess = ''  # next tried letter

        self.start_game()

    def start_game(self):
        # Starts all the necesary function to make the game moving

        
        self.hang_state = '_' * len(self.hang_word)
        print(self.hang_state)
        self.hang_letters = self.letter_scan(self.hang_word)
        if self.current_mistakes < 10:
            self.round(self.current_round)
        else:
            """
            
                    G A M E   O V E R
            
            """

    def round(self, round):
        # Takes care of all the proceses needed for each round
        if self.current_round == 0:
            print(f'''
                Welcome to the GAME!
                {self.hang_state}''')
            self.letter_check()
        elif self.current_round < 10:
            pass

    def letter_check(self):
        letter_memory = ''
        print(letter_memory)
        while letter_memory == '':
            letter_memory = input('Enter your letter: ')
            if letter_memory in self.tried_letters:
                print('E: You already tried this letter! Try a new one')
                letter_memory = ''
            elif len(letter_memory) > 1:
                print('E: You entered too many letters! Try again')
        if letter_memory in self.hang_letters:
            for i in range(len(self.hang_word)):
                if self.hang_word[i] == letter_memory:
                    self.hang_state[i] =

    def letter_scan(self, word):
        # Creates list of words that are located in each word for hangman

        local_memory = []
        for i in word:
            if i not in local_memory:
                local_memory.append(i)
        return local_memory
    
    def get_random_word(self, dict):
        return random.choice(dict)

game = hangman()