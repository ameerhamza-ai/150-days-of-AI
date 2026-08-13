# Separate numbers from 1 to 30 into even and odd lists
evens = [x for x in range(1, 31) if x % 2 == 0]
odds = [x for x in range(1, 31) if x % 2 != 0]

# Print the results in the required format
print(f"Even: {evens}")
print(f"Odd: {odds}")
