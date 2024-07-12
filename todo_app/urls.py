from django.urls import path
from django.conf.urls import handler404
from .views import RegisterView,TodoListCreateView,TodoDetailView,TokenRefreshAPIView,LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('token/refresh/',TokenRefreshAPIView.as_view(),name='token_refresh'),
    path('todos/',TodoListCreateView.as_view(),name='todos'),
    path('todos/<int:pk>',TodoDetailView.as_view(),name='todo_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

