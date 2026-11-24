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

# import csv
# with open('students.csv', 'r') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     students = set()
#     all_rows = list(reader)
#
#     for row in all_rows:
#         students.add(row[0])
#
#     for s in students:
#         sm = 0
#         c = 0
#
#         for row in all_rows:
#             if s == row[0]:
#                 sm += int(row[2])
#                 c += 1
#         print(s, sm / c)




# with open('app.log', 'r', encoding='utf-8') as file:
#     with open('errors.txt', 'w', encoding='utf-8') as file2:
#         for r in file:
#             if 'ERROR' in r:
#                 file2.write(r)



# with open('app.log', 'r', encoding='utf-8') as file:
#     data = {
#         'errors': 0,
#         'warnings': 0,
#         'infos': 0,
#     }
#
#     for r in file:
#         if 'ERROR' in r:
#             data['errors'] += 1
#         if 'WARNING' in r:
#             data['warnings'] += 1
#         if 'INFO' in r:
#             data['infos'] += 1
#     with open('report.txt', 'w', encoding='utf-8') as file2:
#         file2.write(str(data))
#     print(data)



# def do_task(title):
#     lst = []
#     with open('tasks.txt', 'r', encoding='utf-8') as f:
#         for r in f:
#             if title == ' '.join(r.split()[1:]) and r[0] + r[1] == '[]':
#                 lst.append(r[0] + 'X' + r[1:])
#             else:
#                 lst.append(r)
#
#     with open('tasks.txt', 'w', encoding='utf-8') as f:
#         for l in lst:
#             f.write(l if l.endswith('\n') else l + '\n')
#
#
#
#
# def add_task(title):
#     with open('tasks.txt', 'r', encoding='utf-8') as f:
#         lines = [l for l in f]
#     if f'[] {title}\n' not in lines and f'[X] {title}\n' not in lines:
#         with open('tasks.txt', 'a', encoding='utf-8') as f2:
#             f2.write(f'[] {title}\n')
#
#
# add_task('Картошку пожарить')
# add_task('Помыться')
# do_task('Сыграть в роблокс')
# add_task('Баскет сыграть')
# do_task('Картошку пожарить')

def safe_read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []
    except PermissionError:
        print(f"Нет прав на чтение файла '{filename}'.")
        return []
    except UnicodeDecodeError:
        print(f"Файл '{filename}' не удалось прочитать как текст (кодировка).")
        return []
    except OSError as e:
        print(f"Не удалось открыть '{filename}': {e}")
        return []

print(safe_read('tasks.txt'))
print(safe_read('no_such_file.txt'))
print(safe_read('/root/secret.txt'))
print(safe_read('.'))