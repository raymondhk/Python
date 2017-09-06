#part 1: write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
def odd_num():
    for i in range(1, 1000, 2):
        print i

print odd_num()

#part 2: create another program that prints all the multiples of 5 from 5 to 1,000,000
def multi_five():
    for i in range(5, 1000001, 5):
        print i

print multi_five()

#sum list - create a program that prints the sum of all the values in the list
def sum_list(a):
    sum1 = a[0]
    for i in range(1, len(a)):
        sum1 += a[i]
    return sum1
print sum_list([1,2,5,10,225,3])

#or

b = [1,2,5,10,225,3]
print sum(b)

#avg list - create a program that prints the average of the values in the list
avg = sum(b)/len(b)
print avg