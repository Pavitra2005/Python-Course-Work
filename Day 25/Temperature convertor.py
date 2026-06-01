class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def to_fahrenheit(self):
        return (self.celsius * 9/5)+32
    def to_celsius(self,fahrenheit):
        return (fahrenheit-32)*5/9

t=Temperature(25)
print("Fahrenheit:",t.to_fahrenheit())
print("Celsius from 98F:",t.to_celsius(20))
