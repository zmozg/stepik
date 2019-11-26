from django import forms

from .models import Question, Answer

class AskForm(forms.Form):

    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        data = self.cleaned_data
        return data

    def clean_question(self):
        question = self.cleaned_data['question']
        return question

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        data = self.cleaned_data
        return data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
