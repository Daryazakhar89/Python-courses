from django.urls import path
from my_site.views import main, photo

urlpatterns = [
    path('', main),
    path('photo', photo),
]
