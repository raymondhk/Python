me = {
    "name": "Ray",
    "age": "31",
    "country of birth": "The United States",
    "favorite language": "Python"
}

def dictionary(a):
    for key,data in a.iteritems():
        print "My", key, "is", data

dictionary(me)