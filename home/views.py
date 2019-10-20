from django.shortcuts import render,redirect
from .models import Feedbacks
from .forms import UserFeedbackForm
from django.contrib.auth.models import User
# Create your views here.

def home_view(request):
    if request.method=='POST':
        form=UserFeedbackForm(request.POST)
        form.instance.author=request.user
        if form.is_valid():
            form.save()
            return redirect('home_view')
    form=UserFeedbackForm()
    if(request.user.is_authenticated):
        usr=User.objects.get(username=request.user)
        fdbks=usr.feedbacks_set.order_by('-date_posted')    
        return render(request,'home/home.html',{'feedbcks':fdbks,'form':form})
    else:
        return render(request,'home/home.html',{'form':form})
    #return render(request,'home/home.html',
    #{'feedbcks':Feedbacks.objects.filter(username=request.user).order_by('-date_posted'),'form':form})

