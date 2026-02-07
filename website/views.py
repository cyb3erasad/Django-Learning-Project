from django.shortcuts import render
from . models import ChaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'website/home.html', {'chais': chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'website/description.html', {'chai': chai})