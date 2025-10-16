items = {
    'milk15': {'name': 'молоко 1.5%', 'count': '34', 'price': 89.9},
    'cheese': {'name': 'сыр молочный 1 кг.', 'count': '12', 'price': 990.9},
    'sausage': {'name': 'колбаса 1 кг.', 'count': '122', 'price': 1990.9}
}

price_less_20 = {
    key:
        int(value['count']) < 20
    for key, value in items.items()
}

print("Исходные данные:")

import pprint
pprint.pprint(items)

print(" ")

print("price_less_20 = {")
keys_list = list(price_less_20.keys())
for i, key in enumerate(keys_list):
    value = price_less_20[key]
    comma = ',' if i < len(keys_list) - 1 else ''
    print(f"'{key}': {value}{comma}")
print("}")