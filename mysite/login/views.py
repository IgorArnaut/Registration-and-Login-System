from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LoginForm, RegisterForm


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse((template.render()))


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/user/login")
    else:
        form = RegisterForm()

    return render(request, "/user/register.html", { "form": form })


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()

    return render(request, "/user/login.html", { "form": form })