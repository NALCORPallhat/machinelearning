from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .machine_learning import create_pdf, parse_text_file

def hello_world(request):
    return render(request, 'index.html')


def machine_view(request):
    PDF_FILE = create_pdf()
    with open(PDF_FILE, 'rb') as pdf:
        pdf_stream = pdf.read()
        response = HttpResponse(pdf_stream, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=gehalts_abrechnung.pdf'
        return response


@csrf_exempt
def display_machine(request):
    if request.method == 'POST' and request.FILES['machinelearningfile']:
        myfile = request.FILES['machinelearningfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        return HttpResponse(parse_text_file(filename))
    return render(request, 'index.html')
