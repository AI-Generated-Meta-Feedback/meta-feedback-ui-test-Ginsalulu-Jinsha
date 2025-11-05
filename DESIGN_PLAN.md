Algorithm choice: insertion sort
Insertion Sort is inherently stable. Stability is critical because books with the same primary key (shelfNumber) must maintain their original relative order determined by the returnOrder. A stable sort ensures that if Book A and Book B are both on shelf 5 and A was returned before B, A will remain before B in the sorted output.
complexity: 
The time complexity for Insertion Sort in the average/worst case is O(n^2)
This outlines the complete solution for the Library Book Return Sorting problem, covering the design, analysis, and testing strategy.
Insertion Sort's best-case time complexity is O(n) when the array is already sorted or nearly sorted. If books are mostly sorted by shelfNumber, the algorithm will perform significantly faster, approaching linear time.
