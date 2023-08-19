def count_numeric_values(lst):
    count = 0
    for item in lst:
        if isinstance(item, (int, float)):
            count += 1
    return count

user_list = []

while True:
    user_input = input("Enter a value (or 'exit' to finish): ")
    
    if user_input.lower() == 'exit':
        break
    
    try:
        num_value = int(user_input)
    except ValueError:
        try:
            num_value = float(user_input)
        except ValueError:
            num_value = user_input
        
    user_list.append(num_value)

numeric_count = count_numeric_values(user_list)

if numeric_count > 0:
    print(f"The list contains {numeric_count} numeric value(s).")
else:
    print("The list does not contain any numeric values.")

print("User list:", user_list)