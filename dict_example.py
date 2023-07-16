employees = {
    '101' : {'name' : 'John', 'age' : 29, 'salary' : 25000},
    '102' : {'name' : 'Mary', 'age' : 35, 'salary' : 35000},
    '103' : {'name' : 'Bob', 'age' : 29, 'salary' : 45000},
}

# display the initial dictionary
print("Initial dictionary:")
print(employees)

# add a new entry
employees['104'] = {'name' : 'Sara', 'age' : 25, 'salary' : 55000}

# update
employees['101']['salary'] = 35000

# remove the last entered entry
employees.popitem()

# display the updated dictionary
print("\nUpdated dictionary:")
print(employees)

# display the keys and values separately
print("\nKeys:")

print(list(employees.keys()))

print("\nValues:")
print(list(employees.values()))

# clear the dictionary
employees.clear()

# display the empty dictionary
print("\nEmpty dictionary:")
print(employees)