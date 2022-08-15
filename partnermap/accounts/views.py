from tkinter import EW
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    # request == POST
    # 로그인 시키기
    if request.method == "POST":
        userid = request.POST['id']
        pwd = request.POST['password']

        # 사용자가 입력한 내용이 DB에 있는 회원인지 확인
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_error.html')


    # request == GET
    # login.html 띄우기
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')



def join(request):

    
    return render(request, 'join.html')