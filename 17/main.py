'''1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. 
    კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ ვექტორების დამატება და __str__ მეთოდი, რომელიც დააბრუნებს 
    შემდეგი სახის სტრიქონს "(x, y)".

მაგალითად:
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (5, 7)

2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი 
    რომელიც შეამოწმებს ორი წიგნის ტოლობას.
    ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

მაგალითად:
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False


3. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის 
__new__ და __init__ მეთოდის გადაფარვა.

Car კლასს დაუმატეთ  თითოეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.

დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ 
იყოს ყოველთვის მთელი და ა.შ.'''

from hw_17 import Vector, Book, Car

#N1. დავალება 
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v4 = Vector(1, 2)

v3 = v1 + v2 + v4

print(v3)


#N2. დავალება

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2)
print(book1 == book3)

#N3. დავალება
car1 = Car("Toyota", "Corolla", 2020)

car1.year = 2025

print(car1)
