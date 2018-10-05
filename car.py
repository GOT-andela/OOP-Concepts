class Car(object):

    max_speed = 120
    max_gear = 6

    def __init__(self, name, color, gear=1, speed=0):
        self.name = name
        self.color = color
        self.gear = gear
        self.speed = speed

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

    def get_color(self):
        color = "the color is " + self.color
        return color

    def get_gear(self):
        return self.gear

    def increase_speed(self):
        if self.speed < self.max_speed:
            self.speed += 1
        else:
            self.speed = 0

    def increase_speed(self, incr):
        if self.speed < self.max_speed:
            self.speed += inr
        else:
            self.speed = 0

    def decrease_speed(self):
        if self.speed > 80:
            self.speed -= 1

    def increase_gear(self):
        if self.gear > 0 and segetNamelf.gear < self.max_gear:
            self.gear += 1

    def decrease_gear(self):
        if self.gear > 0:
            self.gear -= 1


class Lorry(Car):

    max_gear = 12

    def __init__(self, name, color, weight):
        Car.__init__(self, name, color)
        self.weight = weight

    def increase_gear(self):
        if self.gear > 0 and self.gear < self.max_gear:
            self.gear += 1


from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def getSpeed(self):
        pass

    @abstractmethod
    def getName(self):
        pass

class Bus(Vehicle):
    def getSpeed(self):
        pass
    def getName(self):
        pass

bus = Bus()
print(bus)

# mycar = Car("Subaru", 'Red')
# print(mycar.get_name())
# print(mycar.get_color())
# mycar.increase_gear()
# print(mycar.get_gear())
# print(mycar.get_speed())
# mycar.increase_speed()
# print(mycar.get_speed())
# myLor = Lorry("Isuzu", "white", 100)
# myLor1 = Lorry("Isuzu", "white", 100)
# myLor2 = Lorry("Isuzu", "white", 100)
# myLor3 = Lorry("Isuzu", "white", 100)
# myLor4 = Lorry("Isuzu", "white", 100)
# print(isinstance(myLor,Lorry))
