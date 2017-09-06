#write a program that tests the type of list
#have a running sum for integers and print result
#concatenate string items and print 

l = ['magical unicorns',19,'hello',98.98,'world']
m = [2,3,1,7,4,12]
n = ['magical','unicorns']

def type_list(a):
    sum1 = 0
    str1 = ""
    for i in range(0, len(a)):
        if type(a[i]) == int or type(a[i]) == float:
            sum1 += a[i]
        elif type(a[i]) == str:
            str1 += a[i] + " "
              
    if all(isinstance(item, int) for item in a) == True or all(isinstance(item, float) for item in a) == True:
        print "The list you entered is of integer type"
        print "Sum:", sum1
    elif all(isinstance(item, str) for item in a) == True:
        print "The list you entered is of string type"
        print "String:", str1
    else:
        print "The list you entered is of mixed type"
        print "Sum:", sum1
        print "String:", str1
#output
type_list(l)
type_list(m)
type_list(n)
