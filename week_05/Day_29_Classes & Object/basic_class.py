class Car:
    def __init__ (self,brand: str,model:str,year:int,color:str) -> None:
        self.brand = brand 
        self.model = model 
        self.year = year 
        self.color = color 

    def display_info(self) -> str:
        return (f"Car Brand: {self.brand} | Model: {self.model} | "
                f"Launched: {self.year} | Color: {self.color}")

    def start_engine(self) -> str:
        return f"{self.brand} {self.model} engine started!"

# Car 1 Instance
car1 = Car("Toyota", "Corolla Altis Grande", 2024, "Super White")
print("==== Car 1 Info ====")
print(car1.display_info())
print(car1.start_engine())

print()

# Car 2 Instance
car2 = Car("Hyundai", "Tucson", 2025, "Phantom Black")
print("==== Car 2 Info ====")
print(car2.display_info())
print(car2.start_engine())
        