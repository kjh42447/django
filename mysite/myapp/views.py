#가상환경 접속 : E:\backend\django\mysite>mysite.cmd
#가상환경 종료 : deactivate
#주석 단축키 : ctrl + /
import imp
from multiprocessing import context
from venv import create
#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#브라우저 출력
#질문 목록 화면
def index(request):
    page = request.GET.get('page', '1')     #디폴트 페이지 : 1
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)    #10항목씩 출력
    page_obj = paginator.get_page(page)
    context = {"question_list" : page_obj}
    return render(request, "myapp/question_list.html", context)

#질문 상세 내용 화면
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "myapp/question_detail.html", context)

#답변 저장 화면
@login_required(login_url='common:login')       #로그인 했는지 체크
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #POST
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user        #auther 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            #redirect : 페이지 이동 함수
            return redirect('myapp:detail', question_id = question.id)
    #GET
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'myapp/question_detail.html', context)    

#질문 등록 화면
@login_required(login_url='common:login')
def question_create(request):
    #POST : 리소스 생성 및 변경, html body에 담아 전송, 보안, 길이 무제한, 멱등x
    if request.method == 'POST':
        form = QuestionForm(request.POST)   #request.POST : 사용자가 입력한 내용이 담겨있다.
        if form.is_valid():
            question = form.save(commit=False)      #임시저장하여 question객체를 리턴받음
            question.author = request.user          #author계정에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()                         #실제로 저장
            return redirect('myapp:index')
    #GET : 검색, 링크에 추가하여 전송, 보안 취약, 길이 제한, 멱등
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'myapp/question_form.html', context)