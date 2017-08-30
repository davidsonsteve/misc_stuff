
# The Farm Object 01
class FarmObject(object):
        number = 1
        def __init__(self, category=""):
            self.category = category
            self.farmID = FarmObject.number
            #FarmObject.number += 1
        def get_category(self):
            return self.category
        def get_farmid(self):
            return self.farmID
        def set_category(self, newcategory = ""):
                self.category = newcategory

        def __str__(self):
                data = vars(self)
                return '\n'.join("%s: %s" % item for item in data.items())


## Structure Objects 0101
class Structure(FarmObject):
        def __init__(self):
            FarmObject.__init__(self, category = "Structure")


## Plant Objects 0103
class Plant(FarmObject):
        def __init__(self):
            FarmObject.__init__(self, category = "Plant")


## Animal Objects 0102
class Animal(FarmObject):
        number = 1
        def __init__(self, name="", species="Unknown"):
                FarmObject.__init__(self, category = "Animal")
                self.animalID = Animal.number
                self.name = name
                self.species = species
                Animal.number += 1
        def get_animalid(self):
            return self.animalID
        def get_name(self):
                return self.name
        def set_name(self, newname=""):
                self.name = newname
        def get_species(self):
                return self.species
        def set_species(self, newspecies=""):
                self.species = newspecies

### Animal > Dog 010201
class Dog(Animal):
        number = 1
        def __init__(self,name="",subspecies="Unknown"):
                Animal.__init__(self,name,species="Dog")
                self.dogID = Dog.number
                self.subspecies = subspecies
                Dog.number += 1
        def get_subspecies(self):
                return self.subspecies
        def set_subspecies(self,newsubspecies=""):
                self.subspecies = newsubspecies
        def get_barcode(self):
            return str(self.dogID).zfill(6) + \
                   str(self.animalID).zfill(3) + \
                   str(self.farmID).zfill(3)

### Animal > Chicken 010202
class Chicken(Animal):
        number = 1
        def __init__(self,name="",subspecies="Unknown"):
                Animal.__init__(self,name,species="Chicken")
                self.subspecies = subspecies
                self.chickenID = Chicken.number
                Chicken.number += 1
        def get_subspecies(self):
                return self.subspecies
        def set_subspecies(self,newsubspecies=""):
                self.subspecies = newsubspecies
        def get_chickID(self):
                return  str(self.chickenID)


#### Animal > Chicken > Hen 01020201xx
class Hen(Chicken):
    number = 1
    def __init__(self,name="",eggcolor=""):
        Chicken.__init__(self,name)
        self.eggcolor = eggcolor
        self.henID = Hen.number
        Hen.number += 1
    def get_barcode(self):
        return str(self.farmID).zfill(2) +\
        str(self.animalID).zfill(3) +\
        str(self.chickenID).zfill(2) +\
        str(self.henID).zfill(2)
        


a = Hen()
b = Chicken()
c = Dog()
d = Structure()
e = Animal()
f = Plant()
g = Hen()






print str(g)
print g.get_barcode()

# f = Chicken("Boo")
# print(f)
# g = Chicken("Drumstick","Wyandotte")
# print(g)
# j = Hen("Henrietta","brown")
# print (j)
# j.set_name("PoopyFeet")


# return string statements - a better way?
# overall organization - what becomes a subclass
# categories, such as "print all animals"
# nice way of returning type, and add it to print statement?
# add all of these to some sort of dict or something?
