"""Write a function called return_a_list_copy that takes a list as an argument. The function should simply return the copied list."""

some_list = [1,2,3,4,5]

def return_a_list_copy(some_list):
  return some_list[:]

print(return_a_list_copy(some_list))