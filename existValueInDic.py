def key_exists(dictionary, key):
    return key in dictionary

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

user_key = input("Enter a key to check: ")

if key_exists(my_dict, user_key):
    print(f"The key '{user_key}' exists in the dictionary.")
else:
    print(f"The key '{user_key}' does not exist in the dictionary.")