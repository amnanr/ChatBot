from django.urls import path
from . import views

urlpatterns = [
    # Route for the chat page (initial view rendering)
    path('', views.index, name='chatpage'),

    # API endpoint for chatbot responses
    path('api/chatbot/', views.chatbot_response, name='chatbot_response'),

    # API endpoint for handling file uploads
    path('api/upload/', views.upload_file, name='upload_file'),
]