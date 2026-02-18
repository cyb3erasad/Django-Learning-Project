from django.shortcuts import render
from . models import ChaiVarity, ChaiStore
from django.shortcuts import get_object_or_404
from . forms import ChaiVarityForm
# Create your views here.

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'website/home.html', {'chais': chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'website/description.html', {'chai': chai})

def chai_store(request):
    if request.method == "POST":
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            store = ChaiStore.objects.filter(chai_varieties=chai_varity)
    else:
        form = ChaiVarityForm()        
    
    return render(request, 'website/chai_store.html', {'store': store, 'form': form})