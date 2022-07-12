# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pywsd.lesk import simple_lesk, adapted_lesk, cosine_lesk

from pywsd import disambiguate
from pywsd.similarity import max_similarity as maxsim

from pywsd.lesk import cached_signatures

from nltk.corpus import wordnet as wn
from wn.synset import Synset


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
    sent = 'I deposited my money in the piggy bank'
    sent = 'I biked across the river bank early Saturday morning'
    ambiguous = 'bank'
    answer = adapted_lesk(sent, ambiguous, pos='n')
    print(answer.definition())

    # print(disambiguate('I went to the bank to deposit my money'))
    # print(disambiguate('I went to the bank to deposit my money', algorithm=maxsim, similarity_option='wup', keepLemmas=True))

    print(cached_signatures['dog.n.01']['simple'])
    print(cached_signatures['dog.n.01']['adapted'])


    print('=============================================================\n')
    print('I went to the bank to deposit my money\n')
    print('=============================================================\n')

    res = disambiguate('I went fishing to the river bank and I cought nothing',
                       algorithm=maxsim, similarity_option='wup', keepLemmas=True)
    res = disambiguate('I went fishing to the river bank and I cought nothing', algorithm=maxsim, keepLemmas=True)
    synsets = list(filter(lambda a: isinstance(a[2], Synset), res));
    list(map(lambda tuple: print(f'{tuple[0]}-{tuple[1]}-{tuple[2].definition()}\n'), synsets))

    print('=============================================================\n')

    res = disambiguate('I went to the bank to deposit my money', algorithm=maxsim, similarity_option='wup',
                       keepLemmas=True)
    # print (res)
    synsets = list(filter(lambda a: isinstance(a[2], Synset), res));
    list(map(lambda tuple: print(f'{tuple[0]}-{tuple[1]}-{tuple[2].definition()}\n'), synsets))

