# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pywsd.lesk import simple_lesk

from pywsd import disambiguate
from pywsd.similarity import max_similarity as maxsim, max_similarity

from pywsd.lesk import cached_signatures
from pywsd.lesk import simple_lesk, adapted_lesk, cosine_lesk

from nltk.corpus import wordnet as wn
from wn.synset import Synset
from pywsd.baseline import random_sense, first_sense, max_lemma_count

from nltk.wsd import lesk

def print_tuple(tuple):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{tuple[0]}')
    print(f' ')
    print(f'{tuple[1]}')
    print(f' ')
    print(f'{tuple[2].definition()}\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(print("Wordnet {}".format(wn.get_version())))

    print(" NLTK WSD Test ==================")

    print(lesk('I went to the bank to deposit my money', 'bank').definition())
    print(lesk('my cat likes to eat mice', 'cat').definition())
    print("==TERRIBLE!!! ^^^^^ =============")

    print(" Adapted lesk Test ==================")

    print(adapted_lesk('I went to the bank to deposit my money', 'bank').definition())
    print(adapted_lesk('my cat likes to eat mice', 'cat').definition())
    print("=================================")


    print(" Cosigne lesk Test ==================")

    print(cosine_lesk('I went to the bank to deposit my money', 'bank').definition())
    print(cosine_lesk('my cat likes to eat mice', 'cat').definition())
    print("=================================")


    print("max_similarity('my cat likes to eat mice', 'cat', 'wup', pos='n').definition()")
    print(max_similarity('my cat likes to eat mice', 'cat', 'wup', pos='n').definition())
    print("max_similarity('my cat likes to eat mice', 'cat', 'lin', pos='n').definition()")
    print(max_similarity('my cat likes to eat mice', 'cat', 'lin', pos='n').definition())


    bank_sents = ['I went to the bank to deposit my money',
                  'The river bank was full of dead fishes']

    plant_sents = ['The workers at the industrial plant were overworked',
                   'The plant was no longer bearing flowers']

    print("#TESTING simple_lesk() ...")
    print("Context:", bank_sents[1])
    answer = simple_lesk(bank_sents[1], 'bank')
    print("Sense:", answer)
    print("Definition:", answer.definition())

    answer = simple_lesk(bank_sents[1], 'bank')
    print("Sense:", answer)
    print("Definition:", answer.definition())

    print("#TESTING random_sense() ...")
    answer = random_sense('bank')
    print("Sense:", answer)
    print("Definition:", answer.definition())
    print()

    print("#TESTING first_sense() ...")
    answer = first_sense('bank')
    print("Sense:", answer)
    print("Definition:", answer.definition())
    print()

    print("#TESTING most_frequent_sense() ...")
    answer = max_lemma_count('bank')
    print("Sense:", answer)
    print("Definition:", answer.definition())
