from django.shortcuts import render,HttpResponse
import text2emotion as te

# Create your views here.
def index(request):
    return render(request, 'hello.html')
def about(request):
    if request.method == 'POST':
        inp1 = request.POST['inp1']
        if inp1 != '':
            val1 = te.get_emotion(inp1)
        print(val1)
    return render(request, 'predicted.html', {'val1': val1})