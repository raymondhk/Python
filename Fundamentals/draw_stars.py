#Part 1 create a function that takes a list of numbers and prints out *

def draw_stars(arr):
    for i in range(len(arr)):
        stars = ''
        for j in range(0,arr[i]):
            stars += '*'
        print stars

draw_stars([4,6,1,3,5,7,25])

#Part 2 modify the function, allow a list containing integers and strings
#When a string is passed instead of * use the first letter instead

def draw_stars2(arr):
    for i in range(len(arr)):
        draw = ''
        if type(arr[i]) is int:
            for j in range(0,arr[i]):
                draw += '*'
            print draw
        if type(arr[i]) is str:
            string = arr[i].lower() #places the lower case string of the array in the variable
            for k in range(0,len(arr[i])):
                draw += '%s' %string[0] 
            print draw

draw_stars2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
