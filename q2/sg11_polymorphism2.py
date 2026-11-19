#1. Duck typing is a concept in Python where an object is fit for a specific task, regardless of its class or inheritance.
#2. It is needed to have the same method that the Dog and Cat classes have. It ;ets ot work in the same loop without inheriting from the Animal class directly.

# Create the Car class
class Car:
# Define the move method for the car
  def move(self):
    print("The car drives on the road.")
# Create the Boat class
class Boat:
# Define the move method for the boat
  def move(self):
    print("The boat sails on the water.")
# Create the Drone class
# Define the move method for the drone
  def move(self):
    print("The drone flies in the sky.")

# Create the start_trip function
def start_trip(vehicle):
# Call the move method of the given object
  vehicle.move()

# Create one object of each class
my_car = Car()
my_boat = Boat()
my_drone = Drone()

# Call the start_trip() function for each object
start_trip(my_car)
start_trip(my_boat)
start_trip(my_drone)

The code shows polymorphism because the single funtion, start_trip(vehicle), accepts objects from different classes. It focuses more on its moethod .move() rather than what class it will come from. This way, eacj object responds differently by doing its own specific action without needing a parent class 
