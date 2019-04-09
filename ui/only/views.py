from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import signForm
from .models import Reading
import csv, io


# Create your views here.

def home(request):
    return render(request, 'only/prof.html')




def sign_create_view(request):
    form1 = signForm(request.POST)
    if form1.is_valid():
        form1.save()
        return redirect('login')
    else:
        form1 = signForm()
    # context = {'form' : form}
    return render(request,"only/sign_create.html", {'form1':form1})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. Please provide the following information.')
            return redirect('sign')
    else:
        form = UserCreationForm()
    return render(request, 'only/register.html', {'form':form})




def csv_upload(request):
    template = "only/csv_upload.html"

    prompt = {
        'order': 'Order of the CSV file should be Intensity > Sodium Level'
    }

    if request.method == "GET":
        return render(request, template, prompt)
        # return redirect('processing')

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please select a CSV file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Reading.objects.update_or_create(
            intensity = column[0],
            level = column[1]
        )

    context = {}
    return render(request, template, context)




def processing(request):
    return render(request, 'only/processing.html')
