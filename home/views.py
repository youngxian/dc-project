from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.


class HomeView(View):
    template_name = "home.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class WorkExprienceView(View):
    template = "work_exprience_page.html"

    def get(self, request, **kwargs):
        return render(request, self.template)