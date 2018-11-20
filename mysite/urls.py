from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('Portfolio', views.portfolio, name='portfolio'),
    path('Contact', views.contact, name='contact'),
]
