## Program Assessement
# Class Vehicle
class Vehicle:
    def __init__(self, fare):
        self.fare = fare
# Part A create two instances of Vehicle,
class bus(Vehicle):
    def __init__(self):
        fare = Vehicle.fare
class car(Vehicle):
    def __init__(self, fare):
        self.fare = fare

# Use function __add__()
def total(b, c):    
    b = car.fare()
    c = bus.fare()
    def __add__(b, c):
        return b + c
# use function __gt__() and  __lt__()
def instances(x, y):
    x = car.fare 
    y = bus.fare
    def __gt__(x, y):
        return x > y
    def __lt__(x, y):
        return x < y
 
# Input fares
if __name__ == '__main__':
    def main():
        supermetro = Vehicle(1)
        bus_fare = float(input("Enter Bus fare: ")) 
        supermetro = bus(bus_fare)
    # Nissans 
        nissan = Vehicle(1)
        nissan_fare = float(input("Enter Nissans fare: ")) 
        nissan = car(nissan_fare)
    
    # give the total of the two fares
        print('Bus Fare is: $ {:.2f}'.format(bus_fare))
        print('Car Fare is: $ {:.2f}'.format(nissan_fare))
        print("Total fare is: ", total(bus_fare, nissan_fare))
main()

       
    
    