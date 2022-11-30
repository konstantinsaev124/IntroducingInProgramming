class Vehicle():
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_vol = engine_vol
        self.max_speed = max_speed
        self.total_km = total_km
        self.max_passengers = max_passengers

    def print_info(self):
        print(f"Vehicle({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers})")

audi = Vehicle("audi","a6",1.9,220,100000,5)
audi.print_info()

class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, price, has_basket, max_passengers = 2):
        super().__init__(brand, model, engine_vol, max_speed,total_km,max_passengers)
        self.price = price
        self.has_basket = has_basket

skuter = Motorbike("audi","a6",1.9,220,100000,2000,True)
print(skuter.max_passengers)

class Car(Vehicle):
     def __init__(self, brand, model, engine_vol, max_speed, total_km, category, fuel_type,max_passengers = 4):
        super().__init__(brand, model, engine_vol, max_speed,total_km,max_passengers)
        self.category = category
        self.fuel_type  = fuel_type

audi = Car("audi","a6",1.9,220,100000,"combi","disel",)
print(audi.max_passengers)

class Bus(Vehicle):
     def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, company, year,):
        super().__init__(brand, model, engine_vol, max_speed,total_km, max_passengers)
        self.company = company
        self.year = year

bus = Bus("audi","a6",1.9,220,100000,12,"sonya", 1999)
print(bus.year)

bus1 = Bus("test1","test2",5.0,220,100000,12,"sonya", 1999)
bus2 = Bus("test5","test6",5.0,220,100000,12,"sonya", 1999)
bus3 = Bus("test3","test4",5.0,220,100000,12,"sonya", 1999)
audi1 = Car("audi","a6",1.9,220,100000,"combi","disel",)
VW2 = Car("VW","polo",3.0,300,100000,"hatchback","petrol")
audi3 = Car("audi","a4",2.0,150,100000,"combi","disel")
skuter1 = Motorbike("simson","v1.5",1.9,220,100000,2000,True)
skuter2 = Motorbike("honda","v1.5",1.9,220,100000,2000,True)
skuter3 = Motorbike("zid","v1.5",1.9,220,100000,2000,True)
skuter4 = Motorbike("yamaha","v1.5",1.9,220,100000,2000,True)

vehicles = [bus1,bus2,bus3,skuter4,audi1,VW2,audi3,skuter1,skuter2,skuter3]