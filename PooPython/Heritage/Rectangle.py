class Rectangle:
    def __init__(self, lenght, width, height, color="red"):
        self.lenght = lenght
        self.width = width
        self.height = height
        self.color = color
    
    def calculate_area(self):
        return self.width * self.height
            
            
rec = Rectangle(5, 3, 5, "blue")
print(rec.lenght)

rec.color = "yellow"
print(rec.color)

area = rec.calculate_area()

print(area)