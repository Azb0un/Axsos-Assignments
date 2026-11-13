class EvenOddChecker:
    # Stores the number given by the user
    def __init__(self, number):
        self.number = number

    # Uses modulo (%) to check if the number is even or odd
    def check(self):
        if self.number % 2 == 0:
            return f"{self.number} is an even number."
        else:
            return f"{self.number} is an odd number."


# Ask the user for a whole number and convert it to an integer
user_input = int(input("Enter a whole number: "))

# Create an object from the class and display the result
checker = EvenOddChecker(user_input)
print(checker.check())