from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.shortcuts import redirect


# Create your views here.
def index(request):
    tasks = List.objects.all()
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def delete(request, pk):
    task = List.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    context = {'task': task}
    return render(request, 'delete.html', context)