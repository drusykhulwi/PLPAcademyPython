# Define the Smartphone class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life
        self.price = price

    def describe(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage, {self.battery_life}h battery life, priced at ${self.price}."

    def check_battery(self):
        if self.battery_life > 20:
            return "Battery life is good."
        else:
            return "Battery life is low. Consider charging."

# Define the Smartwatch class that inherits from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery_life, price, strap_material, waterproof):
        super().__init__(brand, model, storage, battery_life, price)
        self.strap_material = strap_material
        self.waterproof = waterproof

    def describe(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage, {self.battery_life}h battery life, {self.strap_material} strap, waterproof: {self.waterproof}, priced at ${self.price}."

    def check_waterproof(self):
        return "This smartwatch is waterproof." if self.waterproof else "This smartwatch is not waterproof."

# Create instances of Smartphone and Smartwatch
phone = Smartphone("Apple", "iPhone 14", 128, 30, 999)
watch = Smartwatch("Samsung", "Galaxy Watch 4", 16, 48, 299, "silicone", True)

# Display descriptions and check battery status
print(phone.describe())
print(phone.check_battery())
print(watch.describe())
print(watch.check_battery())
print(watch.check_waterproof())

# Define the base class Vehicle
class Vehicle:
    def move(self):
        pass

# Define the Car class that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Define the Plane class that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create instances of Car and Plane
my_car = Car()
my_plane = Plane()

# Call the move method on each instance
my_car.move()
my_plane.move()
