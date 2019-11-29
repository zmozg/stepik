from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Question, Answer

class AskForm(forms.Form):

    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        data = self.cleaned_data
        return data

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == None or text.strip() == '':
            raise forms.ValidationError
        return text

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == None or title.strip() == '':
            raise forms.ValidationError
        return title


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)#, initial="Put youre answer here...")
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        data = self.cleaned_data
        return data

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == None or text.strip() == '':
            raise forms.ValidationError
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == None:
            raise forms.ValidationError('net ego')
        try:
            question = Question.objects.get(pk=question)
        except Question.DoesNotExist:
            raise forms.ValidationError("Question does not exist")
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == None or username.strip() == '':
            raise forms.ValidationError("Empty Field")
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Est yge")
        except User.DoesNotExist:
            pass
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == None or password.strip() == '':
            self.empty_password = password
        return make_password(password)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == None or username.strip() == '':
            raise forms.ValidationError("Empty Field")
        
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == None or password.strip() == '':
            raise forms.ValidationError("Empty Field")
        return password.strip()
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Uncorrect user/password")
        if not user.check_password(password):
            raise forms.ValidationError("Uncorrect user/password")


