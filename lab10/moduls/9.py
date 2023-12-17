import itertools

def unique_combinations_generator(*iterables):
    for combination in itertools.product(*iterables):
        yield combination

sequence1 = [1, 2, 3]
sequence2 = ['a', 'b', 'c']
sequence3 = ['x', 'y']

combinations = unique_combinations_generator(sequence1, sequence2, sequence3)
for combo in combinations:
    print(combo)
