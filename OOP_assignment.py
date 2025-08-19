#Assignment 1 : design your own class!
class Smartphone:
    def __init__(self, phonename, user_input):
        self.__password="private"
        self.phonename=phonename
        self.turn_off=True
        self.user_input=user_input

    def turn_on(self):
        if self.__password==self.user_input:
            self.turn_off=False
            print(f"your {self.phonename} phone is turned on")
            return True
        else:
            print("incorrect password")
            return False


    def open_app(self, appname):
        if self.turn_off==False:
            print(f"{appname} is openning....")
        else:
            print("you have to open your phone first")
    

    
class Machine(Smartphone):
    def __init__(self, machinename):
        self.machine=machinename
    
    #polymorphism function
    def turn_on(self):
        print(f"the machine {self.machine} is turned off")


# #creating an object from Smartphone class
# phone=Smartphone("samsung A10", input("enter your password: "))
# #accessing methods of the Smartphone class
# phone.turn_on()
# phone.open_app("linkdin")

#Assignment 2: polymorphism

class Livingthings:
    def __init__(self, name):
        self.moving=True
        self.breath=True
        self.name=name

    def move(self):
        return f"{self.name} can move"
class Animal(Livingthings):

    def move(self):
        return f"{self.name} is moving"

class Human(Livingthings):
    
    def move(self):
        return f"{self.name} is moving"
# #polymorphism accessing
# print(Livingthings("all living things").move())
# print(Animal('goat').move())
# print(Human('berhe').move())
