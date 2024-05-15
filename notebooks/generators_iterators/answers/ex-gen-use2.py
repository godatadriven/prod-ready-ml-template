def get_alphabet_letter(alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for ind, letter in enumerate(alphabet):
        yield (letter, ind+1)

[x.lower() if x in 'AEIOU' else x for x in get_alphabet_letter()]