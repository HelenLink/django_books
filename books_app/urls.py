from . import views
from django.urls import path

urlpatterns = [
    path('', views.menu),
    path('book/<int:pk>', views.one_book, name="book-detail"),
]