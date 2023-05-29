from django.shortcuts import render, redirect
from .forms import DocumentForm


def create_document(request):
    if request.method == 'POST':
        form  = DocumentForm(request.POST)

        if form.is_valid(): 
            form.save()
            return render(request, 'success.html')
        
    else:
        form = DocumentForm()
    
    return render(request, 'document_form.html', {'form': form})

def success_document(request):
    if request.method == 'GET':
        form = DocumentForm()
        return render(request, 'success.html', {'form': form})
    
