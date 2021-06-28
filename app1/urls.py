from django.urls import path
from . import views

urlpatterns = [
    path('create', views.make_short_url, name='make_short_url'),
    path('s/<str:short_url>', views.redirect_to_url, name='redirect_to_url')
]
