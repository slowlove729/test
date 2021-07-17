from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question, Answer

# 현재 막힌 부분 index.html으로 보낸 context를 처리하지 못함
# https://docs.djangoproject.com/ko/3.2/intro/tutorial03/
# 뷰가 실제로 뭔가를 하도록 만들기
def index(request):
    # latest_question_list = Question.objects.all() #전체
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #최근 5개
    # print(latest_question_list)
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
        
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    answer_list = Answer.objects.filter(question_id = question_id)
    print(answer_list)
    context = {
        'question': question,
        'answer_list': answer_list, 
    }
    return render(request, 'polls/detail.html', context)
    
    
def results(request, question_id):
    return HttpResponse(
        f"You're looking at the results of question {question_id}."
    )
    
def vote(request, question_id):
    return HttpResponse(
        f"You're voting on question {question_id}."
    )