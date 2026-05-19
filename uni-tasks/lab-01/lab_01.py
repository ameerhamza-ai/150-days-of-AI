def calculate_bmi(weight,height):
    if height == 0:
        return "Height must greater than 0"
    bmi = weight / (height ** 2)
    
    if bmi < 18:
        status = "Underweight"
    elif bmi >= 18 and bmi <= 25:
        status = "Healthy"
    elif bmi > 25 and bmi <= 30:
        status = "Overweight"
    else:
        status = "Obese"
    
    return f"Weight: {weight} kg | Height: {height} m\nYour BMI is {bmi:.2f}\nYou're {status}"


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
print("---Final Report---")
result = calculate_bmi(weight,height)
print(result)