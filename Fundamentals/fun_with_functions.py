#create a function that distinguishes between odd and even numbers (1-2000)
def odd_even(a,b): #a = 1, b = 2
    for i in range(a, b+1):
        if i % 2 != 0:
            print "Number is %s. This is an odd number." %i
        else:
            print "Number is %s. This is an even number." %i

odd_even(1,2000)

#create a function called 'multiply' that iterates through each value in a list
#and returns a list where each value has been multiplied by 5
def multiply(arr,val):
    for i in range(len(arr)):
        arr[i] *= val
    return arr

print multiply([2,4,10,16],5)

#new function should take multiply function as argument
#take multiplied list as a two-dimensional list, each internal list contain the 1's times the number in org list
def layered_multiples(arr):
    for i in range(len(arr)):
        newarr = [] #resets the newarr
        for j in range(0,arr[i]):
            newarr.append(1) #adds 1 for each iteration
        arr[i] = newarr
    return arr

print multiply([2,4,5],3)
print layered_multiples(multiply([2,4,5],3))