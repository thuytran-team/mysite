from django.urls import path
from .views import Clothings, Home, Contact, Newsdate, Register,addUser,modalForm,addModalForm
urlpatterns = [
    path('', Home, name='Home'),
    path('clothings/', Clothings, name='Clothings'),
    path('contact/', Contact, name='Contact'),
    path('newsdate/<int:year>', Newsdate, name='Newsdate'),
    path('signup/', Register, name='SignUp'),
    path('addUser/', addUser, name='addUser'),
    path('modalForm/', modalForm, name='modalForm'),
    path('addModelForm/', addModalForm, name='addForm'),

]
