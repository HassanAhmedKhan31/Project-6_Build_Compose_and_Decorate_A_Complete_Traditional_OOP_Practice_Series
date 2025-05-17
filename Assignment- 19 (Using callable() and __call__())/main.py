class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Example
m = Multiplier(3)
print(callable(m))  # True
print(m(10))        # Output: 30
