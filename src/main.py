import os
import re


def clear_name(file_names: str) -> list:
    """Удаляет знаки препинания и цифры и возвращать только строки, содержащие имя"""

    new_name_list = list()
    base_path = r"C:\Users\user\Desktop\skyPro\practic\lesons\lesons"
    full_path = os.path.join(base_path, "data", file_names)

    with open(full_path, "r", encoding="utf-8") as name_file:
        name_list = name_file.read().split()
        for name_items in name_list:
            if re.findall(r"\b[а-яА-ЯёЁA-Za-z]+\b", name_items):
                new_name_list.append(re.findall(r"\b[а-яА-ЯёЁA-Za-z]+\b", name_items)[0])

    # with open(full_path, "w", encoding="utf-8") as name_file:
    #     for name_items in new_name_list:
    #         name_file.write(name_items + "\n")

    return new_name_list


def filter_russian_names(name_list: list) -> list:
    """Фильтрация имен написанных на русском"""
    rus_name_list = list()
    for name_items in name_list:
        if re.findall(r"\b[а-яА-ЯёЁ]+\b", name_items):
            rus_name_list.append(re.findall(r"\b[а-яА-ЯёЁ]+\b", name_items)[0])

    return rus_name_list

def filter_english_names(name_list: list) -> list:
    """Фильтрация имен написанных на английском"""
    english_name_list = list()
    for name_items in name_list:
        if re.findall(r"\b[a-zA-Z]+\b", name_items):
            english_name_list.append(re.findall(r"\b[a-zA-Z]+\b", name_items)[0])

    return english_name_list


def save_to_file(file_name:str, data:str) ->None:
    """Функция сщздает фаил и записывает в него, полученные данные"""
    base_path = r"C:\Users\user\Desktop\skyPro\practic\lesons\lesons"
    full_path = os.path.join(base_path, "data", file_name)

    with open(full_path, "w", encoding="utf-8") as name_file:
        name_file.write(data)


if __name__ == "__main__":
    name_list = clear_name("names.txt")
    rus_name_list = filter_russian_names(name_list)
    save_to_file("rus_name.txt", "\n".join(rus_name_list))
    eng_name = filter_english_names(name_list)
    save_to_file("eng_name.txt", "\n".join(eng_name))