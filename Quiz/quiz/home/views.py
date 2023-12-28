from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *
import random
import json
# Create your views here.

def home(request):
    return HttpResponse("Hello from django")

def get_quiz(request):
    question_objs = list(Question.objects.all())
    data = []
    for question_obj in question_objs:
        data.append({
            "category" : question_obj.category.category_name,
            "question" : question_obj.question,
            "marks" : question_obj.marks, 
            "answers" : question_obj.get_answers()
        })
    payload = {'status' : True , 'data' : data}
    return JsonResponse(payload)   
