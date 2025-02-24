from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register/', views.register, name="register"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('userlogout/', views.logout, name="userlogout"),
    path('create_record/', views.create_record, name="create_record"),
    path('update_record/<int:pk>/', views.update_record, name="update_record"),
    path('delete_record/<int:pk>/', views.delete_record, name="delete_record"),
    path('view_record/<int:pk>/', views.view_record, name="view_record"),
    path("chatbot/", views.chatbot, name="chatbot"),
]