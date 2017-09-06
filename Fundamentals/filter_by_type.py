#test -- if integer is greater or equal to 100 print "That's a big number"...less than 100 print "That's a small number"
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
#test -- if the string is greater than or equal to 50 characters print "Long sentence."
#if string is less than 50 characters print "Short sentence."
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
#test -- if the length of list is greater than or equal to 10 print "Big list!"
#if list is less than 10 values print "Short list."
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#function
def filter(a):
    if isinstance(a, int) and a >= 100:
        print "That's a big number!"
    elif isinstance(a, int) and a < 100:
        print "That's a small number"
    elif isinstance(a, str) and len(a) >= 50:
        print "Long sentence."
    elif isinstance(a, str) and len(a) < 50:
        print "Short sentence."
    elif isinstance(a, list) and len(a) >= 10:
        print "Big list."
    elif isinstance(a, list) and len(a) < 10:
        print "Short list."

#results
filter(sI)
filter(mI)
filter(bI)
filter(eI)
filter(spI)
filter(sS)
filter(mS)
filter(bS)
filter(eS)
filter(aL)
filter(mL)
filter(lL)
filter(eL)
filter(spL)