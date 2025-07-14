# class Appliance:
#     def __init__(self,brand):
#         self.brand=brand
#
#     def turnOn(self):
#             print("The "+self.brand+" appliance is now on.")
#
# class WashingMachine(Appliance):
#     def startWash(self):
#         print("Washing clothes with "+self.brand+ " washing machine.")
#
# def main():
#     wm = WashingMachine("Samsung")
#     wm.turnOn()
#     wm.startWash()
#
#
# if __name__ == "__main__":
#     main()



# class Employee:
#     def __init__(self,name):
#         self.name=name
#
#     def introduce(self):
#         print("Hello, I am "+self.name)
#
#
# class Manager(Employee):
#     def introduce(self):
#         super().introduce()
#         print("I am a manager.")
#
# def main():
#     manager=Manager("Alice")
#     manager.introduce()
#
#
# if __name__ == "__main__":
#     main()




# class Vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#
#     def showBrand(self):
#         print("Brand:", self.brand)
#
# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model
#
#     def displayDetails(self):
#         print("Brand: " + self.brand)
#         print("Model: " +self.model )
#
# def main():
#     car = Car("Toyota", "Corolla")
#     car.displayDetails()
#
#
# if __name__ == "__main__":
#     main()




# class Animal:
#     def __init__(self,name):
#         self.name=name
#
#     def makeSound(self):
#         print("This animal makes a sound")
#
# class Dog(Animal):
#     def makeSound(self):
#         print("Woof")
#
# class Cat(Animal):
#     def makeSound(self):
#         print("Meow")
#
# def main():
#     d = Dog("Buddy")
#     c = Cat("Kitty")
#     d.makeSound()
#     c.makeSound()
#
#
# if __name__ == "__main__":
#     main()








