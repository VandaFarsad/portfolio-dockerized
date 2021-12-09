from django.db.models.query import QuerySet
from django.views.generic import TemplateView

from .models import Project, Skill


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        skills = Skill.objects.filter(is_active=True)
        projects = Project.objects.filter(is_active=True)

        context["skills"] = skills
        context["projects"] = projects

        return context


class ImpressumView(TemplateView):
    template_name = "impressum.html"
