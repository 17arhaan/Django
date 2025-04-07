from django.urls import path
from . import views

app_name = 'Hostel_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]
