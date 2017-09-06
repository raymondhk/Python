#write a function that takes in a dictionary and returns a list of tuples
#first tuple item is the key and the second is the value

#input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def tuple(a):
    name = a.keys()
    number = a.values()
    tup = zip(name, number)
    print tup

tuple(my_dict)