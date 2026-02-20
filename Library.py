library = []

quantity = int(input("Enter the number of books: "))

for i in range(quantity):
    book = {
        "id": i + 1,
        "title": input("Enter the title of the book: "),
        "author": input("Enter the author of the book: "),
        "pages": int(input("Enter the number of pages: ")),
        "available": input("Is the book available? (yes/no): ").lower() == "yes"
    }
    library.append(book)


print("\nChoose an option:")
print("1 - Remove a book by ID")
print("2 - Search book by title")
print("3 - Show available books")

option = input("Option: ")

if option == "1":
    remove_id = int(input("Enter the ID to remove: "))
    for book in library:
        if book["id"] == remove_id:
            library.remove(book)
            print("Book removed successfully.")
            break
    else:
        print("Book not found.")

elif option == "2":
    search_title = input("Enter the title: ").lower()
    for book in library:
        if book["title"].lower() == search_title:
            print("\nBook found:")
            print(book)
            break
    else:
        print("Book not found.")

elif option == "3":
    print("\nAvailable books:")
    available_books = [book for book in library if book["available"]]

    if available_books:
        for book in available_books:
            print(f"{book['title']} by {book['author']}")
    else:
        print("No available books.")

else:
    print("Invalid option.")



total_pages = sum(book["pages"] for book in library)

print("\nLibrary Catalog:")
for book in library:
    print(book)

print("\nTotal books:", len(library))
print("Total pages:", total_pages)
