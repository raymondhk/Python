#create a function that takes two lists and creates a single dictionary

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    for i in range(len(arr1)):
        new_dict[arr1[i]] = arr2[i].capitalize()
    return new_dict

print make_dict(name,favorite_animal)

#hacker challenge: if lists are of unequal length, the longer list should be used for the keys

name2 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Ray", "Bob", "Jess"]
favorite_animal2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict2(arr1, arr2):
    new_dict = {}
    if len(arr1) > len(arr2):
        for i in range(len(arr2)):
            new_dict[arr1[i]] = arr2[i].capitalize()
        for i in range(len(arr2), len(arr1)):
            new_dict[arr1[i]] = "None"
    else:
        for i in range(len(arr1)):
            new_dict[arr2[i]] = arr1[i].capitalize()
        for i in range(len(arr1), len(arr2)):
            new_dict[arr2[i]] = "None"
    return new_dict

print make_dict2(favorite_animal2, name2)