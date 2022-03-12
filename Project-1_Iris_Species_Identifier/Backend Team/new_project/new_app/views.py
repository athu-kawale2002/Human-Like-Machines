from logging import exception
from django.shortcuts import render, redirect
from new_app.MLmodel import makePrediction
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
            if int(inp1)<0 or int(inp2)<0 or int(inp3)<0 or int(inp4)<0:
                raise Exception("exception")
            if int(inp1)>10 or int(inp2)>10 or int(inp3)>10 or int(inp4)>10:
                raise Exception("exception1")
            result = makePrediction(inp1, inp2, inp3, inp4)
        return render(request, 'main.html', {'result': result})
    except:
        if inp1 == '' or inp2 == '' or inp3 == '' or inp4 == '':
            messages.success(
                request, "Fill all the Input Features to Get Prediction. . .")
            return redirect(index)
        if int(inp1)<0 or int(inp2)<0 or int(inp3)<0 or int(inp4)<0:
            messages.success(
                request, "Enter the positive value of the lengths in range 0 to 10. . .")
            return redirect(index)
        if int(inp1)>10 or int(inp2)>10 or int(inp3)>10 or int(inp4)>10:
            messages.success(
                request, "Enter the positive value of the lengths in range 0 to 10. . .")
            return redirect(index)
        if type(inp1) != int or type(inp2) != int or type(inp3) != int or type(inp4) != int:
            messages.success(
                request, "Fill all the Input Features numeric value Only. . .")
            return redirect(index)
