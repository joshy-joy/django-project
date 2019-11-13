from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib
from django.http import JsonResponse

def home(request):

    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('UTF-8')).hexdigest()
            try:
                Hash.objects.get(hash = text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash', hash = text_hash)

    form = HashForm()
    return render(request, 'home.html',{'form':form})

def hash (request, hash):

    hash = Hash.objects.get(hash = hash)
    return render(request, 'hash.html', {'hash':hash})

def quickhash(request):

    text = request.get['text']
    return JsonResponse({'hash': hashlib.sha256(text.encode('UTF-8')).hexdigest() })