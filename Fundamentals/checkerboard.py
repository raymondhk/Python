#create a program that prints a 'checkerboard'

def checkerboard(a,b): #a = row, b = column
    row = ""
    for j in range(0,b,2):
            row += "* "
    for i in range(0,a):
        if i % 2 is 0:
            print row
        else:
            print " " + row

checkerboard(10,10)
checkerboard(20,20)