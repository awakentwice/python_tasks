#aufulpoetry2_ans.py

import random

articles = ['a', 'another', 'the', 'other', 'recent']
nouns = ['dog', 'cat', 'fish', 'man', 'girl']
verbs = ['jumped', 'sang', 'played', 'stoned', 'ran']
adverbs = ['loudly', 'badly', 'hardly', 'strongly', 'sadly']

line_numbers = 5
input_line_numbers = input('Enter line numbers or Enter: ')

try:
    lines = int(input_line_numbers)
    if 1 <= lines <= 10:
        line_numbers = lines
        
except ValueError as err:
    print('Error: You should enter a number.')

for _ in range(line_numbers):
    variation = random.randint(0, 1)
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    if variation:
        adverb = random.choice(adverbs)
        print(' '.join([article, noun, verb, adverb]))
    else:
        print(' '.join([article, noun, verb]))
