# Задача 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

origin_list = [1, 2, 3, 5, 1, 5, 3, 10]

def sort_list(lst):                     # Функция создает словарь с числами из исходного списка в качестве ключей и количеством каждого числа из исходного списка в качестве значений                             
    sorted_nums = dict()
    for i in range(len(lst)):
        count = 0
        for j in range(0,len(lst)):
            if lst[i] == lst[j]:
                count += 1
                sorted_nums[lst[i]] = count            
    return sorted_nums

dictionary = sort_list(origin_list)
print([key for key in dictionary if dictionary[key] == 1]) # Проверяем полученный при помощи функции sort_list словарь на уникальность элементов




