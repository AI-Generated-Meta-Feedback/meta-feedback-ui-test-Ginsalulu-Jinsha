def a_comes_before_b(book_a, book_b):

    shelf_a, order_a = book_a
    shelf_b, order_b = book_b

    if shelf_a < shelf_b:
        return True
   
    if shelf_a == shelf_b and order_a < order_b:
        return True
        
    return False

def insertion_sort_books(books):

    n = len(books)
    
    for i in range(1, n):
        key = books[i]  # Current book to insert
        j = i - 1       # Start comparing with the element just before 'key'
        
        while j >= 0 and not a_comes_before_b(key, books[j]):
            # Shift the element to the right
            books[j + 1] = books[j]
            j -= 1
        
        # Insert the key into its correct sorted position
        books[j + 1] = key
        
    return books
