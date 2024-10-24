from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.files.storage import FileSystemStorage

@ensure_csrf_cookie
def video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(file.name)
            handle_uploaded_file(file)
            return render(request, "video.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'video.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def media_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage(location='media/')
        filename = fs.save(uploaded_file.name, uploaded_file)
        # Now you can use the 'filename' to display the video in your template.
        # ...
        context = {'filename': filename}  # Initialize an empty context dictionary
        # Add any relevant data to the context (e.g., filename, messages, etc.)
        # ...
    return render(request, 'video.html', context)