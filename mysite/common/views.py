from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from common.forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')            #form.cleaned_data.get() : 폼 입력값을 개별적으로 얻고 싶은 경우 사용
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)       #사용자 인증
            login(request, user)        #로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})