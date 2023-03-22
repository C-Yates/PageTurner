from django.urls import path
# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('bookList/', views.book_list, name='book_list'),
    path('<int:book_id>/book_detail/', views.book_detail, name='book_detail'),
    path('<int:book_id>/rate/', views.new_rating, name='new_rating'),
    path('topBooks/', views.top_books, name='top_books'),
]
