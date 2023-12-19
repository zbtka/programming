import itertools

def limited_combinations_generator(*iterables, r):
    for combination in itertools.product(*iterables):
        for limited_combo in itertools.combinations(combination, r):
            yield limited_combo
sequence1 = [1, 2, 3]
sequence2 = ['a', 'b', 'c']
sequence3 = ['x', 'y']
r = 3  
if r > 3:
    print("Максимальное количество последовательностей ограничено")
combinations = limited_combinations_generator(sequence1, sequence2, sequence3, r=r)
for combo in combinations:
    print(combo)

