
from django.urls import path
from .views import hello, users_list, new_user, edit_user, delete_user

urlpatterns = [
    path('', hello, name='hello'),
    path('users/', users_list, name='users_list'),
    path('new_user/', new_user, name='new_user'),
    path('edit_user/<int:id>/', edit_user, name='edit_user'),
    path('delete_user/<int:id>/', delete_user, name='delete_user'),
]

