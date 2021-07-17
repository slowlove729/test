from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.
from .models import Question, Answer

admin.site.register(Question)
admin,site.register(Answer)