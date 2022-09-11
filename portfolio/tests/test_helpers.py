import pytest
from portfolio.helpers import split_into_blocks, split_paragraphs
from portfolio.models import Skill


def test_split_into_blocks_len_1():
    splitted = split_into_blocks([1, 2], 1)
    assert splitted == [[1], [2]]


@pytest.mark.django_db()
def test_split_into_blocks_len_2():
    Skill.objects.create(title="a_title")
    Skill.objects.create(title="another_title")
    skills_splitted = split_into_blocks(Skill.objects.all(), 2)
    assert len(skills_splitted) == 1
    assert len(skills_splitted[0]) == 2


def test_split_paragraphs():
    assert split_paragraphs(r"First paragraph\pSecond paragraph") == ["First paragraph", "Second paragraph"]
