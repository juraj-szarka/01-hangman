import random
import word_dict


def get_random_word(dict):
    return random.choice(dict)

print(get_random_word(common_words))