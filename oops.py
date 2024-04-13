class Kettle(object):

    power_source = "Electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    
    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 9.66
print(kenwood.price)

hamilton = Kettle("Hamilton", 12.44)
hamilton.switch_on()
print(hamilton.on)

print(Kettle.power_source)
print(hamilton.power_source)
print(kenwood.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)