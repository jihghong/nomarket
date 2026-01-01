import datetime

nomarket_dates = set([
    datetime.date(2026, 1, 1),
    datetime.date(2026, 1, 3),
    datetime.date(2026, 1, 4),
    datetime.date(2026, 1, 10),
    datetime.date(2026, 1, 11),
    datetime.date(2026, 1, 17),
    datetime.date(2026, 1, 18),
    datetime.date(2026, 1, 24),
    datetime.date(2026, 1, 25),
    datetime.date(2026, 1, 31),
    datetime.date(2026, 2, 1),
    datetime.date(2026, 2, 7),
    datetime.date(2026, 2, 8),
    datetime.date(2026, 2, 12),
    datetime.date(2026, 2, 13),
    datetime.date(2026, 2, 14),
    datetime.date(2026, 2, 15),
    datetime.date(2026, 2, 16),
    datetime.date(2026, 2, 17),
    datetime.date(2026, 2, 18),
    datetime.date(2026, 2, 19),
    datetime.date(2026, 2, 20),
    datetime.date(2026, 2, 21),
    datetime.date(2026, 2, 22),
    datetime.date(2026, 2, 27),
    datetime.date(2026, 2, 28),
    datetime.date(2026, 3, 1),
    datetime.date(2026, 3, 7),
    datetime.date(2026, 3, 8),
    datetime.date(2026, 3, 14),
    datetime.date(2026, 3, 15),
    datetime.date(2026, 3, 21),
    datetime.date(2026, 3, 22),
    datetime.date(2026, 3, 28),
    datetime.date(2026, 3, 29),
    datetime.date(2026, 4, 3),
    datetime.date(2026, 4, 4),
    datetime.date(2026, 4, 5),
    datetime.date(2026, 4, 6),
    datetime.date(2026, 4, 11),
    datetime.date(2026, 4, 12),
    datetime.date(2026, 4, 18),
    datetime.date(2026, 4, 19),
    datetime.date(2026, 4, 25),
    datetime.date(2026, 4, 26),
    datetime.date(2026, 5, 1),
    datetime.date(2026, 5, 2),
    datetime.date(2026, 5, 3),
    datetime.date(2026, 5, 9),
    datetime.date(2026, 5, 10),
    datetime.date(2026, 5, 16),
    datetime.date(2026, 5, 17),
    datetime.date(2026, 5, 23),
    datetime.date(2026, 5, 24),
    datetime.date(2026, 5, 30),
    datetime.date(2026, 5, 31),
    datetime.date(2026, 6, 6),
    datetime.date(2026, 6, 7),
    datetime.date(2026, 6, 13),
    datetime.date(2026, 6, 14),
    datetime.date(2026, 6, 19),
    datetime.date(2026, 6, 20),
    datetime.date(2026, 6, 21),
    datetime.date(2026, 6, 27),
    datetime.date(2026, 6, 28),
    datetime.date(2026, 7, 4),
    datetime.date(2026, 7, 5),
    datetime.date(2026, 7, 11),
    datetime.date(2026, 7, 12),
    datetime.date(2026, 7, 18),
    datetime.date(2026, 7, 19),
    datetime.date(2026, 7, 25),
    datetime.date(2026, 7, 26),
    datetime.date(2026, 8, 1),
    datetime.date(2026, 8, 2),
    datetime.date(2026, 8, 8),
    datetime.date(2026, 8, 9),
    datetime.date(2026, 8, 15),
    datetime.date(2026, 8, 16),
    datetime.date(2026, 8, 22),
    datetime.date(2026, 8, 23),
    datetime.date(2026, 8, 29),
    datetime.date(2026, 8, 30),
    datetime.date(2026, 9, 5),
    datetime.date(2026, 9, 6),
    datetime.date(2026, 9, 12),
    datetime.date(2026, 9, 13),
    datetime.date(2026, 9, 19),
    datetime.date(2026, 9, 20),
    datetime.date(2026, 9, 25),
    datetime.date(2026, 9, 26),
    datetime.date(2026, 9, 27),
    datetime.date(2026, 9, 28),
    datetime.date(2026, 10, 3),
    datetime.date(2026, 10, 4),
    datetime.date(2026, 10, 9),
    datetime.date(2026, 10, 10),
    datetime.date(2026, 10, 11),
    datetime.date(2026, 10, 17),
    datetime.date(2026, 10, 18),
    datetime.date(2026, 10, 24),
    datetime.date(2026, 10, 25),
    datetime.date(2026, 10, 26),
    datetime.date(2026, 10, 31),
    datetime.date(2026, 11, 1),
    datetime.date(2026, 11, 7),
    datetime.date(2026, 11, 8),
    datetime.date(2026, 11, 14),
    datetime.date(2026, 11, 15),
    datetime.date(2026, 11, 21),
    datetime.date(2026, 11, 22),
    datetime.date(2026, 11, 28),
    datetime.date(2026, 11, 29),
    datetime.date(2026, 12, 5),
    datetime.date(2026, 12, 6),
    datetime.date(2026, 12, 12),
    datetime.date(2026, 12, 13),
    datetime.date(2026, 12, 19),
    datetime.date(2026, 12, 20),
    datetime.date(2026, 12, 25),
    datetime.date(2026, 12, 26),
    datetime.date(2026, 12, 27),
    datetime.date(2027, 1, 1)
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