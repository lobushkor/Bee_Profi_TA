from django.shortcuts import render, redirect
from .forms import TourRequestForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, 'search.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contact.html')


class TourRequestView(LoginRequiredMixin, View):
    def get(self, request):
        form = TourRequestForm(request=request)
        return render(request, 'request.html', {'form': form})

    def post(self, request):
        form = TourRequestForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('main_page:index')
        else:
            return render(request, 'request.html', {'form': form})



