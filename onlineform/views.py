from django.shortcuts import render
from .form import ClientForm
from django.contrib import messages
from .models import ClientDetails

from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView

# Create your views here.
def onlineform(request):
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your data is saved')        
    return render(request,'onlineform.html',{'form': ClientForm})

def getdetail(request):
    return render(request,'getdetail.html')

def filteredlist(request):
    firstname=request.POST['firstname']
    clients=ClientDetails.objects.filter(full_name__startswith=firstname)   
    if not clients:
        messages.success(request, f'No Client with that first name') 
        return render(request,'getdetail.html',{'clients':clients})
    else:
        return render(request,'filtered_list.html',{'clients':clients})


class ClientListView(ListView):
    model=ClientDetails
    context_object_name ='clients'

class ClientDetailView(DetailView):
    model=ClientDetails
class ClientUpdateView(UpdateView):
    model=ClientDetails
    fields=['full_name','phone_number','client_value','email','website']
   

