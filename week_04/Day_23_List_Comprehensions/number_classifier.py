numbers = list(range(1, 21))

# Create 3 lists based on multiples of 3 and 5
multiples_of_3 = [x for x in numbers if x % 3 == 0]
multiples_of_5 = [x for x in numbers if x % 5 == 0]
multiples_of_both = [x for x in numbers if x % 3 == 0 and x % 5 == 0]

print("Multiples of 3:", multiples_of_3)
print("Multiples of 5:", multiples_of_5)
print("Multiples of both:", multiples_of_both)
