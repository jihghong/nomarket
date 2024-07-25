nomarket 股市休市日期
=====================

使用方法 (請參考 [snippets/nomarket_demo.py](snippets/nomarket_demo.py))

    from datetime import date
    from nomarket import nomarket, prev_marketdates, prev_marketdate, next_marketdates, next_marketdate, marketdates_between

    print(nomarket(date(2024, 2, 4)))  # True
    print(nomarket(date(2024, 2, 5)))  # False

    print(prev_marketdate(date(2024, 2, 15)))  # 2024-02-05
    print(next_marketdate(date(2024, 2, 5)))   # 2024-02-15

    for d in prev_marketdates(date(2024, 2, 15), 3): print(d)
    # 2024-02-05
    # 2024-02-02
    # 2024-02-01

    for d in next_marketdates(date(2024, 2, 5), 3): print(d)
    # 2024-02-15
    # 2024-02-16
    # 2024-02-19

    for d in marketdates_between(date(2024, 2, 4), date(2024, 2, 16)): print(d)
    # 2024-02-05
    # 2024-02-15
    # 2024-02-16


安裝方法
--------

    pip install "nomarket @ git+https://www.github.com/jihghong/nomarket"

維護
----

目前僅提供台灣股市休市日期，如要參與維護，或擴充適用於全球市場，歡迎提出 pull request
