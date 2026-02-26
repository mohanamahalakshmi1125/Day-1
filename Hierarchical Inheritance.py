class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Dog barks"
class Cat(Animal):
    def meow(self):
        return "Cat meows"
dog = Dog()
cat = Cat()
print(dog.speak())  
print(cat.speak())  
print(dog.bark())   
print(cat.meow())   