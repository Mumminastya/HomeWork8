def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))

def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def edit_data() -> None:
    """Управление справочником."""
    condition = input('Введите, что хотите найти: ')
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    
    book = data.split('\n')
    search_elements = search(data, condition)
    if len(search_elements) == 0:
        print("Ничего не найдено")
        return
    editable_element = search_elements[0]
    index = book.index(editable_element)
    print(f"Запись для редактирования {editable_element} - {index}" )
    
    print('1. редактировать, 2. удалить')
    mode = int(input())
    if mode == 1:
        fio = input('Введите ФИО: ')
        phone_num = input('Введите номер телефона: ')
        book[index] = f'{fio} | {phone_num}'
    elif mode == 2:
        book.pop(index)
    else:
        return

    open('book.txt', 'w').close()
    with open('book.txt', 'a', encoding='utf-8') as new_book:
        for d in book:
            print(f'\n{d}')
            new_book.write(f'{d}\n')

    
def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def edit() -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))