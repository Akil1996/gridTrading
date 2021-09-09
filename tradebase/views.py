from django.shortcuts import redirect, render
from .models import BrokerDetails


def tradebase_home(request):
    return render(request, "tb/home.html", {})


def user_detials(request):
    if request.method == "POST":
        userName = request.POST["userName"]
        password = request.POST["password"]
        accessToken = request.POST["accessToken"]
        udetails = BrokerDetails(userName = userName, passWord = password, accessToken = accessToken)
        udetails.save()
        redirect('/')
    return render(request, "tb/userdetails.html", {})