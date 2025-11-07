'''1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).
'''
#დავალება N1

words = input("შეიყვანეთ მიმდევრობა: ")

items = words.split()           

uniqe_items = set(items)            

print(uniqe_items)


'''2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი 
    სიმრავლე, რომლის შეცვლაც შეუძლებელი იქნება (frozenset).'''

#დავალება N2

words = input("შეიყვანეთ მიმდევრობა: ")

items = words.split()           

uniqe_items = frozenset(items)            

print(uniqe_items)


'''
3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. 
    დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).'''

#დავალება N3

first = set({57, 57})

second = set({56, 56})

both = first.union(second)
print(tuple(both))

'''
4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). 
    დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).'''

#დავალება N4

numbers = tuple(input("შეიყვანეთ მიმდევრობა: ").split())

uniqe_items = list(set(numbers))

print(uniqe_items)

'''
5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
[("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

დაბეჭდეთ შემდეგი ფორმატით:

Name: Gega, Age: 24
Name: Gaga, Age: 21
Name: Goga, Age: 19
Name: Giga, Age: 27
Name: Gagi, Age: 11 '''

#დავალება N5

list1 = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for i in list1:
    print(f"name: {i[0]}, age: {i[1]}")

'''
6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
დავბეჭდოთ თანხვედრა.'''

#დავალება N6

customer_list1 = ["Irakli", "Giorgi", "Nona", "Oto"]

customer_list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

customer_list1, customer_list2 = set(customer_list1), set(customer_list2)

cross_list = customer_list1.intersection(customer_list2)

print(f"თანხვედრა: {cross_list}")