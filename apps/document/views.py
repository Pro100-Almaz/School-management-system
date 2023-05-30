from django.shortcuts import render, redirect
<<<<<<< HEAD
from .forms import DocumentForm, InstructorForm
from .models import Document, Instractor
=======
from .forms import DocumentForm
from .models import Document
from docx import Document as Doc
from django.core.files.storage import FileSystemStorage
<<<<<<< HEAD
>>>>>>> 580b9f83ec3fd30d0f502201e1016427b395879d
=======
>>>>>>> 580b9f83ec3fd30d0f502201e1016427b395879d


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

def generate_word_document(request, item_id):
    data = Document.objects.get(id = item_id)

    doc = Doc()

    doc.add_paragraph("Your data goes here")

    file_name = "example.docx"
    file_path = f"media/{file_name}"

    fs = FileSystemStorage()
    with fs.open(file_path, "wb") as file:
        doc.save(file)

    # Save the document
    return file_path
    
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