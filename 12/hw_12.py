import json, os

def create_file(directory, filename):
    
    file_path = None
    
    if len(directory.split('/')) == 2:

        file_path = f"{directory}/{filename}.json"

        os.makedirs(directory, exist_ok= True)
        print(f"საქაღალდე '{directory}' შეიქმნა.")

    else:
        print(f"საქაღალდის შექმნა ვერ მოხერხდა")
        return None
               
    try:
        with open(file_path, 'x', encoding='utf-8') as f:
            print(f"json ფაილი '{file_path}' წარმატებით შეიქმნა.") 
    except FileExistsError:
        print(f"ფაილი {file_path}, უკვე არსებობს")

    except Exception as e:
        print(f"შეცდომა ფაილის შექმნისას '{file_path}': {e}")
        return None
    
    return file_path


def read_file(filepath):

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"შეცდომა: ფაილი '{filepath}' არ მოიძებნა.")
        return []
    except json.JSONDecodeError:
        print(f"შეცდომა: ფაილი '{filepath}' ცარიელია ან არასწორი ფორმატისაა.")
        return [] 
    except IOError as e:
        print(f"შეცდომა ფაილის წაკითხვისას: {e}")
        return []

def write_data_to_file(filepath, json_data: list):
  
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json.dumps(json_data, indent=2))
        print(f"მონაცემები '{filepath}'-ში წარმატებით განახლდა.")
    except Exception as e:
        print(f"შეცდომა ფაილში ჩაწერისას: {e}")


def add_new_players(filepath, player: dict):
       
    current_data = read_file(filepath)
    
    if type(player["id"]) != int:
        print("მოთამაშის id არ არის ვალიდური...\n")
        return
    
    for user in current_data:
        if user['id'] == player['id']:
            print(f"მოთამაშე id: {player['id']}, უკვე არსებობს...")
            return
    else:
        current_data.append(player)
        current_data.sort(key=lambda i : i["id"])
    
    write_data_to_file(filepath, current_data)
    print(f"მოთამაშე '{player.get('name')}' დაემატა.")


def update_file(filepath):
    players = read_file(filepath)
    update_player = {}

    update_player['id'] = input("\nშეიყვანე ID ან დააჭირე enter: ") or None

    if update_player['id'] is None or not update_player['id'].isdigit():
        print("მოთამაშის ID არ არის ნატურალური რიცხვი")
        return
    
    for i in range(len(players)):
        update_player['id'] = int(update_player['id'])

        if update_player['id'] == players[i]['id']:
            update_player['name'] = input("შეიყვანე მოთამაშის სახელი ან დააჭირე enter: ") or players[i]["name"]

            update_player['country'] = input("შეიყვანე მოთამაშის ქვეყანა ან დააჭირე enter: ") or players[i]["country"]

            update_player['rating'] = input("შეიყვანე მოთამაშის რეიტინგი ან დააჭირე enter: ")
            update_player['rating'] = int(update_player['rating']) if update_player['rating'].isdigit() else players[i]["rating"]

            update_player['age'] = input("შეიყვანე მოთამაშის ასაკი ან დააჭირე enter: ")
            update_player['age'] = int(update_player['age']) if update_player['age'].isdigit() else players[i]["age"]

            players[i] = update_player

            break
    else:
        print(f"მოთამაშე ID: {update_player['id']}-ით არ მოიძებნა ")
        return
        
    write_data_to_file(filepath, players)
    print("მონაცემები წარმატებით შეიცვალა და ჩაიწერა ფაილში")










