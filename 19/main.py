import json
from faker import Faker

from random import choice



# student = Faker()

# students_list = [{'id': i, 
#                   'first_name': student.first_name(), 
#                   'last_name': student.last_name(), 
#                   'student_status': choice([True, False])} 
#                   for i in range(1,101)]


# with open('students.json', mode="w", encoding='utf-8') as file:
#     json.dump(students_list, file, indent=2)


with open('students.json', mode='r', encoding='utf-8') as file:

    students = json.load(file)

active = [st for st in students if st['student_status']]
in_active = [st for st in students if not st['student_status']]

students = {
    'active': active,
    'inactive': in_active
}

with open('students_new.json', mode='w', encoding='utf-8') as file:
    json.dump(students, file, indent=4)