from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from main_page.models import TourRequest
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views import View

from django.contrib.auth.forms import AuthenticationForm


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    login_form = AuthenticationForm()

    def get_success_url(self):
        user = self.request.user
        if user.is_staff:
            return reverse_lazy('users:manager_profile')
        else:
            return reverse_lazy('users:profile')

    def form_invalid(self, login_form):
        messages.error(self.request, 'Невірні данні')
        return self.render_to_response(self.get_context_data(login_form=login_form))


class MyRegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main_page:index')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.get(username=username)
        login(self.request, user)
        return redirect(self.success_url)


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        tour_requests = TourRequest.objects.filter(user=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'tour_requests': tour_requests,
        }
        return render(request, 'profile.html', context)

    def post(self, request):
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Ваш профіль успішно оновлено')

            return redirect('users:profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
            }
            messages.error(request, 'Помилка оновлення профілю')

            return render(request, 'profile.html', context)


class ManagerProfileView(LoginRequiredMixin, View):
    def get(self, request):
        tour_requests = TourRequest.objects.all().order_by('-date_added')
        context = {'tour_requests': tour_requests}
        return render(request, 'manager_profile.html', context)

    def post(self, request):
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')

        tour_request = TourRequest.objects.get(id=request_id)

        if action == 'start_work':
            tour_request.status = 'в роботі'
            tour_request.save()
        elif action == 'finish_work':
            tour_request.status = 'завершено'
            tour_request.save()
        return redirect('users:manager_profile')






