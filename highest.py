a_dictionary = {"a": 1, "b": 2, "c": 3}

# get key w
max_key = max(a_dictionary, key=a_dictionary.get)

print(max_key)