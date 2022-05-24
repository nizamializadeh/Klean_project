from django.shortcuts import render

# Create your views here.
def index(request):
    todo_list = "aas"
    return render(request,"index.html",{'todo_list':todo_list})