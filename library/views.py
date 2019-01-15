from django.shortcuts import render
from .forms import SubscribeForms


def library(request):
    form = SubscribeForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        new_form = form.save()
    return render(request, 'library/library.html', locals())
