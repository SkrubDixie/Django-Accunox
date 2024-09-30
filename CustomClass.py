class Rectangle:
    def __init__(self, length: int, width: int):
        #Initializing with length and width in int format
        self.length = length
        self.width = width

    def __iter__(self):
        # Getting the length and width in the required order
        # yield is used to first print length, then iterate again and print width
        yield {'length': self.length}
        yield {'width': self.width}

# Example
rect = Rectangle(10, 5)

#Iterating over the class
for dimension in rect:
    print(dimension)
