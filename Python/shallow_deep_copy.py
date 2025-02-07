import copy

print("_______________________SHALLOW COPY_________________________")
# Shallow Copy (If the original object contains any references to mutable objects, the copy will also reference the same object.)

original = {"name": "Alice", "hobbies": ["reading", "cycling"]}

shallow_copy = copy.copy(original)

shallow_copy["hobbies"][0] = "swimming"

print("Original List : ", original)  # Output: Original List :  {'name': 'Alice', 'hobbies': ['swimming', 'cycling']}
print("Shallow Copy : ", shallow_copy)  # Output: Shallow Copy :  {'name': 'Alice', 'hobbies': ['swimming', 'cycling']}

# Deep Copy  "(original object and copied object are completely independent of each other)"
print("_______________________DEEP COPY_________________________")

original_deep = {"name": "Alice", "hobbies": ["reading", "cycling"]}

deep_copy = copy.deepcopy(original_deep)

deep_copy["hobbies"][0] = "swimming"

print("Original List : ", original_deep)  # Output: Original List :  {'name': 'Alice', 'hobbies': ['reading', 'cycling']}
print("Deep Copy : ", deep_copy)  # Output: Deep Copy :  {'name': 'Alice', 'hobbies': ['swimming', 'cycling']}
