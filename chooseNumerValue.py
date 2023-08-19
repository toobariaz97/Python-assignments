def has_numeric_value(lst):
    for item in lst:
        if isinstance(item, (int, float)):
            return True
    return False

user_list = input("Enter a list of values (separated by spaces): ").split()

for i in range(len(user_list)):
    try:
        user_list[i] = int(user_list[i])
    except ValueError:
        try:
            user_list[i] = float(user_list[i])
        except ValueError:
            pass

if has_numeric_value(user_list):
    print("The list contains at least one numeric value.")
else:
    print("The list does not contain any numeric values.")