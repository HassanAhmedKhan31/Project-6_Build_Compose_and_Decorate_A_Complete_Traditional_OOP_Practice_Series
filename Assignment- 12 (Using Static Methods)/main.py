class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example
print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0
