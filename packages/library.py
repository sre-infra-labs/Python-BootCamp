library = {}

def add_book(book):
    """
    Add a book into library

    Args:
        book (Dictionary): Book with isbn, title, author, pages

    Raises:
        ValueError: [description]
        Exception: [description]

    Returns:
        [type]: [description]
    """
    global library

    if(type(book) != type({})):
        raise ValueError("Invalid value for book properties")

    # If book not existing
    new_book_isbn = book['isbn']
    if (new_book_isbn in library):
        raise Exception("Duplicate entry for book with same isbn")
    else:
        library[new_book_isbn] = book
        return library[new_book_isbn]

def find_book_by_isbn(isbn):
    global library

    if(isbn == None or isbn.strip() == ''):
        raise ValueError('Invalid author name string')

    book = library[isbn]
    if (book == None):
        raise Exception('Book not found with provided isbn')
    else:
        return book

def find_book_by_title(title):
    global library

    if(title == None or title.strip() == ''):
        raise ValueError('Invalid title value provided')

    for book in library.values():
        if (book['title'] == title):
            return book
    else:
        raise Exception("Book not found matching with title")

if __name__ == '__main__':
    print("Add book with isbn '20200312-01'")
    book1 = add_book({'isbn':'20200312-01','title':'Clean code for python','pages':200, 'author':'Krishna'})
    print(f"Book titled '{book1['title']}' added to library")

    isbn = '20200312-01'
    print(f"Find book with isbn '{isbn}'")
    book2 = find_book_by_isbn(isbn)
    print(f"Book titled '{book2['title']}' found with isbn '{isbn}'")

    title = 'Clean code for python1'
    print(f"Find book with title '{title}'")
    book3 = find_book_by_title(title)
    print(f"Book '{title}' by {book3['author']}' found")


