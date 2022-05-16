# Задача 38. Напишите программу, удаляющую из текста все слова содержащие "абв"

# Считываем данные из текстового файла '07_Task_38_origin_file.txt'
with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_3\01_Task_38_origin_file.txt', 'r', encoding='utf8') as file:
    text = file.read().split()

def remove_words(word, text):   # Функция удаляет из текста все слова, содержащие заданную комбинацию символов
    for i in text:
        if word in i:
            text.remove(i)
    return text

# Перезаписываем файл. Для удобства проверки работы программы создаем новый файл с результатом '07_Task_38_result_file.txt'
with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Homework\Python_homework_3\01_Task_38_result_file.txt', 'w', encoding='utf8') as file:
    file.write(' '.join(remove_words('абв', text)))