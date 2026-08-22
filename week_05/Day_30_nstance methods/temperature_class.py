class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def is_freezing(self):
        return self.celsius <= 0

    def is_boiling(self):
        return self.celsius >= 100

    def increase(self, amount):
        self.celsius += amount
        print(f"Temperature increased by {amount}°C.")

    def decrease(self, amount):
        self.celsius -= amount
        print(f"Temperature decreased by {amount}°C.")

    def __str__(self):
        return f"{self.celsius}°C / {self.to_fahrenheit():.1f}°F / {self.to_kelvin():.2f}K"

    # --- TESTING ---
t1 = Temperature(25)
t2 = Temperature(0)
t3 = Temperature(100)

print(t1)
print(f"Is t2 freezing? {t2.is_freezing()}")
print(f"Is t3 boiling? {t3.is_boiling()}")
t1.increase(10)
print(t1)