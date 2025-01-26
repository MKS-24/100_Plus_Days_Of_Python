class MyClass:
    def __init__(self, value):
        # Constructor mein private variable initialize karein
        self._value = value  # Private attribute

    # Getter method
    def get_value(self):
        return self._value

    # Setter method
    def set_value(self, new_value):
        if isinstance(new_value, int) and new_value >= 0:  # Validation
            self._value = new_value
        else:
            raise ValueError("Value must be a positive integer")

# Object creation
obj = MyClass(10)  # Constructor se value initialize
print(obj.get_value())  # Getter method call, output: 10

obj.set_value(20)  # Setter method call
print(obj.get_value())  # Getter method call, output: 20

# Invalid value set karne ki koshish
try:
    obj.set_value(-5)  # Validation fail karega
except ValueError as e:
    print(e)  # Output: Value must be a positive integer



# bad way to set and set value inside constructor