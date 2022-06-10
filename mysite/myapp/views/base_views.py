#가상환경 접속 : E:\backend\django\mysite>mysite.cmd
#가상환경 종료 : deactivate
#주석 단축키 : ctrl + /
#admin / 1111
#user2 / passworduser2!
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

#질문 목록 화면
def index(request):
    page = request.GET.get('page', '1')     #디폴트 페이지 : 1
    kw = request.GET.get('kw', '')      #검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |      #제목
            Q(content__icontains=kw) |      #내용
            Q(answer__content__icontains=kw) |      #답변 내용
            Q(author__username__icontains=kw) |     #질문 글쓴이
            Q(answer__author__username__icontains=kw)       #답변 글쓴이
        ).distinct()
    paginator = Paginator(question_list, 10)    #10항목씩 출력
    page_obj = paginator.get_page(page)
    context = {"question_list" : page_obj}
    return render(request, "myapp/question_list.html", context)

#질문 상세 내용 화면
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "myapp/question_detail.html", context)