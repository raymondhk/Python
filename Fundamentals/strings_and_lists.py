#replace the first instance of the word day with mouth in the string
words = "It's thanksgiving day. It's my birthday too!"
print words.find("day")
print words.replace("day", "mouth", 1)

#find the max and min of the list
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

#print the first and last values on a list
a = ['hello',2,54,-2,7,12,98,'world']
b = [a[0],a[len(a)-1]]
print b

#sort list, split list in half, then push first half list into index 0 of the second half
list1 = [19,2,54,-2,7,12,98,32,10,-3,6]
list1.sort()
list2 = list1[:len(list1)/2]
list3 = list1[len(list1)/2:]
list3.insert(0, list2)
print list3