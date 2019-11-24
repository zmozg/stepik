from django.contrib import admin
from qa.models import Question, Answer

#class QuestionAdmin(admin.ModelAdmin):
#    class Meta:
        #model = Question

admin.site.register(Question)
admin.site.register(Answer)
