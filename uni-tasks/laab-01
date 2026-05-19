def calculate_efficiency(distance,fuel_used):
    if fuel_used <= 0:
        return "Fuel used must be grater than 0"
    efficiency = distance / fuel_used
    
    if efficiency > 20:
        status = "Car is fuel efficient"
    elif efficiency > 15 and efficiency <= 20:
        status = "Consumption is good"
    elif efficiency > 10 and efficiency <= 15:
        status = "Consumption is high"
    else:
        status = "Car needs tuning"
    return f"Distance travelled: {distance} km\nFuel used: {fuel_used} liters\nEfficiency: {efficiency:.2f} KM/L\nStatus: {status}"

distance = float(input("Enter distance travelled in km: "))
fuel_used = float(input("Enter fuel consumption in liters: "))

result = calculate_efficiency(distance,fuel_used)
print("\n" + result)
