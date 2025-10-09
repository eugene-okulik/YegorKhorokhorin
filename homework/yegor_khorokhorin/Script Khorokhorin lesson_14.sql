INSERT INTO students (name, second_name, ) VALUES ('Yegor', 'Khorokhorin')

UPDATE students SET group_id = 21283 WHERE id = 21306


INSERT INTO books (title, taken_by_student_id) VALUES ('Why?', 21306)

INSERT INTO books (title, taken_by_student_id) VALUES ('Because', 21306)


INSERT INTO `groups` (title, start_date, end_date) VALUES ('Yegor group', 'march 2025', 'sept 2025')


INSERT INTO subjects (title) VALUES ('SUBJ for YEGOR')

INSERT INTO subjects (title) VALUES ('SUBJ2 for YEGOR')

UPDATE subjects SET title = 'SUBJ3 for YEGOR' WHERE id = 12276


INSERT INTO lessons (title, subject_id) VALUES ('Lesson1 for SUBJ for YEGOR', 12274)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson1 for SUBJ2 for YEGOR', 12275)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson2 for SUBJ2 for YEGOR', 12276)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson2 for SUBJ for YEGOR', 12274)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson2 for SUBJ2 for YEGOR', 12275)

INSERT INTO lessons (title, subject_id) VALUES ('Lesson1 for SUBJ2 for YEGOR', 12276)


UPDATE lessons SET title = 'Lesson1 for SUBJ3 for YEGOR' WHERE id = 12747

UPDATE lessons SET title = 'Lesson2 for SUBJ3 for YEGOR' WHERE id = 12750


INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 12745, 21306)

INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 12746, 21306)

INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 12747, 21306)

INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 12748, 21306)

INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 12749, 21306)

INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 12750, 21306)


SELECT * FROM marks WHERE student_id = 21306

SELECT * FROM books WHERE taken_by_student_id  = 21306

SELECT * 
FROM students 
JOIN `groups` ON students.group_id = groups.id 
JOIN books ON students.id = books.taken_by_student_id 
JOIN marks ON students.id = marks.student_id 
JOIN lessons ON marks.lesson_id = lessons.id 
JOIN subjects ON lessons.subject_id = subjects.id WHERE students.id = 21306