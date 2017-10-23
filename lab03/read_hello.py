# Opens 'hello_world.txt file'. 'r' means the files is a readable version
f = open('hello_world.txt', 'r')
# for loop to print first 4 characters ([:4] = characters at postion 0,1,2,3)
for lines in f:
    print lines [:4]