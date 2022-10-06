from django.shortcuts import render


def main(request):
    return render(request, 'my_site/main.html')


def photo(request):
    return render(request, 'my_site/photo.html')
