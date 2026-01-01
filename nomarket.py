import datetime

nomarket_dates = set([
    datetime.date(2025, 1, 1),
    datetime.date(2025, 1, 4),
    datetime.date(2025, 1, 5),
    datetime.date(2025, 1, 11),
    datetime.date(2025, 1, 12),
    datetime.date(2025, 1, 18),
    datetime.date(2025, 1, 19),
    datetime.date(2025, 1, 23),
    datetime.date(2025, 1, 24),
    datetime.date(2025, 1, 25),
    datetime.date(2025, 1, 26),
    datetime.date(2025, 1, 27),
    datetime.date(2025, 1, 28),
    datetime.date(2025, 1, 29),
    datetime.date(2025, 1, 30),
    datetime.date(2025, 1, 31),
    datetime.date(2025, 2, 1),
    datetime.date(2025, 2, 2),
    datetime.date(2025, 2, 8),
    datetime.date(2025, 2, 9),
    datetime.date(2025, 2, 15),
    datetime.date(2025, 2, 16),
    datetime.date(2025, 2, 22),
    datetime.date(2025, 2, 23),
    datetime.date(2025, 2, 28),
    datetime.date(2025, 3, 1),
    datetime.date(2025, 3, 2),
    datetime.date(2025, 3, 8),
    datetime.date(2025, 3, 9),
    datetime.date(2025, 3, 15),
    datetime.date(2025, 3, 16),
    datetime.date(2025, 3, 22),
    datetime.date(2025, 3, 23),
    datetime.date(2025, 3, 29),
    datetime.date(2025, 3, 30),
    datetime.date(2025, 4, 3),
    datetime.date(2025, 4, 4),
    datetime.date(2025, 4, 5),
    datetime.date(2025, 4, 6),
    datetime.date(2025, 4, 12),
    datetime.date(2025, 4, 13),
    datetime.date(2025, 4, 19),
    datetime.date(2025, 4, 20),
    datetime.date(2025, 4, 26),
    datetime.date(2025, 4, 27),
    datetime.date(2025, 5, 1),
    datetime.date(2025, 5, 3),
    datetime.date(2025, 5, 4),
    datetime.date(2025, 5, 10),
    datetime.date(2025, 5, 11),
    datetime.date(2025, 5, 17),
    datetime.date(2025, 5, 18),
    datetime.date(2025, 5, 24),
    datetime.date(2025, 5, 25),
    datetime.date(2025, 5, 30),
    datetime.date(2025, 5, 31),
    datetime.date(2025, 6, 1),
    datetime.date(2025, 6, 7),
    datetime.date(2025, 6, 8),
    datetime.date(2025, 6, 14),
    datetime.date(2025, 6, 15),
    datetime.date(2025, 6, 21),
    datetime.date(2025, 6, 22),
    datetime.date(2025, 6, 28),
    datetime.date(2025, 6, 29),
    datetime.date(2025, 7, 5),
    datetime.date(2025, 7, 6),
    datetime.date(2025, 7, 12),
    datetime.date(2025, 7, 13),
    datetime.date(2025, 7, 19),
    datetime.date(2025, 7, 20),
    datetime.date(2025, 7, 26),
    datetime.date(2025, 7, 27),
    datetime.date(2025, 8, 2),
    datetime.date(2025, 8, 3),
    datetime.date(2025, 8, 9),
    datetime.date(2025, 8, 10),
    datetime.date(2025, 8, 16),
    datetime.date(2025, 8, 17),
    datetime.date(2025, 8, 23),
    datetime.date(2025, 8, 24),
    datetime.date(2025, 8, 30),
    datetime.date(2025, 8, 31),
    datetime.date(2025, 9, 6),
    datetime.date(2025, 9, 7),
    datetime.date(2025, 9, 13),
    datetime.date(2025, 9, 14),
    datetime.date(2025, 9, 20),
    datetime.date(2025, 9, 21),
    datetime.date(2025, 9, 27),
    datetime.date(2025, 9, 28),
    datetime.date(2025, 10, 4),
    datetime.date(2025, 10, 5),
    datetime.date(2025, 10, 6),
    datetime.date(2025, 10, 10),
    datetime.date(2025, 10, 11),
    datetime.date(2025, 10, 12),
    datetime.date(2025, 10, 18),
    datetime.date(2025, 10, 19),
    datetime.date(2025, 10, 25),
    datetime.date(2025, 10, 26),
    datetime.date(2025, 11, 1),
    datetime.date(2025, 11, 2),
    datetime.date(2025, 11, 8),
    datetime.date(2025, 11, 9),
    datetime.date(2025, 11, 15),
    datetime.date(2025, 11, 16),
    datetime.date(2025, 11, 8),
    datetime.date(2025, 11, 22),
    datetime.date(2025, 11, 23),
    datetime.date(2025, 11, 29),
    datetime.date(2025, 11, 30),
    datetime.date(2025, 12, 6),
    datetime.date(2025, 12, 7),
    datetime.date(2025, 12, 13),
    datetime.date(2025, 12, 14),
    datetime.date(2025, 12, 20),
    datetime.date(2025, 12, 21),
    datetime.date(2025, 12, 25),
    datetime.date(2025, 12, 27),
    datetime.date(2025, 12, 28),
    datetime.date(2026, 1, 1)
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