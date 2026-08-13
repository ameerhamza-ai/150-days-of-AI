numbers = list(range(1, 16))

# 1. Ternary expression: Even if divisible by 2, else Odd
even_odd_labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

# 2. Ternary expression: Fizz if divisible by 3, else the number itself
fizz_labels = ["Fizz" if x % 3 == 0 else x for x in numbers]

print("Even/Odd:", even_odd_labels)
print("Fizz Filter:", fizz_labels)
