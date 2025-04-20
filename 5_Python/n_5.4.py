import random as r
from datetime import date
from array import array

def number_of_days(d, m):
    for i in range(10):
        if m[i] in [1, 3, 5, 7, 8, 10, 12]:
            d.append(r.randint(1, 31))
        elif m[i] in [4, 6, 9, 11]:
            d.append(r.randint(1, 30))
        elif m[i] == 2 and years[i] % 4 == 0:
            d.append(r.randint(1, 29))
        else:
            d.append(r.randint(1, 28))

years = [r.randint(2020, 2025) for _ in range(10)]
months = [r.randint(1, 12) for _ in range(10)]
days = []
number_of_days(days, months)

dates = [date(years[i], months[i], days[i]) for i in range(10)]

arr = array('i', [])
begin = date(2020, 1, 1)
for d in dates:
    arr.append((d - begin).days)

for i in range(9):
    dev = abs(arr[i + 1] - arr[i])
    if 2 <= dev % 10 <= 4 and not(12 <= dev % 100 <= 14):
        w = "дня"
    elif dev % 10 == 1 and dev % 100 != 11:
        w = "день"
    else:
        w = "дней"
    print(f"Разница между {dates[i]} и {dates[i + 1]}: {dev} {w}")