#i = 1
#print 'x ' + '%s ' % i
'''
def multi_table(a):
    top = 'x '
    first = '1 '
    for i in range(1, a+1):
        top += '%s ' % i
        first += '%s ' % i*1
    print top
    print first

multi_table(5)
'''

def mul_table(x, y):
    for line in xrange(1, y+1):
        for table in xrange(1, x+1):
            print line * table, "\t",
        print

mul_table(5,5)
'''
print ' x 1 2 3 4 5 6 7 8 9 10 11 12'
for row in range(1, 12 + 1): 
    display_string  = ''
    for column in range(0, 12 + 1):
        if column is 0:
            display_string += ' ' + str(row)
        else:    
            display_string += ' ' + str(column * row)
    print display_string 
'''