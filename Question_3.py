# Question 1

def my_list():
    maxvalue = list1[0]
    for x in list1:
        if x > maxvalue:
            maxvalue = x
    return maxvalue


list1 = [2, 6, 3, 10, 99, 20, 4]
print("The maximum value in the list is:", my_list())

#  Question 2
string = "My favourite song is Lose Yourself by Eminem"
print(string.lower())


# Question 3
AnotherList = [89, 2, 76, 30, 200, 86, 5, 10]
AnotherList.sort()
print("Sorted list:", AnotherList)
