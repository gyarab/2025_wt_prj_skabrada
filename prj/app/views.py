from django.shortcuts import render


def api_playground(request):
    return render(request, "api_playground.html")