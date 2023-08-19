

# Simple

def has_numeric_value(lst):
    for item in lst:
        if isinstance(item, (int, float)):
            return True
    return False

# Example list
my_list = [1, 'apple', 3.14, 'banana', True, 42]

if has_numeric_value(my_list):
    print("The list contains at least one numeric value.")
else:
    print("The list does not contain any numeric values.")
    
    