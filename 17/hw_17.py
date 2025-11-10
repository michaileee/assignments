

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, arguments):
        return Vector(self.x +arguments.x, self.y + arguments.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    

class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author
    
    def __eq__(self, books):

        return True if self.name == books.name and self.author == books.author else False


class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("brand უნდა იყოს ტექსტი")
        if not value.strip():
            raise ValueError("brand არ შეიძლება იყოს ცარიელი")
        self._brand = value.strip()

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError("model უნდა იყოს ტექსტი")
        if not value.strip():
            raise ValueError("model არ შეიძლება იყოს ცარიელი")
        self._model = value.strip()

    # --- year ---
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("year უნდა იყოს მთელი რიცხვი")
        self._year = value

    def __str__(self):
        return f"{self.brand} {self.model} - {self.year} წელს გამოშვებული"



    
