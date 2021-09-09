from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        userName = request.POST["userName"]
        email = request.POST["email"]
        password = request.POST["password"]
        conformPassword = request.POST["conformPassword"]
        user = User.objects.create_user(username= userName, password= password, email= email, first_name= firstName, last_name= lastName)
        user.save()
        return redirect('/accounts/login/')
    return render(request, "account/register.html", {})

def login(request):
    if request.method == "POST":
        userName = request.POST["userName"]
        password = request.POST["password"]
        user = auth.authenticate(username = userName, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    return render(request, "account/login.html", {})

def logout(request):
    auth.logout(request)
    return redirect('/accounts/login/')