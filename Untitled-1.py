print("===== Library System =====")

print("1- Add Book \n 2- View Books \n 3- Search Book \n 4- Delete Book \n 5- Exit")
print("choose an option:")
v = input()

book_list = [{"title": "Python","author": "Ahmed","year": 2024}]
match v:
    case "Add Book":
        print("Add Book")
        m = input("Enter book title: ")
        n = input("Enter book author: ")
        o = int(input("Enter book year: "))

        book_list.append({"title": m, "author": n, "year": o})
    case "View Books":
        print("View Books")
        num = 1 
        while num <= len(book_list):
            print(f"{num}- Title: {book_list[num-1]['title']}, Author: {book_list[num-1]['author']}, Year: {book_list[num-1]['year']}")
            num += 1
        if len(book_list) == 0:
            print("No books available.")
    case "Search Book":
        print("Search Book")
        search_title = input("Enter book title to search: ")
        found_books = [book for book in book_list if book['title'].lower() == search_title.lower()]
        if found_books:
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
        else:
            print("Book not found.")
    case "Delete Book":
        print("Delete Book")
        delete_title = input("Enter book title to delete: ")
        initial_length = len(book_list)
        book_list = [book for book in book_list if book['title'].lower() != delete_title.lower()]
        if len(book_list) < initial_length:
            print(f"Book '{delete_title}' deleted successfully.")
        else:
            print("Book not found.")
    case "Exit":
        print("Exiting the program.")
    case "Count Books":
        print(f"Total books in the library: {len(book_list)}")
