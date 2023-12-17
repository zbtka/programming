def calculate_sequence(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    
    a_i_minus_2 = 1
    a_i_minus_1 = 1
    a_i = 0

    for i in range(2, n + 1):
        a_i = a_i_minus_2 + a_i_minus_1 / (a_i_minus_1 ** (a_i_minus_1 - 1))
        a_i_minus_2 = a_i_minus_1
        a_i_minus_1 = a_i
    
    return a_i

result = calculate_sequence(10)
print(result)
