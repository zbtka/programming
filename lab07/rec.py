def to_str_recursive(lst):
    if isinstance(lst, list):
        if len(lst) == 0:
            return "None"
        else:
            return str(lst[0]) + " -> " + to_str_recursive(lst[1:])
    else:
        return str(lst) + " -> None"

nested_list = [1, [2, [3, [4, [5]]]]]
string_recursive = to_str_recursive(nested_list)
print(string_recursive)
