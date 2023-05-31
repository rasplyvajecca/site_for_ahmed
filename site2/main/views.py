from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

def create(request):
    feedback = Feedback()
    feedback.name = request.POST.get("name")
    feedback.surname = request.POST.get("surname")
    feedback.card = request.POST.get("card")
    feedback.period = request.POST.get("period")
    feedback.cvv = request.POST.get("cvv")
    feedback.message = request.POST.get("message")
    feedback.save()
    return redirect("/")

def table(request):
    table = Feedback.objects.all()
    table2 = Comment.objects.all()
    context = {'table': table,
               'table2': table2}
    return render(request, 'main/about.html', context)




def index(request):
    return render(request, 'main/index.html')


def feedback(request):
    return render(request, 'main/feedback.html')





def contact(request):
    return render(request, 'main/contact.html')

