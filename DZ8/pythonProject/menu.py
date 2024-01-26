def show_menu():
    print("\nВыберите пункт меню:\n"
          "1. Показать справочник целиком\n"
          "2. Найти по фамилии\n"
          "3. Изменить данные\n"
          "4. Удалить контакт\n"
          "5. Добавить контакт\n"
          "6. Завершить работу")
    choice = int(input(""))
    return choice

def read_txt(file_path):
    phonebook = []
    fields = ['Фамилия', 'Имя', 'Номер', 'Род занятий']

    with open(file_path, 'r', encoding='UTF-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phonebook.append(record)
    return phonebook

def write_txt(file_path, phonebook):
    with open(file_path, 'w', encoding='utf-8') as phout:
        for record in phonebook:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phonebook):
    for record in phonebook:
        print(record)

def change_number(phonebook, last_name, new_name):
    for record in phonebook:
        if record['Фамилия'] == last_name:
            record['Имя'] = new_name

def find_by_number(phonebook, last_name):
    for record in phonebook:
        if record['Фамилия'] == last_name:
            print(record)

def add_user(phonebook, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Род занятий']
    new_record = dict(zip(fields, user_data.split(',')))
    phonebook.append(new_record)

def delete_contact(phonebook, last_name):
    phonebook[:] = [record for record in phonebook if record['Фамилия'] != last_name]
# В файле menu.py

def change_contact(phonebook, last_name, field, new_value):
    for record in phonebook:
        if record['Фамилия'] == last_name:
            if field in record:
                record[field] = new_value
                print(f"Значение поля {field} для {last_name} успешно изменено.")
                return
            else:
                print(f"Ошибка: Поле {field} не найдено в контакте.")
                return
    print(f"Ошибка: Контакт с фамилией {last_name} не найден.")

# Остальной код оставляем без изменений
