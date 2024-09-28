# my_list = [1,2,3,4,5]
# my_list.append(6)
# my_list.remove(2)
# min_Num = min(my_list)
# max_Num = max(my_list)
# print(max_Num,  min_Num)


# write a program to given a list of fruits: ['apple', 'banana', 'cherry', 'orange'
# 'kiwi','mango'] and Access the first, middle, and last element of the list.
# Change the second element to 'blueberry'

# fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# first_element = fruits[0]
# print("First element:", first_element)
# middle_index = len(fruits) // 2
# middle_element = fruits[middle_index]
# print("Middle element:", middle_element)
# last_element = fruits[-1]
# print("Last element:", last_element)
# fruits[1] = 'blueberry'
# print("Updated list:", fruits)


# Write a program that takes a list of student names as input,
# sorts the names in alphabetical order, and prints the sorted list.

# def sort_student_names(names):
#      sorted_names = sorted(names)
#      return sorted_names
# student_names = input("Enter a list of student names separated by spaces: ").split()
# sorted_names = sort_student_names(student_names)
# print("Sorted list of student names:", sorted_names)

# Write a program that takes a list of integers and prints:
# The first 3 elements,The last 2 elements,The entire list in reverse order
# def print_list_elements(my_list):
#     print("The first 3 elements:", my_list[:3])
#     print("The last 2 elements:", my_list[-2:])
#     print("The entire list in reverse order:", my_list[::-1])
# my_list = [1, 2, 3, 4, 5, 6]
# print_list_elements(my_list)   


# Write a Python program that removes all duplicates from 
# a given list and prints the new list without duplicates.

# def remove_duplicates(input_list):
#     return list(dict.fromkeys(input_list))
# my_list = [1, 2, 2, 3, 4, 4, 5]
# new_list = remove_duplicates(my_list)
# print("Original list:", my_list)
# print("List without duplicates:", new_list)  



# Create a dictionary where the keys are the names of 5 different countries 
# and the values are their capitals. Write a program to display all 
# the countries and their capitals.

# countries_and_capitals = {
#     "United States": "Washington D.C.",
#     "Canada": "Ottawa",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Brazil": "Brasilia"
# }

# for country, capital in countries_and_capitals.items():
#     print(f"The capital of {country} is {capital}.")




# - Write a program to update the 'grade' value to 'A', and add a new key-value pair 
# for 'major' with the value 'Computer Science'.
# student = {'name': 'John', 'age': 22, 'grade': 'B'}

# student = {'name': 'John', 'age': 22, 'grade': 'B'}
# student['grade'] = 'A'
# student['major'] = 'Computer Science'
# print(student)

# Write a program that creates a dictionary where the keys are subjects
# (e.g., 'Math', 'Science') and the values are lists of marks.
# Add marks for 3 subjects, and print the average marks for each subject.


# def calculate_average_marks(subject_marks):
#   average_marks = {}
#   for subject, marks in subject_marks.items():
#     average_marks[subject] = sum(marks) / len(marks)
#   return average_marks
# subject_marks = {
#     'Math': [85, 90, 78],
#     'Science': [92, 88, 95],
#     'English': [75, 80, 82]
# }
# average_marks = calculate_average_marks(subject_marks)
# for subject, average in average_marks.items():
#   print(f"The average marks for {subject} is {average}")















