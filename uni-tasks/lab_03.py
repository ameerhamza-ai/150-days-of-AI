class CarMonitor:
    def __init__(self,distance,fuel_used):
        self.__distance = distance 
        self.__fuel_used = fuel_used 

    def getDistance(self):
        return self.__distance
    def getFuel(self):
        return self.__fuel_used
    def setDistance(self,distance):
        if distance <= 0:
            return "Error! Distance must be greater than 0"
        else:
            self.__distance = distance 
    def setFuel(self,fuel_used):
        if fuel_used <= 0:
            return "Error! Fuel consumption must be greater than 0"
        else:
            self.__fuel_used = fuel_used 
        
    def get_efficiency(self):
        if self.__fuel_used == 0:
            return "Cannot calculate efficiency (Fuel is 0)"
        efficiency = self.__distance / self.__fuel_used
        
        if efficiency > 20:
            status = "Car is fuel efficient"
        elif efficiency > 15 and efficiency <= 20:
            status = "Consumption is good"
        elif efficiency > 10 and efficiency <= 15:
            status = "Consumption is high"
        else:
            status = "Car needs tuning"

        return f"Efficiency: {efficiency:.2f} KM/L\nCar status: {status}"
    def __str__(self):
        return f"Distance travelled: {self.__distance} km\nFuel used: {self.__fuel_used} liters\n{self.get_efficiency()}"
    
_distance = float(input("Enter distance travelled in km: "))
_fuel_used = float(input("Enter fuel consumption in liters: "))
print("===Final Report===")
v1 = CarMonitor(_distance,_fuel_used)
print(v1)