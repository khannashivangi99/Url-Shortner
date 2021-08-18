from django.shortcuts import render,redirect
from .models import URL
import uuid
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        original_url=request.POST['original_url']
        uid=str(uuid.uuid4())[:5] # reducing the length of uuid to 5
        new_url=URL(original_url=original_url,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def redirecting(request,pk):
    url_details=URL.objects.get(uuid=pk)
    return redirect(url_details.original_url)
    

