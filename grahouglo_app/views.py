from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.http import HttpResponseRedirect
# Create your views here.




def home(request):

    form = ClientFeedbackForm()
    if request.method == 'POST': 
        form = ClientFeedbackForm(request.POST)
        if form.is_valid(): 
            form.save(commit=True) 
            return redirect('home') 
        else:
             print(form.errors)

    context = {'form': form}

    return render(request, 'grahouglo/home.html', context)