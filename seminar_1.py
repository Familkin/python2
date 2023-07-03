# Задание 0

dict1 = {'One': 1, 'Two': 2, 'Three': 3}
dict2 = {'Four': 4, 'Five': 5, 'Six': 6}
dict1.update(dict2)
print(dict1)

# Задание 1.2


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    dict1.update(dict2)
    return dict1


merge_dicts(dict1, dict2)

print(dict1)


# задание 2

keys = ['one', 'two', 'three']
values = [1, 2, 3]
result = dict()
for i in range(len(values)):
    result[keys[i]] = values[i]
print(result)

# Задание 2.2


def get_dict(keys: list, values: list) -> dict:
    return {keys[i]: values[i] for i in range(len(values))}


get_dict(keys, values)

# задание 3
# задание 3.1

client_dict = {
    "name": "John",
    "age": 25,
    "salary": 5000,
    "city": "Moscow"
}


def create_dict(client_dict: dict, keys: list = ['name', 'age']) -> dict:
    result = {}
    for i in keys:
        result[i] = client_dict[i]
    return result


create_dict(client_dict, ['salary', 'city'])

# задание 3.2
keys = ['name', 'age']
new_dict = {i: client_dict[i] for i in keys}
print(new_dict)

# дз


def calculate_revenue_by_month(dates: list[str], amounts: list[int]) -> dict[str, int]:
    revenue_by_month = {}
    for date, amount in zip(dates, amounts):
        month = date.split('-')[1]
        if month in revenue_by_month:
            revenue_by_month[month] += amount
        else:
            revenue_by_month[month] = amount
    return revenue_by_month


purchase_dates = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23',
                  '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
purchase_amounts = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037,
                    4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]

revenue_by_month = calculate_revenue_by_month(purchase_dates, purchase_amounts)
print("Выручка компании по месяцам:", revenue_by_month)
