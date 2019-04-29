from django.shortcuts import render, redirect, reverse, HttpResponse
from MyGit01 import models
from MyGit01.forms import RegForm
import hashlib


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        password = md5.hexdigest()

        user_obj = models.UserProfile.objects.filter(username=username, password=password, is_active=True).first()

        if user_obj:
            request.session["pk"] = user_obj.pk

            return redirect(reverse("customer_list"))
        else:
            return render(request, "login.html", {"error": "用户名密码错误!"})

    return render(request, "login.html")


def reg(requset):
    if requset.method == "POST":
        form_obj = RegForm(requset.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse("login"))

    else:
        form_obj = RegForm()

    return render(requset, "reg.html", {"form_obj": form_obj})
