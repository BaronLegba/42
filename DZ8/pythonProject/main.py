from menu import show_menu, read_txt, print_result, change_contact, find_by_number, add_user, write_txt, delete_contact

def main():
    phonebook = read_txt('telnum.txt')

    while True:
        choice = show_menu()
        if choice == 6:
            break
        elif choice == 1:
            print_result(phonebook)
        elif choice == 2:
            find_by_number(phonebook, input('Введите фамилию: '))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            field = input('Введите поле для изменения: ')
            new_value = input(f'Введите новое значение для поля {field}: ')
            change_contact(phonebook, last_name, field, new_value)
            write_txt('telnum.txt', phonebook)
        elif choice == 4:
            delete_contact(phonebook, input('Введите фамилию для удаления: '))
            write_txt('telnum.txt', phonebook)
        elif choice == 5:
            add_user(phonebook, input('Введите новые данные (Фамилия, Имя, Телефон, Род занятий): '))
            write_txt('telnum.txt', phonebook)

if __name__ == "__main__":
    main()
