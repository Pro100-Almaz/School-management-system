from django.shortcuts import render, redirect
from .forms import DocumentForm, InstructorForm
from .models import Document, Instractor, File
from docx import Document as Doc
from django.core.files.storage import FileSystemStorage

def create_document(request):
    if request.method == 'POST':
        form  = DocumentForm(request.POST)
        form_name = request.POST['form_name']

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
    
    for document in documents:
        print(document.id)

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

def view_document(request, id):
    schedule = {
        1 : ["Introduction"],
        2 : ["Identifying Your Opportunity"],
        3 : ["Developing Your Value Proposition"],
        4 : ["Identifying Your Customers"],
        5 : ["Understanding Your Environment"],
        6 : ["Developing Your Business Model"],
        7 : ["Other Concepts: Social Entrepreneurship; People and Financial Resources; Intellectual Property"],
        8 : ["Introduction to Accounting and Finance"],
        9 : ["Preparation of Financial Statements"],
        10 : ["Introduction to Financial Statement Analysis"],
        11 : ["The Corporation and Financial Markets"],
        12 : ["The Time Value of Money"],
        13 : ["Investment Decision Rules"],
        14 : ["Fundamentals of Capital Budgeting"],
        15 : ["Preparation and Submission of Final Group Project Written Components"],
        16 : ["Final Group Project Pitch Presentations in Recitation Slots"],
    }


    data = Document.objects.get(id = id)
    files = File.objects.all()
    print(files)

    fs = FileSystemStorage()

    doc = Doc(fs.open("template.docx"))

    for paragraph in doc.paragraphs:
        if 'Course_Title' in paragraph.text:
            paragraph.text = paragraph.text.replace('Course_Title', data.course_name)
            paragraph.style = 'Heading 1'
        if 'Instructor_Name' in paragraph.text:
            paragraph.text = paragraph.text.replace('Instructor_Name', str(data.instructors))
        if 'Description_Text' in paragraph.text:
            paragraph.text = paragraph.text.replace('Description_Text', data.description)
        if 'Learning_Outcomes' in paragraph.text:
            paragraph.text = paragraph.text.replace('Learning_Outcomes', data.learning_outcomes)
        if 'Learning_Format' in paragraph.text:
            paragraph.text = paragraph.text.replace('Learning_Format', data.education_format)
        if 'Lecture_Class' in paragraph.text:
            paragraph.text = paragraph.text.replace('Lecture_Class', data.lecture_class)
        if 'Lab_Class' in paragraph.text:
            paragraph.text = paragraph.text.replace('Lab_Class', data.labaratory_class)
        if 'Year_Education' in paragraph.text:
            paragraph.text = paragraph.text.replace('Year_Education', str(data.year_enrollment))
        if 'Prerequisite_HAS' in paragraph.text:
            paragraph.text = paragraph.text.replace('Prerequisite_HAS', str(data.prerequisites))
        if 'Prerequisite_FOR' in paragraph.text:
            paragraph.text = paragraph.text.replace('Prerequisite_FOR', str(data.prerec_for))
        
    
    file_name = "syllabus.docx"
    file_path = f"{file_name}"

    fs = FileSystemStorage()
    with fs.open(file_path, "wb") as file:
        doc.save(file)

    return render(request, 'document_view.html', {"file_path": file_path, "data": data})
