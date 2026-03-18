from django.shortcuts import render, redirect
# Create your views here.
from .Forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('success')
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form})
