import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(base_path)))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_file_path)

with open(eugene_file_path) as file:
    for i, line in enumerate(file, start=1):
        parts = line.strip().split()
        date_str = parts[1] + ' ' + parts[2]
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        # print(date_obj)
        if i == 1:
            print(date_obj + datetime.timedelta(weeks=2))
        elif i == 2:
            print(date_obj.strftime("%A"))
        elif i == 3:
            now = datetime.datetime.now()
            delta = now - date_obj
            print(delta.days)
