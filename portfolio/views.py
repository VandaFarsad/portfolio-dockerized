from django.db.models.query import QuerySet
from django.views.generic import TemplateView
from constance import config


from .models import Project, Skill


class BaseView(TemplateView):
    def _split_into_blocks(self, objects: QuerySet, sublist_len: int = 3) -> list:
        """Splitting a list into a nested list, where each sub list has a fixed length."""
        return [objects[i : i + sublist_len] for i in range(0, len(objects), sublist_len)]  # noqa

    def _split_paragraphs(self, content: str) -> list[str]:
        """Use this method and a for loop to add paragraphs in the template when using constance text fields."""
        return content.split(r"\p")


class IndexView(BaseView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        skills = Skill.objects.filter(is_active=True)
        projects = Project.objects.filter(is_active=True)

        context["skills"] = self._split_into_blocks(skills, 3)
        context["projects"] = self._split_into_blocks(projects, 2)
        context["about_me"] = config.ABOUT_ME
        context["more_about_me"] = self._split_paragraphs(config.MORE_ABOUT_ME)

        return context


class ImpressumView(BaseView):
    template_name = "impressum.html"
