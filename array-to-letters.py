import string
import random

array = []
new_array = []
done = False
counter = 0

def convert_array(array):
    for x in array:
        print(len(str(x)))

    for x in array:
        s = ""
        for _ in range(x):
            s += (random.choice(string.ascii_letters))
        new_array.append(s)
    return new_array

while (not done):
    number = input(("Enter Element " + str(counter) + ": "))
    try:
        array.append(int(number))
    except ValueError:
        done = True
        print(convert_array(array))
    counter += 1