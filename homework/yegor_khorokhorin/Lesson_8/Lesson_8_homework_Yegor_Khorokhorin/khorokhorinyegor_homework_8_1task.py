import random
salary_base = int(input('Введите зарплату : '))
bonus = random.choice([True, False])


def salary_bonus(salary):
    if bonus:
        bonus_amount = random.randrange(10, 100)
        print(f"Бонус получен! + {bonus_amount}")
        salary += bonus_amount
    else:
        print("Бонус не получен.", )
    return salary


final_salary = salary_bonus(salary_base)
print(f"{salary_base}, {bonus} - '${final_salary}'")
