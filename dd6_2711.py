import json

purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        dict_row = json.loads(line)
        if 'user_id' in dict_row and 'category' in dict_row:
            purchases[dict_row['user_id']] = dict_row['category']

with open('visit_log.csv', 'r', encoding='utf-8') as f_read, \
     open('funnel.csv', 'w', encoding='utf-8') as f_write:
    header = f_read.readline().strip()
    f_write.write(header + ',category\n')
    for line in f_read:
        line = line.strip()
        line_list = line.split(',')
        if len(line_list) < 2:
            continue
        user_id = line_list[0]
        if user_id in purchases:
            category = purchases[user_id]
            f_write.write(f"{line},{category}\n")

print("Готово! Программа завершена. Проверьте файл funnel.csv")