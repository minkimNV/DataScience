'''
1. n = the number of books
2. the N number of book titles (bestseller)
3. the most bestseller > alphabet order
'''
import sys
input = sys.stdin.readline
    
n = int(input())

books = {}
for book in range(n):
    book = input().strip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1
sortedbooks = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(sortedbooks[0][0])
