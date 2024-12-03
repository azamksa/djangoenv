from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
 #name = request.GET.get("name") or "world!"
 #return render(request, "bookmodule/index.html" , {"name": name})

#def index(request):
 #return HttpResponse("Index page is working!")


#def index2(request, val1 = 0): #add the view function (index2)
 #return HttpResponse("value1 = "+str(val1))

#def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
# book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 #book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 #targetBook = None
 #if book1['id'] == bookId: targetBook = book1
 #if book2['id'] == bookId: targetBook = book2
 #context = {'book':targetBook} # book is the variable name accessible by the template
 #return render(request, 'bookmodule/show.html', context)

def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

from django.shortcuts import render

def links(request):
    return render(request, 'bookmodule/links.html')

def text_formatting(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')



# Mock function to get a list of books
def __getBooksList():
    books = [
        {'id': 1, 'title': 'Red Book', 'author': 'Ahmad'},
        {'id': 2, 'title': 'Black Book', 'author': 'ali'},
        {'id': 3, 'title': 'Blue Book', 'author': 'omar'},
    ]
    print("Books:", books)
    return books


def search(request):
    books = []
    if request.method == "POST":
        print("POST data:", request.POST)
        keyword = request.POST.get('keyword', '').lower()
        is_title = request.POST.get('option1')
        is_author = request.POST.get('option2')

        # Ensure you're getting valid input from the form
        print("Keyword:", keyword, "Search Title:", is_title, "Search Author:", is_author)

        all_books = __getBooksList()
        for book in all_books:
            if (is_title and keyword in book['title'].lower()) or \
               (is_author and keyword in book['author'].lower()):
                books.append(book)
    return render(request, 'bookmodule/search.html', {'books': books})

def book_detail(request, book_id):
    # Example: Simulating a database or data source
    books = [
        {'id': 1, 'title': 'Book One', 'author': 'Author One'},
        {'id': 2, 'title': 'Book Two', 'author': 'Author Two'},
    ]

    # Find the book with the given ID
    book = next((book for book in books if book['id'] == book_id), None)

    if book is None:
        return render(request, 'bookmodule/not_found.html', {'book_id': book_id})

    return render(request, 'bookmodule/book_detail.html', {'book': book})


#def home(request):
 #return render(request, 'home.html')
