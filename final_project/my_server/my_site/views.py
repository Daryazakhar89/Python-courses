from django.shortcuts import render, redirect
from .models import MySite
from .forms import MySiteForms


def main(request):
    return render(request, 'my_site/main.html')


def my_request(request):
    if request.method == 'POST':
        form = MySiteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = MySiteForms()
    return render(request, 'my_site/my_request.html', {'form': form})
