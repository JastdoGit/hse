documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

owner_by_number = {}
for doc in documents:
    owner_by_number[doc['number']] = doc['name']

shelf_by_number = {}
for shelf, docs_list in directories.items():
    for doc_number in docs_list:
        shelf_by_number[doc_number] = shelf

while True:
    command = input("\nВведите команду: \n")

    if command == 'p':
        doc_number = input("Введите номер документа: \n")

        owner_name = owner_by_number.get(doc_number)

        if owner_name:
            print(f"Владелец документа: {owner_name}")
        else:
            print("Документ с таким номером не найден. Пожалуйста, повторите попытку.")

    elif command == 's':
        doc_number = input("Введите номер документа: \n")

        shelf_number = shelf_by_number.get(doc_number)

        if shelf_number:
            print(f"Документ хранится на полке: {shelf_number}")
        else:
            print("Документ с таким номером не найден. Пожалуйста, повторите попытку.")

    elif command == 'q':
        break

    else:
        print("Неизвестная команда. Доступные команды: 'p', 's', 'q'.")