from importlib.resources import contents
from django.db import models

# Create your models here.
from django.contrib.auth.models import User     

#Question모델
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')      #related_name='author_question' : User모델에서 접근할 때 지정할 인수를 'author_question'로 정의
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)       #modify : 수정
    voter = models.ManyToManyField(User, related_name='voter_question')        #추천인
    
    #id값 대신 제목 표시
    def __str__(self):
        return self.subject
    
#Answer 모델
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #on_delete=models.CASCADE : 질문이 삭제되면 답변도 같이 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')