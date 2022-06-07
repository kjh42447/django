#가상환경 접속 : E:\backend\django\mysite>mysite.cmd
#가상환경 종료 : deactivate
#주석 단축키 : ctrl + /
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

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