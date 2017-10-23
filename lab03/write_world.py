# Creates the file 'hello_world.txt' in the current directory (lab03). 'w' overwrites the contents of the file.
f = open('hello_world.txt', 'w')
# This code allows us to fill the file with contents, in this case the content is "Hello, world!"
f.write('Hello, world!')
# Closes the file when you are done writing and adding contents.
f.close()