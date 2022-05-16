# Задача 43. Реализовать RLE алгоритм - реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_3\02_Task_42_input_data.txt', 'r', encoding='utf8') as file:
    list_to_compress = file.read().split()
    list_to_compress = ' '.join(list_to_compress)

def count_elements(string):                     # Функция создает словарь со знаками из исходного списка в качестве ключей и количеством каждого знака из исходного списка в качестве значений                             
    dictionary = dict()
    for i in range(len(string)):
        count = 0
        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1
                dictionary[string[i]] = count            
    return dictionary

def combine_elements(dictionary):                 # Функция формирует из словаря строку с кодированными значениями
    combined_string = ''
    for key in dictionary:
        combined_string = combined_string + f'{dictionary[key]}{key}'
    return combined_string

print(list_to_compress)    
print(count_elements(list_to_compress))
print(combine_elements(count_elements(list_to_compress)))

with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_3\02_Task_42_compressed_data.txt', 'w', encoding='utf8') as file:
    file.write(combine_elements(count_elements(list_to_compress)))