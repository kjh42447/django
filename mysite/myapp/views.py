from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#브라우저에 해당 문자열 출력
def index(request):
    return HttpResponse("안녕하세요 myapp에 오신것을 환영합니다.")