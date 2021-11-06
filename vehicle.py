## Program Assessement
# Class Vehicle
class Vehicle:
    def __init__(self, fare):
        self.fare = fare
# Part A create two instances of Vehicle,
class bus(Vehicle):
    def __init__(self, fare):
        self.fare = fare
        
class car(Vehicle):
    def __init__(self, fare):
        self.fare = fare
        

# use function __gt__() and  __lt__()

 
# Input fares
if __name__ == '__main__':
    def main():
        
        def instances(bus_, car_):
            bus_ = bus(1)
            bus_.fare
    # Nissans 
            car_ = car(1)
            car_.fare
        def __gt__(x, y):
            return x > y
        def __lt__(x, y):
            return x < y
        # Use function __add__()
        def total(b, c):    
            b = car.fare()
            c = bus.fare()
        def __add__(b, c):
            return b + c
    # give the total of the two fares
        bus_ = float(input("Enter the fare: "))
        car_ = float(input("Enter Bus fare: "))
        print(instances(bus_, car_))
        print("Total fare is: ", total(b, c))
main()

       
    
    