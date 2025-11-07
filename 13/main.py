'''შექმენით csv  ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

id,name,age,grade,subject_name,mark
1,string,0,string,string,0
2,string,0,string,string,0


1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფორმაციას
    (id,name,age,grade,subject_name,mark) და თქვენ სტუდენტს დაამატებს csv ფაილში. 
    დაასორტირეთ მონაცემები id-ის მიხედვით.

2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, 
    ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.

3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.

4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის 
    განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.'''

from hw_13 import create_csv, add_student, read_students, calculate_average_marks, update_student_mark

file_path = create_csv("13/csv", "students")

while True:
           
        choice = input(''' ::::::სტუდენტების მართვა ::::::: 
                       
            1. სტუდენტის დამატება
            2. სტუდენტის ინფორმაციის ნახვა
            3. საშუალო ქულების დათვლა საგნების მიხედვით
            4. სტუდენტის ქულის განახლება
            5. გამოსვლა
                       
            Choose Option: ''')
        
        if choice == '1':
            add_student(file_path)
        elif choice == '2':
            read_students(file_path)
        elif choice == '3':
            calculate_average_marks(file_path)
        elif choice == '4':
            update_student_mark(file_path)
        elif choice == '5':
            print("პროგრამა ითიშება")
            break
        else:
            print("გთხოვთ, აირჩიოთ რიცხვი 1-დან 5-მდე.")