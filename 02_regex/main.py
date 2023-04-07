from pprint import pprint
import re
import csv

def edit_phonebook(filename):
    # Читаем адресную книгу в формате CSV в список contacts_list:
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contact_list = list(rows)


    # 1. Приводим ФИО к нормальному виду.
    for i, row in enumerate(contact_list):
        fio = ' '.join(row[0:3]) # получаем строку с ФИО
        list_fio = fio.split() # получаем корректный список с ФИО
        if len(list_fio) < 3: # это чтобы избежать ошибки индекса (в одном случае у нас нет отчества)
            list_fio.append('')
        for k in range(3): # заменяем в исходном списке ФИО, ФИО встают на свои поля.
            contact_list[i][k] = list_fio[k]

    # 2. форматируем телефоны
    pattern = r"(\+7|8)?\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s*)\(*(доб)?(\.)*\s*(\d+)*\)*"
    subst = r"+7(\2)\3-\4-\5\6\7\8\9"

    for i in range(len(contact_list)):
        res = re.sub(pattern, subst, contact_list[i][5])
        contact_list[i][5] = res

    # 3. Объединить все дублирующиеся записи о человеке в одну.
    result_list = [contact_list[0]] # записываем в новый лист первую строку
    for i in range(1, len(contact_list)):
        flag = 0 # флаг на совпадение (что такой человек уже есть)
        for j, raw in enumerate(result_list):
            if contact_list[i][0] == raw[0] and contact_list[i][1] == raw[1]:  # проверяем совпадение имени и фамилии
                for k in range(7): # проверяем на пустые значения и объединяем
                    if result_list[j][k] == '':
                        result_list[j][k] = contact_list[i][k]
                flag = 1
        if flag == 0: # если такого человека нет в списке - просто добавляем эту строку
            result_list.append(contact_list[i])

    # записываем результат в файл
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result_list)


if __name__ == "__main__":
    edit_phonebook("phonebook_raw.csv")