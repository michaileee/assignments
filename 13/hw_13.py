
import csv
import os
from collections import defaultdict

HEADERS = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']

def create_csv(directory, filename):
   
    file_path = None
     
    if len(directory.split('/')) == 2:

        file_path = f"{directory}/{filename}.csv"

        os.makedirs(directory, exist_ok= True)
        print(f"საქაღალდე '{directory}' შეიქმნა.")

    else:
        print(f"საქაღალდის შექმნა ვერ მოხერხდა")
        return None
    
    try:
       with open(file_path, 'x', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            print(f"ფაილი '{file_path}' შეიქმნა სათაურებით.")
    except FileExistsError:
        print("ფაილი უკვე არსებობოს, შეგიძლიათ მოდიფიკაცია")
    except Exception as e:
        print(f"შეცდომა ფაილის შექმნისას: {e}")
    
    return file_path


def read_csv_data(file_path):
    
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            return data
        
    except FileNotFoundError:
        print(f"შეცდომა: ფაილი '{file_path}' არ მოიძებნა.")
        return []
    
    except Exception as e:
        print(f"შეცდომა ფაილის წაკითხვისას: {e}")
        return []
    

def write_csv_data(file_path, data):
    
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()  
            writer.writerows(data)

    except IOError as e:
        print(f"შეცდომა ფაილში ჩაწერისას: {e}")



def add_student(file_path):
    
    try:
        student_id = int(input("შეიყვანეთ ID: "))
        name = input("შეიყვანეთ სახელი: ")
        age = int(input("შეიყვანეთ ასაკი: "))
        grade = input("შეიყვანეთ შეფასება(A-D): ")
        subject_name = input("შეიყვანეთ საგნის სახელი: ")
        mark = int(input("შეიყვანეთ ქულა (mark): "))

    except ValueError:
        print("შეცდომა: ID, ასაკი და ქულა უნდა იყოს რიცხვი. სცადეთ თავიდან.")
        return

    new_student = {
        'id': student_id,
        'name': name,
        'age': age,
        'grade': grade,
        'subject_name': subject_name,
        'mark': mark
    }

    current_data = read_csv_data(file_path)

    current_data.append(new_student)
    

    try:
        current_data.sort(key=lambda x: int(x['id']))
    except ValueError:
        print("შეცდომა სორტირებისას: ზოგიერთი ID არ არის რიცხვი.")
    
    write_csv_data(file_path, current_data)
    print(f"სტუდენტი '{name}' (ID: {student_id}) წარმატებით დაემატა და დალაგდა.")



def read_students(file_path):
    
    student_id_input = input("შეიყვანეთ სტუდენტის ID (ყველას სანახავად დატოვეთ ცარიელი): ")
    
    all_data = read_csv_data(file_path)
    if not all_data:
        print("ფაილი ცარიელია ან მონაცემები არ მოიძებნა.")
        return

    if not student_id_input:

        print("ყველა სტუდენტის მონაცემები:")
        for row in all_data:
            print(f"  ID: {row['id']}, სახელი: {row['name']}, ასაკი: {row['age']}, კლასი: {row['grade']}, საგანი: {row['subject_name']}, ქულა: {row['mark']}")
    else:
        
        try:
            target_id = int(student_id_input)
            found_students = [row for row in all_data if int(row['id']) == target_id]
            
            if not found_students:
                print(f"სტუდენტი ID-ით {target_id} ვერ მოიძებნა.")
            else:
                print(f"მონაცემები სტუდენტისთვის ID: {target_id}:")
                for row in found_students:
                     print(f"  ID: {row['id']}, სახელი: {row['name']}, ასაკი: {row['age']}, კლასი: {row['grade']}, საგანი: {row['subject_name']}, ქულა: {row['mark']}")
        except ValueError:
            print("შეცდომა: ID უნდა იყოს რიცხვი.")


def calculate_average_marks(file_path):
      
    all_data = read_csv_data(file_path)
    if not all_data:
        print("მონაცემები არ არსებობს საშუალოს გამოსათვლელად.")
        return

    subject_marks = defaultdict(lambda: {'total': 0, 'count': 0})
    
    for row in all_data:
        try:
            subject = row['subject_name']
            mark = int(row['mark'])
            
            subject_marks[subject]['total'] += mark
            subject_marks[subject]['count'] += 1
        except (ValueError, TypeError):
            print(f"გაფრთხილება: არასწორი ქულის ფორმატი ჩანაწერში: {row}")
            continue
            
    if not subject_marks:
        print("საგნები ვერ მოიძებნა.")
        return
        
    for subject, data in subject_marks.items():
        if data['count'] > 0:
            average = data['total'] / data['count']
            print(f"საგანი: {subject} | საშუალო ქულა: {average} (სულ {data['count']} ჩანაწერი)")



def update_student_mark(file_path):

    try:
        target_id = int(input("შეიყვანეთ სტუდენტის ID: "))
        target_subject = input("შეიყვანეთ საგნის სახელი, რომლის განახლებაც გსურთ: ")
        new_mark = int(input("შეიყვანეთ ახალი ქულა: "))
    except ValueError:
        print("შეცდომა: ID და ქულა უნდა იყოს რიცხვი.")
        return

    all_data = read_csv_data(file_path)
    updated = False
    
    for row in all_data:
        try:
           
            if int(row['id']) == target_id and row['subject_name'] == target_subject:
                row['mark'] = new_mark  
                updated = True
                break 
        except ValueError:
            continue 

    if updated:
        write_csv_data(file_path, all_data)
        print(f"ქულა წარმატებით განახლდა: ID={target_id}, საგანი={target_subject}, ახალი ქულა={new_mark}")
    else:
        print(f"ჩანაწერი ვერ მოიძებნა: ID={target_id} და საგანი='{target_subject}'")

