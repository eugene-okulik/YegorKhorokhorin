answer_1 = 'Результат операции: 42'
colon_index = answer_1.index(":")
number_str = answer_1[colon_index + 1:].strip()
result = int(number_str) + 10
print("Pезультат операции и сложения:", result)

answer_2 = 'Результат операции: 514'
colon_index_2 = answer_2.index(':')
number_str_2 = answer_2[colon_index_2 + 1:].strip()
result_2 = int(number_str_2) + 10
print("Pезультат операции и сложения_2:", result_2)

answer_3 = 'Результат работы программы: 9'
colon_index_3 = answer_3.index(':')
number_str_3 = answer_3[colon_index_3 + 1:].strip()
result_3 = int(number_str_3) + 10
print("Результат работы программы и сложения:", result_3)
