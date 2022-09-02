# Creating a string
string = "JavaTpoint"
# initializing an iterator
iterator = 0

# starting a while loop
while iterator < len(string):
    # if loop is at letter  will skip the remaining code and go to next iteration
    if string[iterator] == 'a':
        continue
        # otherwise it will print the letter
    print(string[iterator])
    iterator += 1