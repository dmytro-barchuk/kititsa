from django.shortcuts import render
from django.views.generic.list import ListView

from .models import ProjectType, Project
from info.models import HelloSection


class ProjectListView(ListView):
    model = Project
    template_name = 'projects_list.html'


    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context.update({
            'object_list': Project.objects.filter(show_on_main_screen=True)[:9],
            'hello_section': HelloSection.objects.all()[0],
        })
        return context

    def get_queryset(self):
    	context = Project.objects.filter(show_on_main_screen=True)[:9]

    	return context



    # paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context