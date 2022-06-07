from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Question
from ..forms import QuestionForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

#브라우저 출력


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

#질문 수정 화면
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('myapp:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('myapp:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'myapp/question_form.html', context)

#질문 삭제 회면
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(request, question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('myapp:detail', question_id=question.id)
    question.delete()
    return redirect('myapp:index')