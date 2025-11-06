'''chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს 
    ფაილის საქაღალდის მისამართს, ფაილის სახელს და შემქნის მას.

2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.

3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და 
    ჩაწერს/გაანახლებს ფაილის კონტენტს.

[
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.'''

from data import chess_players, new_players
from hw_12 import create_file, write_data_to_file, read_file, add_new_players, update_file

#საქაღალდის და ფაილის შექმნა
file_path = create_file("12/jsons", "data")

#ფაილში მონაცემების ჩაწერა
write_data_to_file(file_path, chess_players)

#ფაილიდან მონაცემების წაკითხვა
read_file_content = read_file(file_path)
for content in read_file_content:
    print(content)


#ახალი მოთამაშეების დამატება
for player in new_players:
    add_new_players(file_path, player)

#მონაცემების შეცვლა/განახლება ფაილში
update_file(file_path)
