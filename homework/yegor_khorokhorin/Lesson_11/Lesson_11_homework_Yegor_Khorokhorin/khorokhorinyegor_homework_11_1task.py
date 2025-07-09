class Book:
    material_pages = 'paper'
    text_availability = True

    def __init__(self, title, author, number_of_pages, isbn, reservation=False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = isbn
        self.reservation = reservation

    def reserve(self):
        self.reservation = True

    def unreserve(self):
        self.reservation = False

    def __str__(self):
        status = "зарезервирована" if self.reservation is True else ""
        result = (f" Название: '{self.title}', Автор: '{self.author}', страниц: {self.number_of_pages},"
                  f" материал: {self.material_pages}, ISBN: {self.ISBN}")
        if status:
            result += f", {status}"
        return result


class SchoolBooks(Book):
    def __init__(self, title, author, number_of_pages, isbn, subject, group, count_of_tasks, reservation=False):
        super().__init__(title, author, number_of_pages, isbn, reservation)
        self.subject = subject
        self.group = group
        self.count_of_tasks = count_of_tasks

    def __str__(self):
        status = "зарезервирована" if self.reservation else ""
        result = (f" Название: '{self.title}', Автор: '{self.author}', страниц: {self.number_of_pages},"
                  f"предмет: {self.subject}, класс: {self.group}, заданий: {self.count_of_tasks}")
        if status:
            result += f", {status}"
        return result


first_book = Book('1984', 'Джордж Оруэлл',
                  328, 9780451524935, True)
second_book = Book('Мастер и Маргарита', 'Михаил Булгаков',
                   384, 9785699931411, False)
third_book = Book('Преступление и наказание', 'Фёдор Достоевский',
                  671, 9780140449136, False)
fourth_book = Book('To Kill a Mockingbird', 'Харпер Ли',
                   336, 9780061120084, False)
fifth_book = Book('The Great Gatsby', 'Фрэнсис Скотт Фицджеральд',
                  180, 9780743273565, False)
sixth_book = SchoolBooks('Algebra', 'Ivanov',
                         200, 1010101,
                         'Mathematic', 9, True, True)
seventh_book = SchoolBooks('Geography', 'Petrov',
                           250, 2020202,
                           'Geography', 5, True, False)
eighth_book = SchoolBooks('English for beginners', 'Murphy',
                          250, 3030303,
                          'English', 1, True, False)

print(first_book)
print(second_book)
print(third_book)
print(fourth_book)
print(fifth_book)
print(sixth_book)
print(seventh_book)
print(eighth_book)
