try:
    input = input("Введите год: ")
    y = int(input)
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("Високосный год")
    else:
        print("Обычный год")

except ValueError:
    print("Необходимый формат ввода: целое число. Пожалуйста, повторите попытку.")
