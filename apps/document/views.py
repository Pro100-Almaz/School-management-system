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
    
<<<<<<< HEAD
    return render(request, 'document_form.html', {'forms': form})
=======
    return render(request, 'document_form.html', {'form': form})

def success_document(request):
    if request.method == 'GET':
        form = DocumentForm()
        return render(request, 'success.html', {'form': form})
>>>>>>> b31047cc045b87527dcbd7cc679053d0bba3d96e
    
