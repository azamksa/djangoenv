from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example route
    path('<int:bookId>', views.viewbook)

]
