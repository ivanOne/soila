from django.shortcuts import render_to_response
from .models import worker,machine, prise
# Create your views here.
def index(request):

    return render_to_response('index.html')


def company(request):

    return render_to_response('company.html')

def machine_list(request):

    machines = machine.objects.all()
    return render_to_response('machine.html',{'machines':machines})


def worker_list (request):

    workers = worker.objects.all()
    return render_to_response('worker.html',{'workers':workers})

def prise_list(request):

    all_prise =prise.objects.all()

    return render_to_response('prise.html', {'all_prise':all_prise})