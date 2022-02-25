from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('jobs/', views.jobs),
    path('recruiter/', views.recruiter),
    path('aboutus/', views.aboutus),
    path('contactus/', views.contactus),
]
