from multiprocessing import context
#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
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