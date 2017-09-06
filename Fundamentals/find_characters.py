#create program that creates a new list when searching for a string with a particular character

word_list = ['hello','world','my','name','is','Anna']
char = 'o' #take words from word_list that contain the letter 'o' and create a new list

#function
def find_char(a,b):
    new_list = []
    for i in range(0,len(a)):
        if b in a[i]: #if letter is contained within the list at particular index
            new_list.append(a[i]) #add to new list
    print new_list

find_char(word_list,char)

word_list2 = ['hello','world','my','name','is','Anna','python','is','fun'] #another check

find_char(word_list2,char)