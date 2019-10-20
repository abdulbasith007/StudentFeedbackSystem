from django.shortcuts import render,redirect
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    form=UserRegisterForm()
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'users/register.html',{'form':form})