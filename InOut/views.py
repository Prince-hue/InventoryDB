from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def html_index(request):
    return render(request, 'index.html')

#adding forms and backends
def forms(request):
    return render(request, 'form.html')


def html_forms_get(request):
    dic = {
        'Name of Asset' : request.POST['nameOfAsset'],
        'Quantity' : request.POST['quantity'],
        'method' : request.method,
    }
    return JsonResponse(dic)

#trying experiment
from .models import inout
from .forms import inoutforms
from django.shortcuts import redirect
#from dal import autocomplete

def tryy(request):
    in_out = inout.objects.all()
    if request.method == 'POST':
        form = inoutforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('try')
    else:
        form = inoutforms()
    dic = {
        'inout': in_out,
        'form': form,
    }
    return render(request, 'try.html', dic)

from .models import Asset
#class AssetAutocomplete(autocomplete.Select2QuerySetView):
#    def get_queryset(self):
 #       qs = Asset.objects.none()
#
 #       if self.q:
  #          qs = Asset.objects.filter(name_of_asset__istartswith=self.q)
#
 #       return qs
    
from .forms import AssetForm

def assett(request):
    asset = Asset.objects.all()
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset')
    else:
        form = AssetForm()
    dic = {
        'asset': asset,
        'form': form,
    }
    return render(request, 'asset.html', dic)

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})