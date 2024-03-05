"""Creating a Car class with parameters and instances"""

# Define the Car class
class Car:
    make = "Basic"
    model = "Car"
    """Creating a Car class with parameters"""

def __init__(self, make, model):
    self.make = make
    self.model = model

# Create an instance of the Car class using the user's input
my_car = Car("Toyota", "Camry")
# Print the details of the car
print(f'Make: {}')