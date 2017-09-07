# create an animal class with attributes and methods below:
# attribute: name, health
# method: walk, run, display health:

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self, steps):
        self.steps = steps
        self.health -= self.steps
        print "The %s walked %s step(s) and health is now %s" %(self.name, self.steps, self.health) #check to make sure steps are equating
        return self
    
    def run(self, steps):
        self.steps = steps
        self.health -= self.steps*5
        print "The %s ran %s step(s) and health is now %s" %(self.name, self.steps, self.health)
        return self
    
    def displayHealth(self):
        return "Animal Name: %s\nAnimal Health: %s" %(self.name, self.health)

        

lion = Animal("Lion", 20)
print lion.walk(3).run(2).displayHealth()

# create a dog class
# default health of 150
# pet: increases health by 5

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog,self).__init__(name, health=150)
    def pet(self, times):
        self.times = times
        self.health += self.times*5
        print "The %s was pet %s time(s) and health is now %s" %(self.name, self.times, self.health)        
        return self

doggy = Dog("Dog", 0) #see Dragon notes
print doggy.walk(3).run(2).pet(1).displayHealth()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon,self).__init__(name, health=170) #can set standard health
    def fly(self, distance):
        self.distance = distance
        self.health -= self.distance*10
        print "The %s flew %s miles and health is now %s" %(self.name, self.distance, self.health)
        return self
    def DragonHealth(self):
        print "I am a Dragon"
        return super(Dragon,self).displayHealth() #needed to add return in order to display previous parent method
        
    
    
draconis = Dragon("Draconis", 0) #even if user sets a health it stats set at 170
print draconis.DragonHealth()

mouse = Animal("Mickey", 50)
# mouse.fly(5) #does not work
# mouse.pet(2) #does not work
# doggy.fly(5) #does not work