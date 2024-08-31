def Car:
    def __init__ (self,bodytype, color = "white"):
        self.miieage = 0
        self.bodytype = bodytype
        self.color = color

    def drive(self, miles):
        self.mileage = self.mileage + miles
        print("So far", self.mileage, "miles")

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        if miles > self.mileage:
            self.mileage = miles
        else:
            print("Thats illegal")

def main():
    car1 = Car("Truck", "Red")
    car2 = Car("Van")
    car1.drive(30)
    car2.drive(90)
    miles = car1.get_mileage()
    print("Car1:", miles)
    car1.mileage = -100
    miles = car1.get_mileage()
    print("Car1 new mileage:", miles)

main()
