from django import forms
from .models import Question, Answer

class AskForm(forms.ModelForm):
    
    def clean(self):
        data = self.clean_data
        return data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

    class Meta:
        model = Question
        fields = ('title', 'text')

class AnswerForm(forms.ModelForm):
    
    def clean(self):
        data = self.clean_data
        return data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

    class Meta:
        model = Answer
        fields = ('text', 'question')