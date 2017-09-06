#create program that compares two lists to determine if they're identical
#test cases
l1 = [1,2,5,6,2]
l2 = [1,2,5,6,2]

l3 = [1,2,5,6,5]
l4 = [1,2,5,6,5,3]

l5 = [1,2,5,6,5,16]
l6 = [1,2,5,6,5]

l7 = ['celery','carrots','bread','milk']
l8 = ['celery','carrots','bread','cream']

#function
def compare_list(a,b):
    if a == b: #compares the two lists
        print "The lists are the same"
    else:
        print "The lists are not the same"

#output
compare_list(l1,l2)
compare_list(l3,l4)
compare_list(l5,l6)
compare_list(l7,l8)
compare_list(l7,l5) #test between different types within the list