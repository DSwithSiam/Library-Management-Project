from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('details/<int:id>', DetailsPostView.as_view(), name= 'detail_post'),
    path('borrow/<int:id>', BorrowPost, name= 'borrow'),
    path('pay/<int:id>', ReturnBook, name= 'return_book'),
]

