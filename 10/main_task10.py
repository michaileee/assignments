'''1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და 
    zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

    params: [1, 2, 3], ['a', 'b', 'c']  
    outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]'''

#დავალება N1

def grouping(list1, list2):
    
    group = zip(list1, list2)

    return [str(a) for a in group]


param1 = [1, 2, 3]
param2 = ['a', 'b', 'c']

print(f'დაჯგუფებული ელემენტებია: {grouping(param1, param2)}')



'''2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და 
    აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), 
    თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
    ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

    params:[1, 2, 3, 4, 5] 
    output: 120'''

#დავალება N2

from functools import reduce
import sys

def number_multy(list1):
    
    try:
        multy = reduce(lambda a, b: a * b, list1)
        return multy
    
    except TypeError:
        print("შეყვანილი მონაცემების ტიპი არასწორია, დააზუსტეთ მონაცემები")
        sys.exit()

param = [1, 2, 3, 4, 5]

print(f'მიღებული სიის ელემენტების ნამრავლია: {number_multy(param)}')


'''3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და 
    აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

    params: [1, 2, 3, 4, 5, 6, 7]
    outputs: [1, 3, 5, 7]
'''

# დავალება N3

list1 = [1, 2, 3, 4, 5, 6, 7]

odd_list = list(filter(lambda a: a % 2 == 1, list1))

print(f'სიის კენტი ელემენტებია: {odd_list}')


'''4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
    დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. 
    გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც 
    აღმოჩნდა ისიც გაითვალისწინეთ.

    მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, 
    რომელიც მთავრდება რაღაც სიმბოლოებით...

    params: ['hello', 'world', 'coding', 'nod'], 'ing'  
    outputs: ['coding']'''

#დავალება N4

import sys

def check(list1, ending):

    try:
        x = list(filter(lambda a: a.endswith(ending), list1))

    except TypeError:
        print("შეყვანილი მონაცემების ტიპი არასწორია, დააზუსტეთ")
        sys.exit()

    except Exception as error:
        print(error)
        sys.exit()
    
    return x


param1 = ['hello', 'world', 'coding', 'ingnod']

param2 = 'ing'


print(check(param1, param2))