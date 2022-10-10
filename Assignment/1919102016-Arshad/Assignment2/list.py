list = [1, 12, 44, 7, 9]

# Insert integer  at position
print("Before insert the integer", list)

list.insert(2, 2)

print("Insert integer  at position", list)

print('Delete the first occurrence of integer')
list.remove(1)
print(list)

print("Insert integer  at the end of the list")
list.append(11)
print(list)

print("Sort the list")
list.sort()
print(list)

print("Pop the last element from the list")
list.pop(3)
print(list)

print('Reverse the list')
list.reverse()
print(list)
