from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from authentication.forms import (
    UserRegistrationForm,
    UserLoginForm
)
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login as login_,
    logout,
)
from django.views import View

from authentication.models import RegistrationStage
from .forms import StageOneForm, UserRegistrationForm, StageTwoForm
# Create your views here.


class LoginHomeView(View):

    form = UserLoginForm

    def get(self, request, **kwargs):
        context = {"form": UserLoginForm}
        return render(request, "login.html", context)

    def post(self, request):
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.is_active:
                    reg_stage = RegistrationStage.objects.get(user=user)
                    user_log = authenticate(
                        username=username, password=password)
                    if user_log:
                        login_(request, user_log)
                        if reg_stage.stage == '1':
                            return redirect('stage_one', slug=reg_stage.slug)
                        elif reg_stage.stage == '2':
                            return redirect('stage_two', slug=reg_stage.slug)
                        return redirect("home")
                else:
                    messages.error(
                        request, "Authorisation Access Suspended")
            except Exception as e:
                messages.error(
                    request, "Username/Password Incorrect")

        return render(request, "login.html", {"form": form})


class RegisterView(View):
    form = UserRegistrationForm

    def get(self, request, **kwargs):
        context = {"form": UserRegistrationForm()}
        return render(request, "register.html", context)

    def post(self, request):
        next = request.GET.get('next')
        form = self.form(request.POST)
        if form.is_valid():
            user = User()
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            if password != confirm_password:
                messages.error(request, 'Password do not match!')
            else:
                user.set_password(password)
                try:
                    with transaction.atomic():
                        user.save()
                        new_reg = RegistrationStage()
                        new_reg.user = user
                        new_reg.stage = 1
                        new_reg.save()
                        user = authenticate(
                            username=user.username, password=password)
                        if user:
                            login_(request, user)
                            return redirect('stage_one', slug=new_reg.slug)
                except Exception as e:
                    messages.error(
                        request, 'Email already used!!! {}'.format(e))
        return render(request, "register.html", {'form': form})


class StageOneView(LoginRequiredMixin, View):
    model = RegistrationStage

    def get(self, request, slug, **kwargs):
        context = {
            'form': StageOneForm()
        }
        return render(request, 'register.html', context)

    def post(self, request, slug):
        reg_stage = RegistrationStage.objects.get(slug=slug)
        form = StageOneForm(request.POST)
        if form.is_valid():
            reg_stage.about_me = form.cleaned_data['about_me']
            reg_stage.stage = 2
            reg_stage.save()
            return redirect('stage_two', slug=reg_stage.slug)


class StageTwoView(LoginRequiredMixin, View):
    model = RegistrationStage

    def get(self, request, slug, **kwargs):
        context = {
            'form': StageTwoForm()
        }
        return render(request, 'register.html', context)

    def post(self, request, slug):
        reg_stage = RegistrationStage.objects.get(slug=slug)
        form = StageTwoForm(request.POST)
        if form.is_valid():
            reg_stage.activation_code = form.cleaned_data['activation_code']
            reg_stage.stage = 3
            reg_stage.save()
            return redirect('home')
