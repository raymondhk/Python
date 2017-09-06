#create a program that generates random scores
#create a program that logs the scores and associates it with a grade
def random_score(a):
    import random
    lst = []
    for i in range(0,a):
        rand_num = random.randint(60,100)
        # print rand_num
        lst.append(rand_num)
    return lst
# print random_score(10)

def grades(arr):
    print "Scores and Grades"
    for i in range(len(arr)):
        if arr[i] >= 60 and arr[i] < 70:
            print "Score: %s; Your grade is a D" %arr[i]
        elif arr[i] >= 70 and arr[i] < 80:
            print "Score: %s; Your grade is a C" %arr[i]
        elif arr[i] >= 80 and arr[i] < 90:
            print "Score: %s; Your grade is a B" %arr[i]
        else:
            print "Score: %s; Your grade is an A" %arr[i]
    print "End of the program. Bye!"

grades(random_score(10))