from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Question,Choice
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('id')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
        question = get_object_or_404(Question, id=question_id)
        context = {
            'question':question
        }
        return render(request, 'polls/detail.html', context)



def vote(request,question_id):
    question = get_object_or_404(Question,id=question_id)

    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        context = {'question':question,'error_message':'You did not select a choice',}
        return render(request,'polls.detail',context)
    else:
        selected_choice.votes +=1;
        selected_choice.save();
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': question})
