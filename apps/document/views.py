from django.shortcuts import render, redirect
from .forms import DocumentForm, InstructorForm
from .models import Document, Instractor


def create_document(request):
    if request.method == 'POST':
        form  = DocumentForm(request.POST)
        form_name = request.POST['form_name']
        print("THIS IS FORM NAME: ", form_name)

        if form.is_valid(): 
            form.save()
            
            return render(request, 'success.html', {'form_name': form_name})
        
    else:
        form = DocumentForm()

    return render(request, 'document_form.html', {'forms': form})

def success_document(request):
    if request.method == 'GET':
        form = DocumentForm()
        
        return render(request, 'success.html', {'form': form})

    
def list_document(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        
    return render(request, 'document_list.html', {'documents': documents})

def instructor_list(request):
    if request.method == 'GET':
        instructors = Instractor.objects.all()
        
    return render(request, 'instructor_list.html', {'instructors': instructors})


def instructor_create(request):
    if request.method == 'POST':
        form  = InstructorForm(request.POST)

        if form.is_valid(): 
            form.save()
            return render(request, 'success.html')
        
    else:
        form = InstructorForm()

    return render(request, 'instructor_create.html', {'forms': form})