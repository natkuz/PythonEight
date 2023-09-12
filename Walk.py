# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle


def walk_directory(path: str):
    files_dict = {}
    for root, directories, files in os.walk(path): # пример цикла с тремя переменными из гугла подсмотрела
        files_dict[root] = []
        for directory in directories:
            files_dict[root].append((directory, 'directory', os.path.getsize(os.path.join(root, directory))))
        for file in files:
            files_dict[root].append((file, 'file', os.path.getsize(os.path.join(root, file))))
    return files_dict


def json_write(files_dict: str, path_json: str = 'json_file.json'):
    with open(path_json, 'w', encoding='UTF-8') as file:
        json.dump(files_dict, file, indent=6, ensure_ascii=False)


def csv_write(files_dict: dict, path_csv: str = 'csv_file.csv'):
    csv_cols = ['Путь', 'Папка/файл, размер']
    with open(path_csv, 'w', encoding='UTF-8') as file:
        csv_writer = csv.writer(file, dialect='excel', delimiter=' ', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(('Путь', 'Название', 'Тип', 'Размер'))
        for key, values in files_dict.items():
            if values:
                for value in values:
                    csv_writer.writerow([key, value[0], value[1], value[2]])
            else:
                csv_writer.writerow([key, None, None, None])


def pickle_write(files_dict: dict, path_pickle: str = 'pickle_file.pickle'):
    with open(path_pickle, 'wb') as file:
        pickle.dump(files_dict, file)


def pickle_load(path: str): # ну и проверку обратного вывода из pickle'файла взяла из семинара
    with open(path, 'rb') as file:
        files_dict = pickle.load(file)
        print(files_dict)


# walk_directory('C:\\Users\\MACHENIKE\\PycharmProjects\\pythonTasks\\venv\\PythonSeven')
# json_write(walk_directory('C:\\Users\\MACHENIKE\\PycharmProjects\\pythonTasks\\venv\\PythonSeven'))
# csv_write(walk_directory('C:\\Users\\MACHENIKE\\PycharmProjects\\pythonTasks\\venv\\PythonSeven'))
# pickle_write(walk_directory('C:\\Users\\MACHENIKE\\PycharmProjects\\pythonTasks\\venv\\PythonSeven'))
# print("Обратная распаковка Pickle'файла")
# pickle_load('pickle_file.pickle')