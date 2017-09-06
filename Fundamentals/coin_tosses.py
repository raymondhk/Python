#write a function that simulates tossing a coin 5000 times

def coin_toss(a): #a is the amount of times user would like to cycle through the program
    import random
    print "Starting the program..."
    heads = 0 #created empty variables for my count
    tails = 0
    for i in range(1,a+1):
        rand = random.randint(0,1) #randomly generate heads or tails, 0 - heads and 1 - tails 
        if rand is 0:
            heads += 1
            print "Attempt #%s: Throwing a coin ... It's heads! ... Got %s head(s) so far and %s tail(s) so far" %(i,heads,tails)
        else:
            tails += 1
            print "Attempt #%s: Throwing a coin ... It's tails! ... Got %s head(s) so far and %s tail(s) so far" %(i,heads,tails)
    print "Ending the program, thank you!"

coin_toss(5000)