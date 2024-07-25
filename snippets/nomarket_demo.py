from datetime import date
from nomarket import nomarket, prev_marketdates, prev_marketdate, next_marketdates, next_marketdate, marketdates_between

print(f"{nomarket(date(2024, 2, 1))=}")
print(f"{nomarket(date(2024, 2, 2))=}")
print(f"{nomarket(date(2024, 2, 3))=}")
print(f"{nomarket(date(2024, 2, 4))=}")
print(f"{nomarket(date(2024, 2, 5))=}")
print(f"{nomarket(date(2024, 2, 6))=}")
print(f"{nomarket(date(2024, 2, 7))=}")
print(f"{nomarket(date(2024, 2, 8))=}")
print(f"{nomarket(date(2024, 2, 9))=}")
print(f"{nomarket(date(2024, 2, 10))=}")
print(f"{nomarket(date(2024, 2, 11))=}")
print(f"{nomarket(date(2024, 2, 12))=}")
print(f"{nomarket(date(2024, 2, 13))=}")
print(f"{nomarket(date(2024, 2, 14))=}")
print(f"{nomarket(date(2024, 2, 15))=}")
print(f"{nomarket(date(2024, 2, 16))=}")
print(f"{prev_marketdate(date(2024, 2, 15))=}")
print(f"{prev_marketdate(date(2024, 2, 15), inclusive=True)=}")
print(f"{prev_marketdate(date(2024, 2, 15), 6)=}")
print(f"{prev_marketdate(date(2024, 2, 15), 6, inclusive=True)=}")
print(f"{next_marketdate(date(2024, 2, 5))=}")
print(f"{next_marketdate(date(2024, 2, 5), inclusive=True)=}")
print(f"{next_marketdate(date(2024, 2, 5), 6)=}")
print(f"{next_marketdate(date(2024, 2, 5), 6, inclusive=True)=}")
print(f"{list(prev_marketdates(date(2024, 2, 15)))=}")
print(f"{list(prev_marketdates(date(2024, 2, 15), inclusive=True))=}")
print(f"{list(prev_marketdates(date(2024, 2, 15), 6))=}")
print(f"{list(prev_marketdates(date(2024, 2, 15), 6, inclusive=True))=}")
print(f"{list(next_marketdates(date(2024, 2, 5)))=}")
print(f"{list(next_marketdates(date(2024, 2, 5), inclusive=True))=}")
print(f"{list(next_marketdates(date(2024, 2, 5), 6))=}")
print(f"{list(next_marketdates(date(2024, 2, 5), 6, inclusive=True))=}")
print('marketdates_between(date(2024, 2, 1), date(2024, 2, 16))')
for d in marketdates_between(date(2024, 2, 1), date(2024, 2, 16)): print(d)