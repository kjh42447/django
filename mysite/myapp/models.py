from importlib.resources import contents
from django.db import models

# Create your models here.
from django.contrib.auth.models import User     

#Question모델
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    #id값 대신 제목 표시
    def __str__(self):
        return self.subject
    
#Answer 모델
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #on_delete=models.CASCADE : 질문이 삭제되면 답변도 같이 삭제
    content = models.TextField()
    create_date = models.DateTimeField()