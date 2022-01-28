#!/usr/bin/python3

# Question1 - This is an algorithm to find the maximum value in a list
# defining the function
def my_list():
    maxvalue = list1[0]
    for x in list1:
        if x > maxvalue:
            maxvalue = x
    return maxvalue


list1 = [2, 6, 3, 10, 99, 20, 4]
print("The maximum value in the list is:", my_list())

#  Question 2 - This is an algorithm that converts all letters in a string to lowercase.
string = "My favourite song is Lose Yourself by Eminem"
print(string.lower())


# Question 3 - This is an algorithm that sorts a list of integers using the sort() inbuilt python function
AnotherList = [89, 2, 76, 30, 200, 86, 5, 10]
AnotherList.sort()
print("Sorted list:", AnotherList)
