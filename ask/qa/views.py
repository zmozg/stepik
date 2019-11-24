#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from django.core.paginator import Paginator

def test(request):
    return render(request, 'qa/base.html',{
        'test': HttpResponse('test'),
    })


def add_random_question():
    last = Question.objects.count()
    title = 'question_{}'.format(last+1)
    text = 'text question_{} ?'.format(last+1)
    q = Question(title=title, text=text)
    q.save()

def single_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()

    return render(request, 'qa/question.html',{
        'question': question,
        'answers': answers,
    })

def list_questions(request, *args, **kwargs):
    if request.GET.get('rand'):
        add_random_question()
    print(request.GET)
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/list.html',{
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def decor(func):
    print('krasota')
    func()
    print('lepota')
    return func

def mego_decor(funci):
    print('OGO')
    funci()
    print('NICHOSI')
    return funci

#@mego_decor
#@decor
def simple():
    print('nu prosto')
    return
