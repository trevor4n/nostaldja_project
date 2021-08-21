from django.shortcuts import redirect, render
from .models import Decade, Fad

# Fad Show All
def fad_list(req):
    fads = Fad.objects.all()
    return render(req, 'nostaldja/fad_list.html', {'fads': fads})

# START - Fad CRUD
def fad_create(req):
    if req.method == 'POST':
        form = FadForm(req.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(req, 'fad_form', {'form': form})

def fad_detail(req, pk):
    try:
        fad = Fad.objects.get(id=pk)
    except:
        fad = {
            'name': 'Fad not found'
        }
        print(f"fad with id={pk} couldn't be found")
    return render(req, 'fad_detail', {'fad': fad})

def fad_edit(req, pk):
    fad = Fad.objects.get(pk=pk)
    if req.method == 'POST':
        form = FadForm(req.POST, instance = fad)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk = artist.pk)
    else:
        form = FadForm(instance = fad)
    return render(req, 'fad_form', {'form': form})

def fad_delete(req, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')
# END - Fad CRUD

# Decade Show All
def decade_list(req):
    decades = Decade.objects.all()
    return render(req, 'nostaldja/decade_list.html', {'decades': decades})

# START - Decade CRUD
def decade_create(req):
    if req.method == 'POST':
        form = DecadeForm(req.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(req, 'Decade_form', {'form': form})

def decade_detail(req, pk):
    try:
        decade = Decade.objects.get(id=pk)
    except:
        decade = {
            'name': 'Decade not found'
        }
        print(f"decade with id={pk} couldn't be found")
    return render(req, 'decade_detail', {'decade': decade})

def decade_edit(req, pk):
    decade = Decade.objects.get(pk=pk)
    if req.method == 'POST':
        form = DecadeForm(req.POST, instance = decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk = decade.pk)
    else:
        form = DecadeForm(instance = decade)
    return render(req, 'decade_form', {'form': form})

def decade_delete(req, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')
# END - Decade CRUD
