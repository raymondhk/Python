#determine whether a number is prime or a perfect square
#print foo if prime
#print bar if perfect square

for i in range(100, 10001):
    str = ""
    sqr = ""
    for k in range(2, i/2 + 1):
        if k * k == i:
            sqr = "%s: Bar" %i
            print sqr
            break
    if "Bar" not in sqr:
        for j in range(2, i/2 + 1):
            mod = i % j
            str = str + " %s, " %mod
            if mod is 0:
                break
        if " 0," in str:
            print "%s: FooBar" %i
        else:
            print "%s: Foo" %i
