#aufulpoetry1_ans.py

import random

articles = ['a', 'another', 'the']
nouns = ['dog', 'cat', 'fish', 'man', 'girl']
verbs = ['jumped', 'sang', 'played', 'stoned', 'ran']
adverbs = ['loudly', 'badly', 'hardly', 'strongly', 'sadly']

for _ in range(5):
    variation = random.randint(0, 1)
    article = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    if variation:
        adverb = random.choice(adverbs)
        print(' '.join([article, noun, verb, adverb]))
    else:
        print(' '.join([article, noun, verb]))
