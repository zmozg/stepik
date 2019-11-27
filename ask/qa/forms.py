from django import forms
from django.shortcuts import get_object_or_404

from .models import Question, Answer

class AskForm(forms.Form):

    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        data = self.cleaned_data
        return data

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

    def clean_text(self):
        print('clean_text')
        text = self.cleaned_data['text']
        if text == None or text.strip() == '':
            raise forms.ValidationError
        return text

    def clean_title(self):
        print('clean_title', self.cleaned_data)
        title = self.cleaned_data['title']
        if title == None or text.strip() == '':
            raise forms.ValidationError
        return title


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)#, initial="Put youre answer here...")
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        print('clean')
        data = self.cleaned_data
        return data

    def clean_text(self):
        print('clean_t')
        text = self.cleaned_data['text']
        if text == None or text.strip() == '':
            raise forms.ValidationError
        return text

    def clean_question(self):
        print('clean_q')
        question = self.cleaned_data['question']
        if question == None:
            raise forms.ValidationError('net ego')
        try:
            question = Question.objects.get(pk=question)
        except Question.DoesNotExist:
            raise forms.ValidationError("Question does not exist")
        return question

    def save(self):
        print('save')
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
