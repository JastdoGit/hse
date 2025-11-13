from datetime import datetime

DATE_FORMATS = [
    "%A, %B %d, %Y",
    "%A, %d.%m.%y",
    "%A, %d %B %Y",
]

print("Введите строку с датой или 'q' для завершения.")

while True:
    user_input = input("Введите дату: ")

    if user_input.lower() == 'q':
        print("Завершение программы.")
        break

    parsed_date = None

    for fmt in DATE_FORMATS:
        try:
            parsed_date = datetime.strptime(user_input, fmt)

            print(f"Datetime: {parsed_date}")
            break
        except ValueError:
            continue

    if parsed_date is None:
        print("Ошибка: Этот формат не распознан. Попробуйте снова.")