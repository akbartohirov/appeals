from django.shortcuts import render, redirect
from django.forms import modelform_factory, modelformset_factory
from .models import Appeal, AppealFile
from django.contrib import messages
from django.shortcuts import get_object_or_404

AppealForm = modelform_factory(Appeal, exclude=[])
AppealFileFormSet = modelformset_factory(AppealFile, fields=('file',), extra=3)

def create_appeal(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        formset = AppealFileFormSet(request.POST, request.FILES, queryset=AppealFile.objects.none())

        if form.is_valid() and formset.is_valid():
            appeal = form.save()

            for file_form in formset.cleaned_data:
                if file_form and file_form.get('file'):
                    AppealFile.objects.create(appeal=appeal, file=file_form['file'])
            messages.success(request, 'Обращение успешно создано!')
            return redirect('appeals_list')  # перенаправим на список после создания
    else:
        form = AppealForm()
        formset = AppealFileFormSet(queryset=AppealFile.objects.none())

    return render(request, 'appeals/create_appeal.html', {
        'form': form,
        'formset': formset,
    })

def appeals_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')

    appeals = Appeal.objects.all()

    if search:
        appeals = appeals.filter(name__icontains=search)
    if status:
        appeals = appeals.filter(status__icontains=status)

    return render(request, 'appeals/appeals_list.html', {
        'appeals': appeals,
        'search': search,
        'status': status
    })



def edit_appeal(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
    form = AppealForm(request.POST or None, instance=appeal)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Обращение обновлено.')
        return redirect('appeals_list')

    return render(request, 'appeals/edit_appeal.html', {'form': form, 'appeal': appeal})