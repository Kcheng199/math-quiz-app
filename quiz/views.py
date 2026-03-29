# Generates random numbers for quiz questions
# Handles quiz question generation
import random
from django.shortcuts import render

def quiz_view(request):

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    context = {
        "num1": num1,
        "num2": num2
    }

    return render(request, "quiz.html", context)