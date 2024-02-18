from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyModelForm
from .models import MyModel

def my_form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if 'save_draft' in request.POST:  
                instance.is_draft = True
                instance.save()
                return render(request, 'my_template.html', {'form': form})
            else:
                instance.save()
                return redirect('/') 
    else:
        form = MyModelForm()
    return render(request, 'my_template.html', {'form': form})

def draft_list(request):
    drafts = MyModel.objects.filter(is_draft=True)
    return render(request, 'draft_list.html', {'drafts': drafts})


def submitted_list(request):
    submitted = MyModel.objects.filter(is_draft=False)
    return render(request, 'submitted_list.html', {'submitted': submitted})

def edit_draft(request, pk):
    draft = get_object_or_404(MyModel, pk=pk, is_draft=True)
    if request.method == 'POST':
        form = MyModelForm(request.POST, instance=draft)
        if form.is_valid():
            instance = form.save(commit=False)
            if 'save_draft' in request.POST:
                instance.is_draft = True
            else:
                instance.is_draft = False
            instance.save()
            return redirect('draft_list')
    else:
        form = MyModelForm(instance=draft)
    return render(request, 'edit_draft.html', {'form': form})

def view_submitted(request, pk):
    submitted = get_object_or_404(MyModel, pk=pk, is_draft=False)
    form = MyModelForm(instance=submitted)
    return render(request, 'view_submitted.html', {'form': form})
