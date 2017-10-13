import random
import sys
import os

print("Hello World")

name = "Derek"
print(name)

# Comment

# Datatypes:  
# Numbers (),
# Quote (String "\" tällä tavalla saa heittomerkit kommenttiin"), multiline quote ''' tekstiä '''
# List
# 

# Arithmetics:
# % = modula


print("I don't like ", end = "")
print("new lines")
print("I like \n new lines")

myList = ['a', 'b',
            'c']
print('First Item', myList[0])
print(myList[1:3])

to_do_list = [myList, 1, 'a']
print(to_do_list)
print(to_do_list[0][1])

to_do_list.insert(1,'Uusi arvo')
print(to_do_list)

myList.insert(3,'d')
print(myList)
print(to_do_list)

combined_list = myList + to_do_list
myList.insert(4,'e')

print(combined_list)


# Tuples

pi_tuple = (3,1,4,1,5,9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print((new_list))



# Dictionaries / maps
# Unique keys with assosiated values

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark MArdon',
                  'Mirror Master' : 'Sam Schudder',
                  'Pied Piper' : 'Thomas Peterson'}

print(super_villains['Captain Cold'])
del super_villains['Fiddler']
# replace key value
super_villains['Pied Piper'] = 'Hartley RAthaway'


print(super_villains.keys())
print(super_villains.values())

# conditionals
# if else elif == != > >=
# logicals
# and or not

age = 19
if age > 21 :
    print('quite old')
elif (age < 21) and (age >=18)  :
    print('great age')
elif age > 16 :
    print('You are old anough to drive')
else : print('Not')

# endif not needed!! The indent defines when the loop is ended



# Looping
# for

for x in range(1,10):
    print(x, ' ', end= "")
print('\n')

for y in myList:
    print(y)

for z in [2,4,5]:
    print(z)

num_list = [[1,2,3],[10,20,30]]

for x in range(0,2):
    for y in range(0,3):
        print(num_list[x][y])


random_num = random.randrange(0,100)

#while(random_num != 15):
#    print(random_num)
#    random_num = random.randrange(0,100)

i = 0;
while (i <= 20) :
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue

    i+= 1



# functions

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1,4))

## user input
#print('What is your name')
#name = sys.stdin.readline()
#print('Hello ', name)


# Strings
long_string = 'hrvunknonsdf sdrnvso'
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4])

# %c = char, %s = string, %d = int, %f = float, %.5f = 5 desimaalin tarkkuudela float
print("%c is my %s letter and my number %d number is %.2f" %
      ('X','favorite',1,.14))

print(long_string.capitalize())
print(long_string.find("sdr"))
print(long_string.isalpha()) #miten tämä toimii?
print(long_string.isalnum())
print(long_string.replace("sdr","Toinen sana "))
print(long_string.strip()) # remove white space?? ei ainakaan keskeltä stringiä poista.
quote_list = long_string.split(" ")
print(quote_list)

# Files
test_file = open("test.txt", "wb")

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me to the file \n", 'UTF-8'))
test_file.close()
test_file = open("test.txt", "r+")

text_in_file= test_file.read()
print(text_in_file)
test_file.close()
os.remove("test.txt")


# Objects
# attributes "__" = private (set and get value only by using funtion inside of the object)
# attributes "_" = protected (usable for the inherited classes also)

class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    # constructor
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    
    def set_name(self, name): # "self" = object reference to itself (vrt. "this")
        self.__name = name

    def get_name(self):
        return self.__name

    def get_type(self):
        print("Animal")

    def get_sound(self):
        return self.__sound
    
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)


cat = Animal('Wiskers', 33,10,'Meow')
print(cat.toString())

# inheritance
class Dog(Animal):
    # Class Dog ingerits all functions and variables from the Class Animal
    __owner = ""

    #override the constructor of the Animal class
    def __init__(self, name, height, weight, sound, owner):    # additional set parameters
        self.__owner = owner   # Use the constructor of Animal class to handle the rest parameters
        super(Dog, self).__init__(name, height, weight, sound) #super = superclass

    def get_type(self):
        print("Dog")

#    def toString(self):
#        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)

    def multiple_sounds(self, how_many= None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()* how_many)


        
myDog = Dog("Hannu",11,11,"hau","Irpo")
myDog.multiple_sounds(3)


# Polymorphism

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(myDog)
