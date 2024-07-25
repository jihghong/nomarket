import datetime

nomarket_dates = set([
    datetime.date(2024, 1, 1),
    datetime.date(2024, 2, 6),
    datetime.date(2024, 2, 7),
    datetime.date(2024, 2, 8),
    datetime.date(2024, 2, 9),
    datetime.date(2024, 2, 10),
    datetime.date(2024, 2, 11),
    datetime.date(2024, 2, 12),
    datetime.date(2024, 2, 13),
    datetime.date(2024, 2, 14),
    datetime.date(2024, 2, 28),
    datetime.date(2024, 4, 4),
    datetime.date(2024, 4, 5),
    datetime.date(2024, 5, 1),
    datetime.date(2024, 6, 10),
    datetime.date(2024, 9, 17),
    datetime.date(2024, 10, 10),
    datetime.date(2024, 1, 6),
    datetime.date(2024, 1, 7),
    datetime.date(2024, 1, 13),
    datetime.date(2024, 1, 14),
    datetime.date(2024, 1, 20),
    datetime.date(2024, 1, 21),
    datetime.date(2024, 1, 27),
    datetime.date(2024, 1, 28),
    datetime.date(2024, 2, 3),
    datetime.date(2024, 2, 4),
    datetime.date(2024, 2, 17),
    datetime.date(2024, 2, 18),
    datetime.date(2024, 2, 24),
    datetime.date(2024, 2, 25),
    datetime.date(2024, 3, 2),
    datetime.date(2024, 3, 3),
    datetime.date(2024, 3, 9),
    datetime.date(2024, 3, 10),
    datetime.date(2024, 3, 16),
    datetime.date(2024, 3, 17),
    datetime.date(2024, 3, 23),
    datetime.date(2024, 3, 24),
    datetime.date(2024, 3, 30),
    datetime.date(2024, 3, 31),
    datetime.date(2024, 4, 6),
    datetime.date(2024, 4, 7),
    datetime.date(2024, 4, 13),
    datetime.date(2024, 4, 14),
    datetime.date(2024, 4, 20),
    datetime.date(2024, 4, 21),
    datetime.date(2024, 4, 27),
    datetime.date(2024, 4, 28),
    datetime.date(2024, 5, 4),
    datetime.date(2024, 5, 5),
    datetime.date(2024, 5, 11),
    datetime.date(2024, 5, 12),
    datetime.date(2024, 5, 18),
    datetime.date(2024, 5, 19),
    datetime.date(2024, 5, 25),
    datetime.date(2024, 5, 26),
    datetime.date(2024, 6, 1),
    datetime.date(2024, 6, 2),
    datetime.date(2024, 6, 8),
    datetime.date(2024, 6, 9),
    datetime.date(2024, 6, 15),
    datetime.date(2024, 6, 16),
    datetime.date(2024, 6, 22),
    datetime.date(2024, 6, 23),
    datetime.date(2024, 6, 29),
    datetime.date(2024, 6, 30),
    datetime.date(2024, 7, 6),
    datetime.date(2024, 7, 7),
    datetime.date(2024, 7, 13),
    datetime.date(2024, 7, 14),
    datetime.date(2024, 7, 20),
    datetime.date(2024, 7, 21),
    datetime.date(2024, 7, 24),
    datetime.date(2024, 7, 25),
    datetime.date(2024, 7, 27),
    datetime.date(2024, 7, 28),
    datetime.date(2024, 8, 3),
    datetime.date(2024, 8, 4),
    datetime.date(2024, 8, 10),
    datetime.date(2024, 8, 11),
    datetime.date(2024, 8, 17),
    datetime.date(2024, 8, 18),
    datetime.date(2024, 8, 24),
    datetime.date(2024, 8, 25),
    datetime.date(2024, 8, 31),
    datetime.date(2024, 9, 1),
    datetime.date(2024, 9, 7),
    datetime.date(2024, 9, 8),
    datetime.date(2024, 9, 14),
    datetime.date(2024, 9, 15),
    datetime.date(2024, 9, 21),
    datetime.date(2024, 9, 22),
    datetime.date(2024, 9, 28),
    datetime.date(2024, 9, 29),
    datetime.date(2024, 10, 5),
    datetime.date(2024, 10, 6),
    datetime.date(2024, 10, 12),
    datetime.date(2024, 10, 13),
    datetime.date(2024, 10, 19),
    datetime.date(2024, 10, 20),
    datetime.date(2024, 10, 26),
    datetime.date(2024, 10, 27),
    datetime.date(2024, 11, 2),
    datetime.date(2024, 11, 3),
    datetime.date(2024, 11, 9),
    datetime.date(2024, 11, 10),
    datetime.date(2024, 11, 16),
    datetime.date(2024, 11, 17),
    datetime.date(2024, 11, 23),
    datetime.date(2024, 11, 24),
    datetime.date(2024, 11, 30),
    datetime.date(2024, 12, 1),
    datetime.date(2024, 12, 7),
    datetime.date(2024, 12, 8),
    datetime.date(2024, 12, 14),
    datetime.date(2024, 12, 15),
    datetime.date(2024, 12, 21),
    datetime.date(2024, 12, 22),
    datetime.date(2024, 12, 28),
    datetime.date(2024, 12, 29),
    datetime.date(2025, 1, 1)
])

def nomarket(date):
    return date in nomarket_dates

daydelta = datetime.timedelta(days=1)

def prev_marketdates(date, n=1, inclusive=False):
    if inclusive and not nomarket(date):
        yield date
        n -= 1
    while n > 0:
        date -= daydelta
        if not nomarket(date):
            yield date
            n -= 1

def prev_marketdate(date, n=1, inclusive=False):
    if inclusive and not nomarket(date): n -= 1
    while n > 0:
        date -= daydelta
        if not nomarket(date): n -= 1
    return date

def next_marketdates(date, n=1, inclusive=False):
    if inclusive and not nomarket(date):
        yield date
        n -= 1
    while n > 0:
        date += daydelta
        if not nomarket(date):
            yield date
            n -= 1

def next_marketdate(date, n=1, inclusive=False):
    if inclusive and not nomarket(date): n -= 1
    while n > 0:
        date += daydelta
        if not nomarket(date): n -= 1
    return date

def marketdates_between(begin_date, end_date):
    if end_date < begin_date: return
    date = begin_date
    while date <= end_date:
        if not nomarket(date): yield date
        date += daydelta