import packages.library as lib

print(f"\nAdd book with isbn '20200312-01'")
book1 = lib.add_book({'isbn':'20200312-01','title':'Clean code for python','pages':200, 'author':'Krishna'})
print(f"Book titled '{book1['title']}' added to library")

isbn = '20200312-01'
print(f"\nFind book with isbn '{isbn}'")
book2 = lib.find_book_by_isbn(isbn)
print(f"Book titled '{book2['title']}' found with isbn '{isbn}'")

title = 'Clean code for python'
print(f"\nFind book with title '{title}'")
book3 = lib.find_book_by_title(title)
print(f"Book '{title}' by '{book3['author']}' found")


"""
Refactor the book cat application
by adding search_by_criteria function
which accepts any lambda
And also use logging decorator with annotation
"""