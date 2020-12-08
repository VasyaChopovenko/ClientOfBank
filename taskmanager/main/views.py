from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            card_number = userform.cleaned_data["cardNumber"]
            password = userform.cleaned_data["password"]
            return HttpResponse("<h2>Пароль ({1}) для карти № {0}</h2>".format(card_number, password))
        else:
            return HttpResponse("Неправильні дані")
    else:
        userform = UserForm()
        return render(request, "main/index.html", {"form": userform})
