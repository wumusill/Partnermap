from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

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
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1']
            )
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'join_error.html')
    else: 
        return render(request, 'join.html')