#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm


def test(request):
    return render(request, 'qa/base.html', {
        'test': HttpResponse('test'),
    })


def cook(request):
    for met in request.COOKIES:
        print('{} - {}'.format(met, request.COOKIES.get(met)))


def single_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    if request.method == "POST":
        form = AnswerForm(request.POST, initial={'question': pk})
        if form.is_valid():
            form._user = request.user
            form.save()
        else:
            return HttpResponse('200')
        answers = question.answer_set.all()
        url = question.get_url()
        return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': pk})
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })


def paginator_list(request, questions):
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def popular_questions(request):
    questions = Question.objects.popular()
    page = paginator_list(request, questions)
    return render(request, 'qa/list.html', {
        'questions': page.object_list,
    })


def new_questions(request):
    questions = Question.objects.new()
    page = paginator_list(request, questions)
    cook(request)
    return render(request, 'qa/list.html', {
        'questions': page.object_list,
    })


def add_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
        return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {
        'form': form
    })


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/login.html')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/signup.html')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {
        'form': form
    })

# def add_random_question():
#     last = Question.objects.count()
#     title = 'question_{}'.format(last+1)
#     text = 'text question_{} ?'.format(last+1)
#     q = Question(title=title, text=text)
#     q.save()

# def list_questions(request, *args, **kwargs):
#     if request.GET.get('rand'):
#         add_random_question()
#     print(request.GET)
#     questions = Question.objects.new()
#     limit = request.GET.get('limit', 10)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(questions, limit)
#     paginator.baseurl = '/?page='
#     page = paginator.page(page)
#     return render(request, 'qa/list.html',{
#         'questions': page.object_list,
#         'paginator': paginator,
#         'page': page,
#     })

# def decor(func):
#     print('krasota')
#     func()
#     print('lepota')
#     return func
#
# def mego_decor(funci):
#     print('OGO')
#     funci()
#     print('NICHOSI')
#     return funci
#
# #@mego_decor
# #@decor
# def simple():
#     print('nu prosto')
#     return
