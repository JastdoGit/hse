import os


class WebClient:
    def __init__(self, name, sex, age, device_type, browser, bill, region):
        self.name = name
        self.sex = sex
        self.age = age
        self.device_type = device_type
        self.browser = browser
        self.bill = bill
        self.region = region

    def _get_gender_attributes(self):
        # Очищаем от пробелов и приводим к нижнему регистру для проверки
        sex_clean = self.sex.strip().lower()
        if sex_clean == 'female':
            return "женского пола", "совершила", "воспользовалась"
        elif sex_clean == 'male':
            return "мужского пола", "совершил", "воспользовался"
        else:
            return "пол не указан", "совершил(а)", "воспользовался(ась)"

    def _translate_device(self):
        device_clean = self.device_type.strip().lower()
        if self.device_type == 'mobile':
            return "смартфоном"
        elif self.device_type == 'desktop':
            return "стационарным компьютером"
        elif self.device_type == 'laptop':
            return "ноутбуком"
        elif self.device_type == 'tablet':
            return "планшетом"
        else:
            return self.device_type

    def form_description(self):
        sex_str, action_verb, use_verb = self._get_gender_attributes()
        device_str = self._translate_device()

        return (f"Пользователь: {self.name}, {sex_str}, {self.age} лет, "
                f"{action_verb} покупку на сумму {self.bill} у.е., "
                f"{use_verb} {device_str}, браузер: {self.browser}, "
                f"регион совершения покупки: {self.region}")


def load_clients_from_csv(file_path):
    clients_list = []
    print(f"Идёт отбработка данных")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Пропускаем заголовок
            data_lines = lines[1:]

            for line in data_lines:
                line = line.strip()
                if not line:
                    continue

                attributes = line.split(',')

                # Проверяем, что в строке достаточно данных
                if len(attributes) >= 7:
                    # ВАЖНО: Тут мы берем данные в том порядке, который вы указали
                    # 0=name, 1=device_type, 2=browser, 3=sex, 4=age, 5=bill, 6=region

                    new_client = WebClient(
                        name=attributes[0].strip(),
                        device_type=attributes[1].strip(),  # 1-й столбец
                        browser=attributes[2].strip(),  # 2-й столбец
                        sex=attributes[3].strip(),  # 3-й столбец
                        age=attributes[4].strip(),  # 4-й столбец
                        bill=attributes[5].strip(),  # 5-й столбец
                        region=attributes[6].strip()  # 6-й столбец
                    )
                    clients_list.append(new_client)

    except FileNotFoundError:
        print("\n!!! ОШИБКА !!!")
        print("Файл не найден.")

    return clients_list


def save_descriptions_to_txt(clients, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for client in clients:
                f.write(client.form_description() + '\n')
        print(f"\nУспешно, результат уже записан в файл web_clients_description.txt, и расположен здесь: {output_path}")
    except Exception as e:
        print(f"Ошибка при записи: {e}")


def main():
    # Пути к Рабочему столу (Desktop)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    input_file = os.path.join(desktop_path, 'web_clients_correct-старое.csv')
    output_file = os.path.join(desktop_path, 'web_clients_description.txt')

    clients = load_clients_from_csv(input_file)

    if clients:
        save_descriptions_to_txt(clients, output_file)
    else:
        print("В файле отсутствуют данные.")


if __name__ == '__main__':
    main()