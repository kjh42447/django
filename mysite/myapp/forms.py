from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django import forms
from myapp.models import Question, Answer

#질문 등록 클래스
class QuestionForm(forms.ModelForm):
    class Meta:     #모델 폼을 사용하기 위해선 내부 클래스인 Meta 클래스의 정의가 반드시 필요, Meta클래스는 모델과 속성을 표시해야함
        model = Question    #사용할 모델
        fields = ['subject', 'content'] #QuestionForm에서 사용할 Question모델 속성
        
        #폼 위젯
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        
        #폼 레이블
        labels = {
            'subject': '제목',
            'content': '내용',
        }

#답변 등록 클래스
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',
        }