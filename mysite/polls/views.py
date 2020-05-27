from django.shortcuts import render
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question,Choice


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))
    #render函数 

# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     output=', '.join( [  q.question_text for q in latest_question_list ]  )
#     return HttpResponse("hello world .You're at the poll index.\r\n"+output)

# def detail(request,question_id):
#     response="you are looking at the question:%s."
#     return HttpResponse(response % question_id)

def detail(request,question_id):
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #或者
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def results(request,question_id):
    # response="you're looking at the result kf question%s"
    # return HttpResponse(response % question_id)

    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question':question})

def vote(request,question_id):
    #https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial04/
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice =question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"you didn't select a choice.",})
    else:
        selected_choice.vote+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))