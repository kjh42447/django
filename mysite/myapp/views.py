#가상환경 접속 : E:\backend\django\mysite>mysite.cmd
#가상환경 종료 : deactivate
from multiprocessing import context
from venv import create
#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

#브라우저 출력
#질문 목록 화면
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {"question_list" : question_list}
    return render(request, "myapp/question_list.html", context)

#질문 상세 내용 화면
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "myapp/question_detail.html", context)

#답변 저장 화면
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content = request.POST.get('content'), create_date = timezone.now())
    #redirect : 페이지 이동 함수
    return redirect('myapp:detail', question_id = question.id)