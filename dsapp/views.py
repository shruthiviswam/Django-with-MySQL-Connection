from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    return HttpResponse ('Hello World')

def modelform(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data is saved to the Database!')
        # else:
        #     return HttpResponse(forms.errors)
    return render(request, 'dsapp/model.html', {'form': form})