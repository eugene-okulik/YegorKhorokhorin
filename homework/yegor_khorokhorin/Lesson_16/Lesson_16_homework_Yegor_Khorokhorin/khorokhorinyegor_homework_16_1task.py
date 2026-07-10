import mysql.connector as mysql
import os
import csv
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)


cursor = db.cursor(dictionary=True)
if db.is_connected():
    print("Подключение успешно!")

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(base_path)))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    headers = next(file_data)

    check_data_query = """SELECT students.id FROM students
    JOIN `groups` ON students.group_id = `groups`.id
    JOIN books ON books.taken_by_student_id = students.id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjects ON lessons.subject_id = subjects.id
    WHERE students.name = %s
        AND students.second_name = %s
        AND `groups`.title = %s
        AND books.title = %s
        AND subjects.title = %s
        AND lessons.title = %s
        AND marks.value = %s
        """

    for row in file_data:
        name = row[0]
        second_name = row[1]
        group_title = row[2]
        book_title = row[3]
        subject_title = row[4]
        lesson_title = row[5]
        mark_value = row[6]

        cursor.execute(check_data_query, (name, second_name, group_title,
                                          book_title, subject_title, lesson_title, mark_value))
        result = cursor.fetchone()

        if result is None:
            print(row)
cursor.close()
db.close()
