from django.urls import path
from my_site.views import main, my_request

urlpatterns = [
    path('', main),
    path('my_request', my_request),
]
