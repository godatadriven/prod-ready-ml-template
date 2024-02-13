# +
from collections import Counter

def word_count(string):
    words = chain.from_iterable(x.split() for x in test_string)
    for word, group in groupby(sorted(words)):
        yield word, len(list(group))

list(word_count(test_string))

def word_counter(string):
    words = chain.from_iterable(x.split() for x in test_string)
    yield from Counter(words).items()

list(word_counter(test_string))
