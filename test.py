def a_comes_before_b(a, b):
    """Returns True if book 'a' precedes 'b'."""
    # Primary sort: shelfNumber (a[0])
    if a[0] < b[0]:
        return True
    
    # Secondary sort: returnOrder (a[1]), for stability
    if a[0] == b[0] and a[1] < b[1]:
        return True
        
    return False

def insertion_sort_books(books):
    """Sorts books in-place using Insertion Sort."""
    n = len(books)
    
    for i in range(1, n):
        key = books[i]
        j = i - 1
        
        # Shift elements greater than 'key' to the right
        while j >= 0 and not a_comes_before_b(key, books[j]):
            books[j + 1] = books[j]
            j -= 1
        
        books[j + 1] = key
        
    return books

# --- Example Usage ---

# Input: [(Shelf, Order), ...]
test_input = [
    (5, 3),  
    (2, 1),  
    (5, 2),  
    (5, 1)   
]

# print("Input:", test_input)
# sorted_books = insertion_sort_books(test_input)
# print("Output:", sorted_books)
# Expected: [(2, 1), (5, 1), (5, 2), (5, 3)]

