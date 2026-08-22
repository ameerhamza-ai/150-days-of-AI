class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        # True if length equals width
        return self.length == self.width

    def scale(self, factor):
        self.length *= factor
        self.width *= factor
        print(f"Rectangle scaled by {factor}x.")

    def compare(self, other_rect):
        # Compare based on area
        if self.area() > other_rect.area():
            return "Larger"
        elif self.area() < other_rect.area():
            return "Smaller"
        else:
            return "Equal"

    def __str__(self):
        return f"Rectangle({self.length}x{self.width}) - Area: {self.area()}"

    # --- TESTING ---
r1 = Rectangle(10, 5)
r2 = Rectangle(5, 5)

print(r1)
print(f"Is r2 a square? {r2.is_square()}")
print(f"r1 compared to r2: {r1.compare(r2)}")
r2.scale(2)
print(r2)