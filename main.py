# while True:
#     text = input('Введите текст (0 - закончить): ')
#     if text == '0': break
#     with open('notes.txt', 'a', encoding="utf-8") as file:
#         file.write(text + '\n')
#
#
# def watchFile():
#     print('Содержимое файла: ')
#     with open('notes.txt', 'r', encoding="utf-8") as file:
#         content = file.read()
#         return content
#
# print(watchFile())

# import random
# with open('numbers.txt', 'w', encoding='utf-8') as file:
#     for _ in range(10):
#         file.write(str(random.randint(1, 100)))
#         file.write(' ')
#
# res = []
# with open('numbers.txt', 'r', encoding='utf-8') as file:
#     nums = list(map(int, file.readline().split()))
#
#     with open('result.txt', 'w', encoding='utf-8') as file2:
#         file2.write(f'Сумма: {sum(nums)}; ср ариф: {sum(nums) / len(nums)}' )

import csv
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    students = set()
    all_rows = list(reader)

    for row in all_rows:
        students.add(row[0])

    for s in students:
        sm = 0
        c = 0

        for row in all_rows:
            if s == row[0]:
                sm += int(row[2])
                c += 1
        print(s, sm / c)