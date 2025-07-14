import random
import word_dict
import hangman_img



class hangman:
    def __init__(self):
        self.tried_letters = []  # list - letters that were already tried
        self.hang_word = ''  # word of the hangman
        self.hang_state = ''  # current state of the hangman (guessed letters with _ as unguessed)
        self.hang_letters = []  # list - letters from the hangman word
        self.current_round = 0  # current round
        self.current_mistakes = 0  # mistake counter
        self.letter_to_guess = ''  # next tried letter
        self.game_is_active = True
        self.is_first_round = True
        self.hang_word = self.get_random_word()
        self.start_game()

    def start_game(self):
        # Starts all the necesary function to make the game moving

        while self.game_is_active:
            self.update_hang_state()
            self.hang_letters = self.letter_scan(self.hang_word)
            if '_' not in self.hang_state:
                self.game_is_active = False
                print(f"""
                      
correct word was: {self.hang_word}
                
                        Y O U   W I N !
                
                """)
            elif self.current_mistakes < 10:
                self.round(self.current_round)
            else:
                self.game_is_active = False
                print(f"""
                
                        G A M E   O V E R

                        corect word: {self.hang_word}
                
                """)

    def round(self):
        # Takes care of all the proceses needed for each round
        
        if self.current_round == 0:
            if self.is_first_round == True:
                self.is_first_round = False
                print(f'''
                    Welcome to the GAME!''')
            print(f'''{hangman_img.HANGMAN[self.current_mistakes]}
                  mistakes: {self.current_mistakes}/10''')
            print(f'{self.hang_state}')
            letter_memory = self.letter_check()
            self.update_hang_state(letter_memory)
        elif self.current_round < 10:
            pass

    def letter_check(self):
        # gets players letter to guess, checks if correctly

        letter_memory = ''
        print(letter_memory)

        while letter_memory == '':
            letter_memory = input('Enter your letter: ')
            letter_memory = letter_memory.lower()
            if letter_memory in self.tried_letters:
                print('E: You already tried this letter! Try a new one')
                letter_memory = ''
            elif len(letter_memory) > 1:
                print('E: You entered too many letters! Try again')
                letter_memory = ''
        self.tried_letters += letter_memory
        return letter_memory
        
    def update_hang_state(self, letter='.'):
        hang_state_memory = ''
        if letter in self.hang_letters or letter=='.':
            for i in self.hang_word:
                if i not in self.tried_letters:
                    hang_state_memory += '_'
                else:
                    hang_state_memory += i
        else:
            print(f'Letter "{letter}" doesnt appear in this word, try again!')
            self.current_mistakes += 1
        self.hang_state = hang_state_memory

    def letter_scan(self, word):
        # Creates list of words that are located in each word for hangman

        local_memory = []
        for i in word:
            if i not in local_memory:
                local_memory.append(i)
        return local_memory
    
    def get_random_word(self, dict=word_dict.common_words):
        return random.choice(dict)

game = hangman()