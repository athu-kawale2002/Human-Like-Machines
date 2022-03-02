from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Form
from .MLmodel import makePrediction
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def prediction(request):
    try:
        if request.method == 'POST':
            inp1 = request.POST['inp1']
            inp2 = request.POST['inp2']
            inp3 = request.POST['inp3']
            inp4 = request.POST['inp4']
            result = makePrediction(inp1, inp2, inp3, inp4)
            form = Form(inp1=inp1, inp2=inp2, inp3=inp3, inp4= inp4)
            form.save()        
        
        return render(request, 'main.html', {'result':result})
    except:
        if inp1=='' or inp2=='' or inp3=='' or inp4=='':
            messages.success(request, "Fill all the Input Features to Get Prediction. . .")
            return redirect(index)
        if type(inp1)!=int or type(inp2)!=int or type(inp3)!=int or type(inp4)!=int: 
            messages.success(request, "Fill all the Input Features String Only. . .")
            return redirect(index)