'''1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, 
    რომელიც  მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს 
    პარამეტრად მიღებულ რიცხვს.'''
#დავალება N1

# int_list = [10, 20, 30, 40]

# x = input("შეიყვანეთ დასამატებელი პარამეტრი: ")

# def add_number(x):

#     global int_list

#     int_list.append(x)

# add_number(x)

# print(int_list)

'''
2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და 
    აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს შემდეგი სია 
    [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].'''
#დავალება N2

# num_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# def list_sum(num_list):

#     sum = 0
    
#     for i in num_list:
     
#         sum += i

#     return sum

# print(list_sum(num_list))


'''
3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია 
    რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს 
    (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას.'''

#დავალება N3

# gl_str = "global"

# def local():
#     gl_str = "local"

#     return gl_str

# print(gl_str)
# print(local())


'''
4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს
    number და დააბრუნებს  ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, 
    უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).'''
#დავალება N4

# number = input("შეიყვანეთ რიცხვი: ")


# def sum(number):

#     if len(number) == 1:
#         return int(number)
    
#     return int(number[-1]) + sum(number[:len(number)-1])

# print(sum(number))


'''
5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად 
    სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად  
    input: Hello   Output: olleH)'''
#დავალება N5

# text = input("შეიყვანეთ სტრიქონი: ")

# def revers_text(text):
    
#     if len(text) == 1:

#         return text
    
#     return text[-1]+ revers_text(text[:len(text)-1])

# print(revers_text(text))


#დავალება N6

def flatten(arg):
  for item in arg:
    if isinstance(item, (list, tuple, set, frozenset)):
      yield from flatten(item)
    elif isinstance(item, dict):
      yield from flatten(dict.values(item))
    else:
      yield item



# ==========================
arr = [1, 2, 3, [[4, 5, 6], "Text", 7], {'title':{'book':'The wolf','year': 1981 }, 'pages': 256}, (8, [9, 0], True, {5, 8, False})]

arr = list(flatten(arr))

print(arr)