from django.shortcuts import render


def livro_view(request):
    return render(request, "homeBook.html")


def editora_view(request):
    return render(request, "homePubli.html")
