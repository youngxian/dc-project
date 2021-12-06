from django.shortcuts import render
from django.views import View
# Create your views here.


class WorkExperienceFormView(View):
    template_name = "Forms/form_one.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name)
