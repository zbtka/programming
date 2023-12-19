def calculate_a_iterative(i, a):
    if i < 2:
        return 1
    a_values = [1, 1] 
    for n in range(2, i+1):
        a_n = a_values[n-2] + (a_values[n-1] / (a ** (a-1)))
        a_values.append(a_n)
    return a_values[i]
i_value = 5
a_value = 2
result = calculate_a_iterative(i_value, a_value)
print(f"i={i_value} и a={a_value} = {result}")
