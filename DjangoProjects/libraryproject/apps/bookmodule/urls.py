from django.urls import path
from . import views

#app_name = 'bookmodule'

urlpatterns = [
    #path('', views.index, name='index'),  # Example route
    #path('<int:bookId>', views.viewbook),
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name='books.aboutus'),
    #path('html5/links', views.links, name="html5.links"),
    #path('html5/text/formatting', views.text_formatting, name="html5.text_formatting"),
    #path('html5/listing', views.listing, name="html5.listing"),
    #path('html5/tables', views.tables, name="html5.tables"),
    path('search', views.search, name="search"),


]
