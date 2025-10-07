import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('YEGOR', 'Khor', 1)")
student_id = cursor.lastrowid
cursor.execute(f'SELECT * FROM students WHERE id = {student_id}')
print(cursor.fetchone())


cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('WHY?', student_id))
book_1_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM books WHERE id = {book_1_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('BECAUSE', student_id))
book_2_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM books WHERE id = {book_2_id}')
print(cursor.fetchone())


cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Yegor group', 'march 2025', 'sept 2025')")
group_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM `groups` WHERE id = {group_id}')
print(cursor.fetchone())


cursor.execute("INSERT INTO subjects (title) VALUES ('SUBJ for YEGOR')")
subject_1_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM subjects WHERE id = {subject_1_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO subjects (title) VALUES ('SUBJ2 for YEGOR')")
subject_2_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM subjects WHERE id = {subject_2_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO subjects (title) VALUES ('SUBJ3 for YEGOR')")
subject_3_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM subjects WHERE id = {subject_3_id}')
print(cursor.fetchone())


cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s,%s)",
               ('Lesson1 for SUBJ for YEGOR', subject_1_id))
lesson_1_for_subj_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM lessons WHERE id = {lesson_1_for_subj_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s,%s)",
               ('Lesson2 for SUBJ for YEGOR', subject_1_id))
lesson_2_for_subj_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM lessons WHERE id = {lesson_2_for_subj_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s,%s)",
               ('Lesson1 for SUBJ2 for YEGOR', subject_2_id))
lesson_1_for_subj2_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM lessons WHERE id = {lesson_1_for_subj2_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s,%s)",
               ('Lesson2 for SUBJ2 for YEGOR', subject_2_id))
lesson_2_for_subj2_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM lessons WHERE id = {lesson_2_for_subj2_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s,%s)",
               ('Lesson1 for SUBJ3 for YEGOR', subject_3_id))
lesson_1_for_subj3_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM lessons WHERE id = {lesson_1_for_subj3_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s,%s)",
               ('Lesson2 for SUBJ3 for YEGOR', subject_3_id))
lesson_2_for_subj3_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM lessons WHERE id = {lesson_2_for_subj3_id}')
print(cursor.fetchone())


cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (5, lesson_1_for_subj_id, student_id))
mark_for_lesson_1_for_subj_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM marks WHERE id = {mark_for_lesson_1_for_subj_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (4, lesson_2_for_subj_id, student_id))
mark_for_lesson_2_for_subj_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM marks WHERE id = {mark_for_lesson_2_for_subj_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (3, lesson_1_for_subj2_id, student_id))
mark_for_lesson_1_for_subj2_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM marks WHERE id = {mark_for_lesson_1_for_subj2_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (5, lesson_2_for_subj2_id, student_id))
mark_for_lesson_2_for_subj2_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM marks WHERE id = {mark_for_lesson_2_for_subj2_id}')
print(cursor.fetchone())


cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (4, lesson_1_for_subj3_id, student_id))
mark_for_lesson_1_for_subj3_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM marks WHERE id = {mark_for_lesson_1_for_subj3_id}')
print(cursor.fetchone())

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               (3, lesson_2_for_subj3_id, student_id))
mark_for_lesson_2_for_subj3_id = cursor.lastrowid
cursor.execute(f'SELECT* FROM marks WHERE id = {mark_for_lesson_2_for_subj3_id}')
print(cursor.fetchone())


marks_of_student = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(marks_of_student, (student_id,))
print(cursor.fetchall())

books_of_student = "SELECT * FROM books WHERE taken_by_student_id = %s"
cursor.execute(books_of_student, (student_id,))
print(cursor.fetchall())


data_of_student = (
    "SELECT * FROM students "
    "JOIN `groups` ON students.group_id = groups.id "
    "JOIN books ON students.id = books.taken_by_student_id "
    "JOIN marks ON students.id = marks.student_id "
    "JOIN lessons ON marks.lesson_id = lessons.id "
    "JOIN subjects ON lessons.subject_id = subjects.id "
    "WHERE students.id = %s"
)
cursor.execute(data_of_student, (student_id,))
print(cursor.fetchall())

db.commit()

db.close()
