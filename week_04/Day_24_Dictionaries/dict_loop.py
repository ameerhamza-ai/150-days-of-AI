
# 1. Create a dictionary of countries and their capitals
countries_capitals = {
    "Pakistan": "Islamabad",
    "USA": "Washington D.C.",
    "UK": "London",
    "Japan": "Tokyo",
    "France": "Paris"
}

# 2. Loop through the dictionary using .items()
# .items() gives us both the key (country) and the value (capital) at the same time
print("--- Country and Capital List ---\n")

for country, capital in countries_capitals.items():
    print(f"Capital of {country} is {capital}")