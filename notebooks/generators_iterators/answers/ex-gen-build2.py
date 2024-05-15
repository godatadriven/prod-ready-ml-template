def get_alphabet_letter(alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for ind, letter in enumerate(alphabet):
        yield (letter, ind+1)
