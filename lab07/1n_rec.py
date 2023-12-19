def to_str(lst):
    if lst is None:
        return "None"
    if isinstance(lst, list):
        if len(lst) == 0:
            return "None"
        return " -> ".join(map(to_str, lst)) + " -> None"
    return str(lst)
result = to_str([1, [2, [3, [4, [5]]]]])
print(result)
