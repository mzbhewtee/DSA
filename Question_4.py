import timeit
import matplotlib.pyplot as plt
#imorted modules: timeit for time-related functions; matplotlib.pyplot for graphs plotting

# question 1
def my_list(list1):
    start = timeit.default_timer()
    maxvalue = list1[0]
    for x in list1:
        if x > maxvalue:
            maxvalue = x
    end = timeit.default_timer()
    time_elapsed = end - start

#Time Complexity 
    list_length = 1
    timeusedlist = []
    while list_length < 100:
        if list_length == 3:
            print(time_elapsed)
        else:
            time_for_list_containing_one = (list_length * time_elapsed) / 3
        list_length += 1
        timeusedlist.append(time_for_list_containing_one)
    x_axis = range(0, len(timeusedlist))
    y_axis = [time_for_list_containing_one for time_for_list_containing_one in timeusedlist]
    plt.plot(x_axis, y_axis)
    plt.xlabel('Length')
    plt.ylabel('Time')
    plt.title('Time-Complexity')
    plt.show()
    print ("Maxvalue: ",maxvalue,"\nTime Elapsed: ",time_elapsed, "\nTime for a List of one:", time_for_list_containing_one,
           "\nTotal time used list",timeusedlist)

# Space Complexity
    int_size = 4
    list_to_be_calculated = []

    size_of_space_used = 1
    while size_of_space_used < 100:
       space_used = (int_size*size_of_space_used)+4
       list_to_be_calculated.append(space_used)
       size_of_space_used += 1
    x_axis = range(0, len(list_to_be_calculated))
    y_axis = [s for s in list_to_be_calculated]
    plt.xlabel('Length of List')
    plt.ylabel('Space Complexity')
    plt.title('Space Complexity')
    plt.plot(x_axis, y_axis)
    plt.show()
    print("Size of space used in byte: ", list_to_be_calculated)




# Question 2
def lowercase(string):
    print("Coverting",string,"to lowercase...\n")
    start = timeit.default_timer()
    print(string.lower())
    print("Length of the initial string:", len(string))
    end = timeit.default_timer()
    time_elapsed = end-start
    print("Time taken to convert to lowercase:", end - start)

    # Time complexity
    char_length = 0
    timeusedlist = []
    while char_length < 100:
        if char_length == 44:
            print(time_elapsed)
        else:
            time_for_list_containing_one = (char_length * time_elapsed) / 44
        char_length += 1
        timeusedlist.append(time_for_list_containing_one)
    x_axis = range(0, len(timeusedlist))
    y_axis = [time_for_list_containing_one for time_for_list_containing_one in timeusedlist]
    plt.plot(x_axis, y_axis)
    plt.xlabel('Length')
    plt.ylabel('Time')
    plt.title('Time-Complexity')
    plt.show()
    print("Number of characters: ", char_length, "\nTime Elapsed: ", time_elapsed, "\nTime for a List of one:",
           time_for_list_containing_one,
           "\nTotal time used list", timeusedlist)

    # Space complexity

    char_size = 1
    list_to_be_calculated = []

    size_of_space_used = 0
    while size_of_space_used <= 100:
        space_used = (char_size * size_of_space_used) + 1
        list_to_be_calculated.append(space_used)
        size_of_space_used += 1
    x_axis = range(0, len(list_to_be_calculated))
    y_axis = [s for s in list_to_be_calculated]
    plt.xlabel('Length of List')
    plt.ylabel('Space Complexity')
    plt.title('Space Complexity')
    plt.plot(x_axis, y_axis)
    plt.show()
    print("Size of space used in byte: ", list_to_be_calculated)


# Question 3
def sort_list(my_list):
    start = timeit.default_timer()
    print("List: ",AnotherList)
    AnotherList.sort()
    print("Sorted list:", AnotherList)
    end = timeit.default_timer()
    Time = end-start
    print("Time taken to sort the list:", end - start)

#Time complexity
    list_length = 0
    timeusedlist = []
    while list_length < 100:
        if list_length == 8:
            print(Time)
        else:
            time_for_list_containing_one = (list_length * Time) / 8
        list_length += 1
        timeusedlist.append(time_for_list_containing_one)
    x_axis = range(0, len(timeusedlist))
    y_axis = [time_for_list_containing_one for time_for_list_containing_one in timeusedlist]
    plt.plot(x_axis, y_axis)
    plt.xlabel('Length')
    plt.ylabel('Time')
    plt.title('Time-Complexity')
    plt.show()
    print("Number of characters: ", list_length, "\nTime Elapsed: ", Time, "\nTime for a List of one:",
          time_for_list_containing_one,
          "\nTotal time used list", timeusedlist)


#Space complexity
    int_size = 4
    list_to_be_calculated = []

    size_of_space_used = 1
    while size_of_space_used < 100:
        space_used = (int_size * size_of_space_used) + 4
        list_to_be_calculated.append(space_used)
        size_of_space_used += 1
    x_axis = range(0, len(list_to_be_calculated))
    y_axis = [s for s in list_to_be_calculated]
    plt.xlabel('Length of List')
    plt.ylabel('Space Complexity')
    plt.title('Space Complexity')
    plt.plot(x_axis, y_axis)
    plt.show()
    print("Size of space used in byte: ", list_to_be_calculated)

def intro():
    print("For space maximization, all the prompt of question 4 will be done here\n")
    options = int(input("Enter 1 for time-complexity for max value in a list\n"
                   "Enter 2 for lowercase conversion\n"
                   "Enter 3 for list sorting\n"))
    if options == 1:
        list1 = [34, 50, 234]
        my_list(list1)

    elif options == 2:
        string = "My favouRite Song is LOSe Yourself by Eminem"
        lowercase(string)

    elif options == 3:
        AnotherList = [89, 2, 76, 30, 200, 86, 5, 10]
        sort_list(AnotherList)

    else:
        print("Input the correct option")
        intro()
intro()

