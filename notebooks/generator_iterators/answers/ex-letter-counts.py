from collections import Counter

Counter(1 if perm[0] == 'a' or perm[1] == 'a' else 0 for perm in permutations('abcdef', 3))
