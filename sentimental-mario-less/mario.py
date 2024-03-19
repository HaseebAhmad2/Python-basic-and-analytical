
import cs50
# getting height from user
height = cs50.get_int("Enter height: ")
# height range is defined. if height is not in defined range then we have to enter correct height
while (height <= 0 or height > 8):
    height = cs50.get_int("Enter correct height: ")
# loop for controlling nested loops
for i in range(height):
    # loop for printing spaces
    for j in range(height-1-i, 0, -1):
        print(" ", end=(''))
    # loop for printing #
    for k in range(i+1):
        print("#", end=(''))
    print("")
