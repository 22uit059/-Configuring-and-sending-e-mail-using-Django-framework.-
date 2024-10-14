from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('send_email/', views.send_email, name='send_email'),  # Send email page
]
