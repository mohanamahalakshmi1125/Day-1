class Flyer:
    def fly(self):
        return "Can fly"
class Swimmer:
    def swim(self):
        return "Can swim"
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Duck quacks"

duck = Duck()
print(duck.fly())   
print(duck.swim())  
print(duck.quack()) 