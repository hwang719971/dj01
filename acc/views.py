from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.

def chpass(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect('acc:login')
    else:
        pass
    return redirect('acc:update')

def delete(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect('acc:login')
    return redirect('acc:profile')

def update(request):
    if request.method == "POST":
        u = request.user
        um = request. POST.get("umail")
        uc = request.POST.get("ucom")
        pic = request.FILES.get("upic")
        if pic:
            u.pic.delete()
            u.pic = pic
        u.email, u.comment = um, uc
        u.save()
        return redirect('acc:profile')
    return render(request, 'acc/update.html')

def profile(request):
    return render(request, 'acc/profile.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('acc:index')
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        ua = request.POST.get("uage")
        uc = request.POST.get("ucom")
        pic = request.FILES.get("upic")
        
        try:
            User.objects.create_user(username=un, password=up, age=ua, comment=uc, pic=pic)
            return redirect('acc:login')
        except:
            pass
    return render(request, 'acc/signup.html')

def ulogout(request):
    logout(request)
    return redirect('acc:index')

def ulogin(request):
    if request.user.is_authenticated:
        return redirect('acc:index')
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username = un, password = up)
        if u:
            login(request, u)
            messages.success(request, f" {u} 님 환영합니다.")
            return redirect('acc:index')
        else:
            messages.info(request, "계정 정보가 일치하지 않습니다.")
    return render(request, 'acc/login.html')

def index(request):
    return render(request, 'acc/index.html')