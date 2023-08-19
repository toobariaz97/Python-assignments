my_dict = {
    "a": 10,
    "b": 20,
    "c": "not a number",
    "d": 15.5,
    "e": "another string",
    "f": 7
}

def sum_numeric_values(dictionary):
    total = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            total += value
    return total

total_sum = sum_numeric_values(my_dict)
print("Sum of numeric values in the dictionary:", total_sum)
