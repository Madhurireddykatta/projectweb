from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='user_logout'),
    path('upload/', upload_file, name='user_upload'),
    path('sentfile/', sent_files, name='sentfile'),
    path('recievedfile/', recieved_files, name='recieved_files'),
    path('recievedfile/<filename>', download_file, name='download_file'),
]
