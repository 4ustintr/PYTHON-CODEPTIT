def create_books():
    books = []
    for i in range(5):
        name = input("Nhập tên sách: ")
        code = input("Nhập mã số sách: ")
        num_page = int(input("Nhập số trang sách: "))
        author = input("Nhập tên tác giả: ")
        type = input("Nhập thể loại sách: ")
        describe = input("Nhập mô tả sách: ")
        books.append({'name': name, 'code': code, 'num_page': num_page, 'author': author, 'type': type, 'describe': describe})
    return books
def print_authors_and_types(books):
    authors = set([book['author'] for book in books])
    types = set([book['type'] for book in books])
    print("Các tác giả khác nhau: ", authors)
    print("Các thể loại khác nhau: ", types)
def print_min_max_pages(books):
    min_page_book = min(books, key=lambda x: x['num_page'])
    max_page_book = max(books, key=lambda x: x['num_page'])
    print("Sách có ít trang nhất: ", min_page_book)
    print("Sách có nhiều trang nhất: ", max_page_book)

def print_authors_with_more_than_two_books(books):
  d = dict()
  for x in books:
    if x['author'] in d:
        d[x['author']] += 1
    else:
        d[x['author']] = 1
  for author, count in d.items():
     if count > 2:
        print(author)
        for x in books:
            if x['author'] == author:
                print(x)
def check_duplicate_codes(books):
    se = set()
    ok = False
    for x in books:
       if x['code'] in se:
         ok = True
         break
    se.add(x['code'])
    if ok:
       print("YES")
    else:
       print("NO")
def sort_and_print_books(books):
    sorted_books = sorted(books, key=lambda x: x['name'])
    print("Danh sách sách sau khi sắp xếp: ", sorted_books)
if __name__ == '__main__':
    books = create_books()
    #b 
    print_authors_and_types(books)
    #c
    print_min_max_pages(books)
    #d
    print_authors_with_more_than_two_books(books)
    #e
    check_duplicate_codes(books)
    #f
    sort_and_print_books(books)