class Vehicle:
    def move(self):
        print("This vehicle is moving.")
    
class Car(Vehicle):
    def move(self):
        print("Driving on the road.")

class Bicycle(Vehicle):
    def move(self):
        print("Pedling on the road.")

vehicles = [Car(), Bicycle(), Vehicle()]

for vehicle in vehicles:
    vehicle.move()