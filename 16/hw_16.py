import datetime 

class Car:
    
    number_of_cars = 0
   
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
        Car.number_of_cars += 1

    def age_of_car(self):
        current_year = datetime.date.today().year
        return current_year - self.year

    def car_info(self):
        
        age = self.age_of_car() 
        print(f"\nბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}, ასაკი: {age} წელი")

   
    @classmethod
    def total_cars(cls):
        print(f"\nსულ ავტოპარკში: {cls.number_of_cars} მანქანა")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        
        super().__init__(brand, model, year)
        
        self.battery_life = battery_life

    
    def battery_info(self):
        print(f"\nამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი") 