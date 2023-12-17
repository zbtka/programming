def to_str(input_list):
    result = " "
    for item in input_list:
        if isinstance(item, list):
            result += to_str(item) + ' -> '
        else:
            result += str(item) + ' -> '
    result += 'None'
    return result

nested_list = [1, [2, [3, [4, [5]]]]]
result_str = to_str(nested_list)
print(result_str)
