import itertools

def generate_combinations_with_permutations(sequence1, sequence2, sequence3):
    sequences = [sequence1, sequence2, sequence3]
    for permuted_sequences in itertools.permutations(sequences):
        for combo in itertools.product(*permuted_sequences):
            yield ''.join(combo)          
sequence1 = "AB"
sequence2 = "12"
sequence3 = "xy"
for combo in generate_combinations_with_permutations(sequence1, sequence2, sequence3):
    print(combo)
