import csv
import json


# Парсинг csv файла, получение списков книг, авторов и высоты книжного блока
def csv_info():
    title_list = []
    author_list = []
    height_list = []

    with open('./books.csv') as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            csv_dict = dict(zip(header, row))

            title_list.append(csv_dict.get('Title'))
            author_list.append(csv_dict.get('Author'))
            height_list.append(csv_dict.get('Height'))

    return title_list, author_list, height_list


# Парсинг json файла, получение списков имён, пола и адресов пользователей
def jsf_info():
    name_list = []
    gender_list = []
    address_list = []

    with open('./users.json') as jsf:
        reader_jsf = json.load(jsf)

        for json_dict in reader_jsf:

            name_list.append(json_dict.get('name'))
            gender_list.append(json_dict.get('gender'))
            address_list.append(json_dict.get('address'))

    return name_list, gender_list, address_list


# Создание структуры данных для записи в json файл
def generate_json_data():
    name_list = jsf_info()[0]
    gender_list = jsf_info()[1]
    address_list = jsf_info()[2]

    title_list = csv_info()[0]
    author_list = csv_info()[1]
    height_list = csv_info()[2]

    data_list = []

    for i in range(len(name_list)):

        # Обработка условий -  если книг > пользователей, то прекращаем раздавать книги; если наоборот - пустой массив
        if len(name_list) <= len(title_list):
            data = \
                {"name": name_list[i],
                 "gender": gender_list[i],
                 "address": address_list[i],
                 "books": [
                     {
                         "title": title_list[i],
                         "author": author_list[i],
                         "height": height_list[i]
                     }
                 ]
                 }
            data_list.append(data)

        else:
            if i <= len(title_list) - 1:
                data = \
                    {"name": name_list[i],
                     "gender": gender_list[i],
                     "address": address_list[i],
                     "books": [
                         {
                             "title": title_list[i],
                             "author": author_list[i],
                             "height": height_list[i]
                         }
                     ]
                     }
                data_list.append(data)
            else:
                data = \
                    {"name": name_list[i],
                     "gender": gender_list[i],
                     "address": address_list[i],
                     "books": []
                     }
                data_list.append(data)
    return data_list


# Создание итогового json файлa
def create_json():
    with open('./dz3.json', 'w') as dz_json:
        dz_json.write(json.dumps(generate_json_data(), indent=2))


if __name__ == '__main__':
    create_json()
