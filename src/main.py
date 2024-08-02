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
                new_name_list.append(re.findall(r"\b[а-яА-ЯёЁA-Za-z^]+\b", name_items)[0])

    with open(full_path, "w", encoding="utf-8") as name_file:
        for name_items in new_name_list:
            name_file.write(name_items + "\n")

    return new_name_list


print(clear_name("names.txt"))
