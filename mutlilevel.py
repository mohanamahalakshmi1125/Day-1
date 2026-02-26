class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Dog barks"
class Puppy(Dog):
    def weep(self):
        return "Puppy weeps"
puppy = Puppy()
print(puppy.speak())  
print(puppy.bark())   
print(puppy.weep())