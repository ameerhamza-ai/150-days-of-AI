# Create a 3x3 multiplication table using nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]

# Print the matrix formatted row by row
for row in matrix:
    print(row)
