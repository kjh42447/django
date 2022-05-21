(mysite) E:\backend\django\mysite>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

(mysite) E:\backend\django\mysite>python manage.py makemigrations
Migrations for 'myapp':
  myapp\migrations\0001_initial.py
    - Create model Question
    - Create model Answer

(mysite) E:\backend\django\mysite>python manage.py sqlmigrate myapp 0001
BEGIN;
--
-- Create model Question
--
CREATE TABLE "myapp_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subject" varchar(200) NOT NULL, "content" text NOT NULL, "create_date" datetime NOT NULL);
--
-- Create model Answer
--
CREATE TABLE "myapp_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "create_date" datetime NOT NULL, "question_id" bigint NOT NULL REFERENCES "myapp_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "myapp_answer_question_id_a8132dbf" ON "myapp_answer" ("question_id");
COMMIT;

(mysite) E:\backend\django\mysite>python manage.py migrate              
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions
Running migrations:
  Applying myapp.0001_initial... OK

(mysite) E:\backend\django\mysite>python manage.py shell  
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from myapp.models import Question, Answer
>>> from django.utils import timezone
>>> q = Question(subject="myapp테스트", content="myapp에 대해 알고싶습니다.", create_date=timezone.now())
>>> q.save()
>>> q.id
1
>>> q = Question(subject="장고 모델 질문입니다.", content="id는 자동으로 생성되나요?", create_date=timezone.now())  
>>> q.save()
>>> q.id     
2
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
>>>
KeyboardInterrupt
>>> ^Z

now exiting InteractiveConsole...

(mysite) E:\backend\django\mysite>python manage.py shell
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from myapp.models import Question, Answer
>>> Question.objects.all()
<QuerySet [<Question: myapp테스트>, <Question: 장고 모델 질문입니다.>]>
>>> Question.objects.filter(id=1)
<QuerySet [<Question: myapp테스트>]>
>>> Question.objects.filter(subject__contains="장고") 
<QuerySet [<Question: 장고 모델 질문입니다.>]>
>>> q = Question.objects.get(id=1)
>>> q
<Question: myapp테스트>
>>> q.subject = "myapp test"
>>> q.save()
>>> q
<Question: myapp test>
>>> q.delete()
(1, {'myapp.Question': 1})
>>> Question.objects.all()
<QuerySet [<Question: 장고 모델 질문입니다.>]>
>>> q = Question.objects.get(id=2) 
>>> from django.utils import timezone
>>> a = Answer(question = q, content = "네 자동으로 생성됩니다.", create_date = timezone.now())
>>> a.save()
>>> a.id
1
>>> a
<Answer: Answer object (1)>
>>> a.question
<Question: 장고 모델 질문입니다.>
>>> q.answer_set.all()
<QuerySet [<Answer: Answer object (1)>]>