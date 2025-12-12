from itertools import islice


def get_alphabet_letter(alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for ind, letter in enumerate(alphabet):
        yield (letter, ind+1)

alphabet_gen = get_alphabet_letter()

# Get the 3rd letter (C)
print(next(islice(alphabet_gen, 2, 3)))

# You can also create an entire list in memory
# which is not memory efficient.
alphabet_list = list(get_alphabet_letter())
print(alphabet_list[2])