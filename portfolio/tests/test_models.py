import pytest
from portfolio.models import Project, Skill


@pytest.mark.django_db()
def test_project():
    Project.objects.create(title="a_title")
    assert str(Project.objects.first()) == "a_title"
    assert Project.objects.first().is_active


@pytest.mark.django_db()
def test_skill():
    Skill.objects.create(title="a_title")
    assert str(Skill.objects.first()) == "a_title"
    assert Skill.objects.first().is_active
