from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from docx import Document as Doc
from django.core.files.storage import FileSystemStorage


def create_document(request):
    if request.method == 'POST':
        form  = DocumentForm(request.POST)

        if form.is_valid(): 
            form.save()
            return render(request, 'success.html')
        
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
    
