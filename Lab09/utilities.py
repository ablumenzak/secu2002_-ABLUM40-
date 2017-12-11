### TASK 1 ###

# This is the data set that will be called in the function
data = [2, 34, 5, 6, 8, 19]

# This is the fuction that will check a dataset to see if an element is present
# and how many times somehting must iterate through the list until it finds the element e
def lin_find(data,e):
    # count = 0 initially sets the position of count to 0
    count = 0
    # for loop that iterates through the list 'data' to check each element
    for i in data:
        # this adds '1' to the count each time the programme goes through the list
        count += 1
        # states that if e is an element in the list, return the value of e and the number of times it went through the
        # list to find the element
        if e == i:
            return e, count
    # if the element is not in the list a message appears and the count is also given
    return 'element not in list', count

#TESTING

e = 9
print lin_find(data,e)

e = 5
print lin_find(data,e)

data = [3,6,8,9,2,22,3,54,3,6,8,19]
e = 19
print lin_find(data,e)

### TASK 2 ###

# define dataset

# function to run a binary search
def bin_find(data,e):
    # defines inital count position as 0
    count = 0
    # initially defines the first element as 0
    first = 0
    # defines the last value as the length of the list - 1
    last = len(data)-1
    # while loop to say that while the below condition is true carry out the following checks
    while first <= last:
        # each time the while loop runs add one to the value of count
        count += 1
        # defines the value of pivot and allows the loop to be updated as it is in the while loop
        pivot = (first + last) / 2
        # when e is more than the pivot value in data update the value of 'first' to ignore all the values before
        if e > data[pivot]:
            first = pivot + 1
        # when e is less than the pivot value in data update the value of 'last' to ignore all the values after
        elif e < data[pivot]:
            last = pivot -1
        # If e is equal to the pivot return e and the number of times the loop goes through the list (count)
        else:
            return e, count
    # if the condition of the while loop is not met return the message in the string below and the number of times
    # the loop goes through the list
    print 'element is not in the list,', count
    return None

### TESTING ###

data2 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
e = 8
print bin_find(data2,e)

data3 = [1,2,3,4,5,6]
e = 3
print bin_find(data3,e)

data4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
e = 11
print bin_find(data4,e)

data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
e = 8
print bin_find(data2,e)

