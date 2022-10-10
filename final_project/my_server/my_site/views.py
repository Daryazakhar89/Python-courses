from django.shortcuts import render


def main(request):
    return render(request, 'my_site/main.html')


def my_request(request):
    return render(request, 'my_site/my_request.html')
