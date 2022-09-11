from constance import config
from django.views.generic import TemplateView

from .helpers import split_into_blocks

from .models import Project, Skill


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        skills = Skill.objects.filter(is_active=True)
        projects = Project.objects.filter(is_active=True)

        context["skills"] = split_into_blocks(skills, 3)
        context["projects"] = split_into_blocks(projects, 2)
        context["about_me"] = config.ABOUT_ME
        context["more_about_me"] = config.MORE_ABOUT_ME.split(r"\p")

        return context


class ImpressumView(TemplateView):
    template_name = "impressum.html"
