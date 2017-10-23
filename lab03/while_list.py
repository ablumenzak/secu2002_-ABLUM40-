# creating a while loop that goes through numeric list mylist and prints x=1
mylist = [4,1,1,-1,5,2,6,9,5]
# cnt = 0 defines that the while loop will start from the value in the first position of the list
cnt = 0
# while it is true that the value of cnt is less than the length of the list:
while cnt < len(mylist):
    # x is the variable in the list. +1 adds 1 to the value of x in the defined cnt position
    x = mylist[cnt] + 1
    # this line of code moves the cnt position onto the next value
    cnt += 1
    print x


