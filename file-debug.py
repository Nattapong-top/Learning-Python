def map_10():
    book_list = []
    data_books = [
                '978-616-000-001 | Python 101 | 599',
                '978-616-000-002 | Data Science Fund. | 850',
                '978-616-000-003 | Network Security | 675.50'
                ]
    for item in data_books:
        isbn, title, price_str = item.strip().split(' | ')
        price_float =  float(price_str)
        book_dict = {
            'isbn': isbn,
            'title': title,
            'price': price_float
        }
        book_list.append(book_dict)
    print(book_dict)
    print(book_dict)
map_10()