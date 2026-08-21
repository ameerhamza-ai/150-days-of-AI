class Calculator:
    def __init__(self) -> None:
        self.history: list[str] = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        record = f"{a} + {b} = {result}"
        self.history.append(record)
        return result

    def subtract(self,a:float,b:float) -> float:
        result = a - b 
        record = f"{a} - {b} = {result}"
        self.history.append(record)
        return result 

    def multiply(self,a:float,b:float) -> float:
        result = a * b 
        record = f"{a} * {b} = {result}"
        self.history.append(record)
        return result 

    def divide(self,a:float,b:float) -> float | None:
        if b == 0:
            print("Error: Division by zero is not allowed!")
            record = f"{a} / {b} = Error (Division by zero)"
            self.history.append(record)
            return None
        result = a / b
        record = f"{a} / {b} = {result:.2f}"
        self.history.append(record)
        return result 
    
    def show_history(self) -> None:
        if not self.history:
            print("History is currently empty.")
            return

        print("=== Calculation History ===")
        for index, item in enumerate(self.history, start=1):
            print(f"{index}. {item}")

    def clear_history(self) -> None:
        self.history.clear()
        print("History cleared successfully.")


if __name__ == "__main__":
    calc = Calculator()

    
    print("Addition Result:", calc.add(10, 5))
    print("Subtraction Result:", calc.subtract(20, 8))
    print("Multiplication Result:", calc.multiply(4, 6))
    print("Division Result:", calc.divide(50, 2))
    print("Zero Division Test:", calc.divide(10, 0))

    print("\n" + "=" * 35 + "\n")

    calc.show_history()

    print("\n" + "=" * 35 + "\n")

    calc.clear_history()
    calc.show_history()

    