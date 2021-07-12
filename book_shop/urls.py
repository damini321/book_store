from django.urls import path
from . import views

urlpatterns = [
    path('book_detail', views.createbook),
    path('get_data', views.Bookinfo),
]
