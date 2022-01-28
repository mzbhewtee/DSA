import timeit

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

        test_for_1million_size = (1000000 * time_elapsed) / list_length
        estimated_time = "{:.3f}".format(test_for_1million_size)
    print("The estimated time will be: ", estimated_time,
              "seconds to run the algorithm\n\n")

list1 = [5,8,45,89,65,35,22,45]
my_list(list1)
