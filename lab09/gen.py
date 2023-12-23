import itertools, more_itertools

s = [[1, 2,],['a','b'],['x','y']]
seq = [0,1,2,0]

#создаём перестановку индексов
for p in more_itertools.distinct_permutations(seq):

    #и на её основе перестановку последовательностей
    perm = [s[o] for o in p]

    #и теперь комбинацию
    for combination in itertools.product(*perm):
        print(list(combination))
