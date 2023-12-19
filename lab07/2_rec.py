def calculate_a(i, a):
    if i < 2:
        return 1
    else:
        return calculate_a(i-2, a) + (calculate_a(i-1, a) / (a ** (a-1)))

i_value = 5
a_value = 2
result = calculate_a(i_value, a_value)
print(f"i={i_value} и a={a_value} = {result}")
