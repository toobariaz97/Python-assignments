def find_duplicates(lst):
    duplicates = []
    seen = set()
    
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6
           ]

duplicate_values = find_duplicates(my_list)

if len(duplicate_values) > 0:
    print("Duplicate values in the list:", duplicate_values)
else:
    print("No duplicate values found in the list.")