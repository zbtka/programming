import itertools
alp = "АНДРЕЙ" 
ar = itertools.product(alp, repeat=6) 
arl = []
for i in ar:
    arl.append(''.join(i)) 
count = 0  
for e in arl:
    if e[0] == 'Й':
        continue
    if e[-1] == 'Й':
        continue
    if e.count('Й') > 1:
        continue
    if e.startswith('Й'):
        continue
    if e.endswith('Й'):
        continue
    flag = True  
    for i in range(len(e)-1):
        if (e[i] == 'Й' and e[i + 1] == 'Е') or (e[i + 1] == 'Й' and e[i] == 'Е'):
            flag = False
            break
    if flag == True:
        count += 1  
print(count)
